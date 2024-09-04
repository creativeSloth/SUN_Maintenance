from typing import Any, Dict, List, Optional, Tuple, Type

from sqlalchemy.orm import RelationshipProperty, Session, class_mapper

from database.constants.c_db_classes import RSHIP_TYPES
from database.utils.u_db_sess import BASE


def commit_new_entry(cls: Type[BASE], sess: Session, **m_attrs: Any) -> BASE:  # type: ignore
    """
    Commits a new entry in the database using the given SQLAlchemy model class and session
    with the provided keyword arguments that match the model's attributes.

    :param cls: The SQLAlchemy model class representing the database table.
    :type cls: Type[BASE]
    :param sess: The SQLAlchemy session instance used to interact with the database.
    :type sess: Session
    :param m_attrs: Keyword arguments that correspond to the attributes of the model class.
    :return: The newly created database entry.
    :rtype: BASE
    """
    new_entry = cls(**m_attrs)
    sess.add(new_entry)
    sess.commit()
    return new_entry


def ensure_list_entries_exist(
    sess: Session, cls: Type[BASE], cls_attrs: str, attr_list: List[Any]  # type: ignore
) -> Dict[Any, BASE]:  # type: ignore
    """
    Ensures that a list of items exists as entries in a column of a table represented by the SQLAlchemy model.

    :param sess: The SQLAlchemy session instance used to interact with the database.
    :type sess: Session
    :param cls: The SQLAlchemy model class representing the database table.
    :type cls: Type[BASE]
    :param cls_attrs: The column name in the table where the list items should be stored.
    :type cls_attrs: str
    :param attr_list: The list of items to ensure in the column.
    :type attr_list: List[Any]
    :return: A dictionary where the keys are the items and the values are the corresponding database entries.
    :rtype: Dict[Any, BASE]
    """
    # Fetch existing items from the database
    existing_items: Dict[Any, BASE] = {  # type: ignore
        getattr(item, cls_attrs): item for item in sess.query(cls).all()
    }

    # Identify items to add
    items_to_add = [name for name in attr_list if name not in existing_items]

    for name in items_to_add:
        item = commit_new_entry(cls=cls, sess=sess, **{cls_attrs: name})
        existing_items[name] = item

    return existing_items


def create_rshp(
    sess: Session,
    m1: Type[BASE],  # type: ignore
    m1_attrs: Dict[str, Any],
    m2: Type[BASE],  # type: ignore
    m2_attrs: Dict[str, Any],
) -> Tuple[BASE, BASE]:  # type: ignore
    """
    Creates and establishes a relationship between two SQLAlchemy model instances based on their classes and attributes.

    This function performs the following steps:
    1. Retrieves or creates instances of the specified SQLAlchemy models (`m1` and `m2`) using the provided attributes (`m1_attrs` and `m2_attrs`).
    2. Automatically identifies the relationship names between the two instances by inspecting their SQLAlchemy mappings.
    3. Determines the type of relationship (e.g., one-to-one, one-to-many, many-to-many) between the two instances.
    4. Sets up the relationship between the instances based on the determined relationship type.
    5. Commits the changes to the database to persist the relationship.

    **Relationship Types Handled:**
    - **One-to-One (`RSHIP_TYPES[0]`):** Both instances reference each other as single objects.
    - **One-to-Many (`RSHIP_TYPES[1]`):** One instance holds a collection (e.g., list) of the other instance.
    - **Many-to-Many (`RSHIP_TYPES[2]`):** Both instances hold collections of each other.


    :param sess: The SQLAlchemy session used for database operations.
    :type sess: Session
    :param m1: The class of the first SQLAlchemy model.
    :type m1: Type[BASE]
    :param m1_attrs: A dictionary of attributes to filter the query or to use for creating the first instance.
    :type m1_attrs: Dict[str, Any]
    :param m2: The class of the second SQLAlchemy model.
    :type m2: Type[BASE]
    :param m2_attrs: A dictionary of attributes to filter the query or to use for creating the second instance.
    :type m2_attrs: Dict[str, Any]
    :return: A tuple containing the two instances that have been linked.
    :rtype: Tuple[BASE, BASE]
    :raises ValueError: If no relationship is found between the models or if the relationship type cannot be determined.
    """
    # 1. Check for or create an instance of the first model
    m1_instance = get_or_create_instance(sess, m1, m1_attrs)

    # 2. Check for or create an instance of the second model
    m2_instance = get_or_create_instance(sess, m2, m2_attrs)

    # 3. Automatically determine the relationship names and type
    m1_rship_name = get_rship_name(m1, m2)
    m2_rship_name = get_rship_name(m2, m1)

    if not m1_rship_name or not m2_rship_name:
        raise ValueError("No relationship found between the models.")

    rship_type = determine_rship_type(
        m1_instance, m1_rship_name, m2_instance, m2_rship_name
    )

    # 4. Set the relationship based on the relationship type
    if rship_type == RSHIP_TYPES[0]:
        setattr(m1_instance, m1_rship_name, m2_instance)
        setattr(m2_instance, m2_rship_name, m1_instance)

    elif rship_type == RSHIP_TYPES[1]:
        if isinstance(getattr(m1_instance, m1_rship_name), list):
            getattr(m1_instance, m1_rship_name).append(m2_instance)
        else:
            setattr(m2_instance, m2_rship_name, m1_instance)

    elif rship_type == RSHIP_TYPES[2]:
        if isinstance(getattr(m1_instance, m1_rship_name), list):
            getattr(m1_instance, m1_rship_name).append(m2_instance)
        # if isinstance(getattr(m2_instance, m2_rship_name), list):
        #     getattr(m2_instance, m2_rship_name).append(m1_instance)
    else:
        raise ValueError(f"Unsupported relationship type: {rship_type}")

    # 5. Save objects to the database
    return m1_instance, m2_instance


def get_or_create_instance(sess, m: Type[BASE], m_attrs: Dict[str, Any]) -> BASE:  # type: ignore
    """
    Retrieves an instance of a SQLAlchemy model from the database that matches the provided attributes,
    or creates a new instance if no matching record is found.

    This function first queries the database to find an existing record that matches the provided attributes.
    If a matching instance is found, it is returned. If no matching instance exists, a new instance is created
    using the provided attributes, added to the current session, and returned. The instance is not committed to
    the database within this function, leaving that responsibility to the caller.

    :param sess: The SQLAlchemy session used for querying the database.
    :type sess: Session
    :param m: The SQLAlchemy model class to query or instantiate.
    :type m: Type[BASE]
    :param m_attrs: A dictionary of attributes to filter the query or to use for creating a new instance.
    :type m_attrs: Dict[str, Any]
    :return: The retrieved or newly created instance of the model.
    :rtype: BASE
    """
    instance = sess.query(m).filter_by(**m_attrs).first()
    if not instance:
        instance = m(**m_attrs)
        sess.add(instance)
    return instance


def get_rship_name(m1: Type[BASE], m2: Type[BASE]) -> Optional[str]:  # type: ignore
    """
    Determines the name of the relationship between two SQLAlchemy model class, if such a relationship exists.

    This function inspects the attributes of the first model class to identify a relationship with the second
    model class. It utilizes SQLAlchemy's class mapping to iterate over all properties of the first class,
    checking each property to see if it represents a relationship. If a relationship is found that links the
    two classes, the function returns the name of that relationship. If no relationship is found, it returns `None`.

    :param m1: The first SQLAlchemy model class.
    :type m1: Type[BASE]
    :param m2: The second SQLAlchemy model clas.
    :type m2: Type[BASE]
    :return: The name of the relationship attribute as a string, or `None` if no relationship is found.
    :rtype: Optional[str]
    """
    # Get the mapper for the first class
    mapper = class_mapper(m1)

    # Iterate over all relationship properties
    for prop in mapper.iterate_properties:
        if isinstance(prop, RelationshipProperty):
            # Check if the second class is linked by this relationship
            if prop.mapper.class_ == m2:
                return prop.key  # Return the name of the relationship

    return None


def determine_rship_type(
    instance1: BASE, m1_rship_name: str, instance2: BASE, m2_rship_name: str  # type: ignore
) -> str:
    """
    Determines the type of relationship between two SQLAlchemy model instances.

    This function evaluates the relationship type between two SQLAlchemy model instances based on the
    attributes of the instances. It checks if the attributes corresponding to the relationship names
    are lists (indicating a one-to-many or many-to-many relationship) or single objects
    (indicating a one-to-one relationship). The function returns a string indicating the relationship type.

    The possible relationship types returned are:
    - `RSHIP_TYPES[0]`: One-to-one relationship.
    - `RSHIP_TYPES[1]`: One-to-many or many-to-one relationship.
    - `RSHIP_TYPES[2]`: Many-to-many relationship.

    :param instance1: The first SQLAlchemy model instance.
    :type instance1: BASE
    :param m1_rship_name: The name of the relationship attribute in the first model instance.
    :type m1_rship_name: str
    :param instance2: The second SQLAlchemy model instance.
    :type instance2: BASE
    :param m2_rship_name: The name of the relationship attribute in the second model instance.
    :type m2_rship_name: str
    :return: The type of the relationship between the two instances.
    :rtype: str
    :raises ValueError: If the relationship type cannot be determined.
    """
    if hasattr(instance1, m1_rship_name) and hasattr(instance2, m2_rship_name):
        if isinstance(getattr(instance1, m1_rship_name), list) or isinstance(
            getattr(instance2, m2_rship_name), list
        ):
            return RSHIP_TYPES[2]
        else:
            return RSHIP_TYPES[0]
    elif hasattr(instance1, m1_rship_name) or hasattr(instance2, m2_rship_name):
        return RSHIP_TYPES[1]
    else:
        raise ValueError("Could not determine relationship type.")
