from typing import Any, Dict, List, Tuple, Type

from sqlalchemy.orm import Session

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
    Creates a relationship between two SQLAlchemy models and sets the provided attributes.

    Automatically determines the type of relationship between the two models.

    :param session: SQLAlchemy session object.
    :type session: Session
    :param m1: First SQLAlchemy model class.
    :type m1: Type[BASE]
    :param m1_attrs: Dictionary of attributes for the first model.
    :type m1_attrs: Dict[str, Any]
    :param m2: Second SQLAlchemy model class.
    :type m2: Type[BASE]
    :param m2_attrs: Dictionary of attributes for the second model.
    :type m2_attrs: Dict[str, Any]
    :return: The two instantiated and linked objects.
    :rtype: Tuple[BASE, BASE]
    :raises ValueError: If no relationship is found between the models or if the relationship type cannot be determined.
    """
    # 1. Check for or create an instance of the first model
    instance1 = get_or_create_instance(sess, m1, m1_attrs)

    # 2. Check for or create an instance of the second model
    instance2 = get_or_create_instance(sess, m2, m2_attrs)

    # 3. Automatically determine the relationship names and type
    m1_rship_name = get_rship_name(instance1, instance2)
    m2_rship_name = get_rship_name(instance2, instance1)

    if not m1_rship_name or not m2_rship_name:
        raise ValueError("No relationship found between the models.")

    rship_type = determine_rship_type(
        instance1, m1_rship_name, instance2, m2_rship_name
    )

    # 4. Set the relationship based on the relationship type
    if rship_type == RSHIP_TYPES[0]:
        setattr(instance1, m1_rship_name, instance2)
        setattr(instance2, m2_rship_name, instance1)

    elif rship_type == RSHIP_TYPES[1]:
        if isinstance(getattr(instance1, m1_rship_name), list):
            getattr(instance1, m1_rship_name).append(instance2)
        else:
            setattr(instance2, m2_rship_name, instance1)

    elif rship_type == RSHIP_TYPES[2]:
        if isinstance(getattr(instance1, m1_rship_name), list):
            getattr(instance1, m1_rship_name).append(instance2)
        if isinstance(getattr(instance2, m2_rship_name), list):
            getattr(instance2, m2_rship_name).append(instance1)
    else:
        raise ValueError(f"Unsupported relationship type: {rship_type}")

    # 5. Save objects to the database
    sess.commit()

    return instance1, instance2


def get_or_create_instance(sess, model, model_attrs):
    instance = sess.query(model).filter_by(**model_attrs).first()
    if not instance:
        instance = model(**model_attrs)
        sess.add(instance)
    return instance


def get_rship_name(instance: BASE, related_instance: BASE) -> str:  # type: ignore
    """
    Retrieves the name of the relationship attribute in the instance that points to the related instance.

    :param instance: The SQLAlchemy instance (the "one" or "many" side).
    :type instance: BASE
    :param related_instance: The related SQLAlchemy instance (the "many" or "one" side).
    :type related_instance: BASE
    :return: The name of the relationship attribute.
    :rtype: str
    :raises ValueError: If no relationship is found between the instances.
    """
    for rship in instance.__mapper__.relationships:
        if rship.mapper.class_ == related_instance.__class__:
            return rship.key
    raise ValueError("No relationship found between the instances.")


def determine_rship_type(
    instance1: BASE, rship_name1: str, instance2: BASE, rship_name2: str  # type: ignore
) -> str:
    """
    Determines the type of relationship between two instances based on the relationship attributes.

    :param instance1: The first SQLAlchemy instance.
    :type instance1: BASE
    :param rship_name1: The name of the relationship attribute in the first instance.
    :type rship_name1: str
    :param instance2: The second SQLAlchemy instance.
    :type instance2: BASE
    :param rship_name2: The name of the relationship attribute in the second instance.
    :type rship_name2: str
    :return: The type of relationship ('1:1', '1:n', 'n:m').
    :rtype: str
    :raises ValueError: If the relationship type cannot be determined.
    """
    attr1 = getattr(instance1, rship_name1)
    attr2 = getattr(instance2, rship_name2)

    if isinstance(attr1, list) and isinstance(attr2, list):
        return RSHIP_TYPES[2]
    elif isinstance(attr1, list) and not isinstance(attr2, list):
        return RSHIP_TYPES[1]
    elif not isinstance(attr1, list) and not isinstance(attr2, list):
        return RSHIP_TYPES[0]
    else:
        raise ValueError("Cannot determine relationship type.")
