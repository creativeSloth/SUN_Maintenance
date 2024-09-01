from typing import Any, Dict, List

from sqlalchemy import Column
from sqlalchemy.orm import Session


def commit_new_entry(cls: Any, sess: Session, **m_attrs: Any) -> Any:
    r"""
    Commits a new entry in the database using the given object type and session with the
    provided keyword arguments that match the object's attributes.

    :param cls: The SQLAlchemy model class representing the database table.
    :type cls: `Any` class_model
    :param session: The SQLAlchemy session instance used to interact with the database.
    :type session: `sqlalchemy.orm.sessionmaker`
    :param kwargs: Keyword arguments that correspond to the attributes of the `cls`.
    :return: The newly created database entry.
    :rtype: `cls` instance.
    """

    new_entry = cls(**m_attrs)
    sess.add(new_entry)
    sess.commit()
    return new_entry


def ensure_list_entries_exist(
    sess: Session, cls: Any, cls_attrs: str, attr_list: List[Any]
) -> Dict[Any, Any]:
    r"""
    Ensures that a list of items `attr_list` exists as entries in a column `cls_attrs` in a table `cls` (as sqlalchemy model_class) of the database.

    :param sess: The SQLAlchemy session instance used to interact with the database.
    :type sess: `Session`
    :param cls: The SQLAlchemy model class representing the database table.
    :type cls: `Any` 'model_class'
    :param cls_attrs: The column name in the table where the list items are stored.
    :type cls_attrs: `str`
    :param attr_list: The list of items to be ensured in the `cls_attrs` column.
    :type attr_list: `List[Any]`
    :return: A dictionary where the keys are the items in `attr_list` and the values are the corresponding database entries.
    :rtype: `Dict[Any, Any]`
    """

    # Fetch existing items from the database where `cls_attrs` is in the `attr_list`
    # i.e.:
    #  existing_items = {
    #     'admin': <Roles(id=1, role_name='admin')>,
    #     'user': <Roles(id=2, role_name='user')>
    # }

    existing_items: dict[str, Any] = {
        getattr(item, cls_attrs): item for item in sess.query(cls).all()
    }

    # Add new items that are not already in the database
    items_to_add = [name for name in attr_list if name not in existing_items]

    for name in items_to_add:
        item = commit_new_entry(sess=sess, cls=cls, **{cls_attrs: name})
        sess.add(item)
        existing_items[name] = item

    sess.commit()
    return existing_items


def create_relationship(session, m1, m1_attrs, m2, m2_attrs, relationship_type):
    """
    Creates a relationship between two SQLAlchemy models and sets the provided attributes.

    :param session: SQLAlchemy session object.
    :type session: sqlalchemy.orm.Session
    :param m1: First SQLAlchemy model class.
    :type m1: sqlalchemy.ext.declarative.api.DeclarativeMeta
    :param m1_attrs: Dictionary of attributes for the first model.
    :type m1_attrs: dict
    :param m2: Second SQLAlchemy model class.
    :type m2: sqlalchemy.ext.declarative.api.DeclarativeMeta
    :param m2_attrs: Dictionary of attributes for the second model.
    :type m2_attrs: dict
    :param relationship_type: Type of relationship ('one_to_one', 'one_to_many', 'many_to_many').
    :type relationship_type: str
    :return: The two instantiated and linked objects.
    :rtype: tuple
    """
    # 1. Check for or create an instance of the first model
    instance1 = session.query(m1).filter_by(**m1_attrs).first()
    if not instance1:
        instance1 = m1(**m1_attrs)
        session.add(instance1)

    # 2. Check for or create an instance of the second model
    instance2 = session.query(m2).filter_by(**m2_attrs).first()
    if not instance2:
        instance2 = m2(**m2_attrs)
        session.add(instance2)

    # 3. Automatically determine the relationship names
    m1_relationship_name = get_relationship_name(instance1, instance2)
    m2_relationship_name = get_relationship_name(instance2, instance1)

    # 4. Set the relationship based on the relationship type
    if relationship_type == "1:1":
        setattr(instance1, m1_relationship_name, instance2)
        setattr(instance2, m2_relationship_name, instance1)
    elif relationship_type == "1:n":
        if isinstance(getattr(instance1, m1_relationship_name), list):
            getattr(instance1, m1_relationship_name).append(instance2)
        else:
            setattr(instance2, m2_relationship_name, instance1)
    elif relationship_type == "n:m":
        if isinstance(getattr(instance1, m1_relationship_name), list):
            getattr(instance1, m1_relationship_name).append(instance2)
        if isinstance(getattr(instance2, m2_relationship_name), list):
            getattr(instance2, m2_relationship_name).append(instance1)

    # 5. Save objects to the database
    session.commit()

    return instance1, instance2


def get_relationship_name(instance, related_instance):
    """
    Retrieves the name of the relationship attribute in the instance that points to the related instance.

    :param instance: The SQLAlchemy instance (the "one" or "many" side).
    :type instance: sqlalchemy.ext.declarative.api.Base
    :param related_instance: The related SQLAlchemy instance (the "many" or "one" side).
    :type related_instance: sqlalchemy.ext.declarative.api.Base
    :return: The name of the relationship attribute.
    :rtype: str
    """
    for relationship in instance.__mapper__.relationships:
        if relationship.mapper.class_ == related_instance.__class__:
            return relationship.key
    return None
