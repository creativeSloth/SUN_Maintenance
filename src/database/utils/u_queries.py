from typing import Any, Dict, List

from sqlalchemy import Column
from sqlalchemy.orm import Session


def commit_new_entry(cls: Any, sess: Session, **kwargs: Any) -> Any:
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

    new_entry = cls(**kwargs)
    sess.add(new_entry)
    sess.commit()
    return new_entry


def ensure_exists(
    sess: Session, cls: Any, cls_attr: str, attr_list: List[Any]
) -> Dict[Any, Any]:
    r"""
    Ensures that a list of items `attr_list` exists as entries in a column `cls_attr` in a table `cls` (as sqlalchemy model_class) of the database.

    :param sess: The SQLAlchemy session instance used to interact with the database.
    :type sess: `Session`
    :param cls: The SQLAlchemy model class representing the database table.
    :type cls: `Any` 'model_class'
    :param cls_attr: The column name in the table where the list items are stored.
    :type cls_attr: `str`
    :param attr_list: The list of items to be ensured in the `cls_attr` column.
    :type attr_list: `List[Any]`
    :return: A dictionary where the keys are the items in `attr_list` and the values are the corresponding database entries.
    :rtype: `Dict[Any, Any]`
    """

    # Fetch existing items from the database where `cls_attr` is in the `attr_list`
    # i.e.:
    #  existing_items = {
    #     'admin': <Roles(id=1, role_name='admin')>,
    #     'user': <Roles(id=2, role_name='user')>
    # }

    existing_items: dict[str, Any] = {
        getattr(item, cls_attr): item for item in sess.query(cls).all()
    }

    # Add new items that are not already in the database
    items_to_add = [name for name in attr_list if name not in existing_items]

    for name in items_to_add:
        item = commit_new_entry(sess=sess, cls=cls, **{cls_attr: name})
        sess.add(item)
        existing_items[name] = item

    sess.commit()
    return existing_items


def commit_new_joined_list_entry(
    db_object: Any,
    session: Session,
    secondary_id: Column,
    db_join_object: Column,
    **kwargs: Any,
) -> Any:
    r"""
    Commits a new entry in a joined list relationship using the given object type and session with the given primary key.

    :param db_object: The SQLAlchemy model class representing the database table. In ths table a new entry is created
    :type db_object: db_object's `class`
    :param session: The SQLAlchemy session instance used to interact with the database.
    :type session: `sqlalchemy.orm.sessionmaker`
    :param secondary_id: The column in the relationship table where the relationship is established.
    :type secondary_id: `sqlalchemy.Column`
    :param db_join_object: The column in the joined list table where the joined list item is stored.
    :type db_join_object: db_join_object's `class`
    :param kwargs: Keyword arguments that correspond to the attributes of the `db_object`.
    :return: The newly created database entry as an instance of the db_object's `class`
    :rtype: `db_object` instance.
    """
    kwargs[secondary_id.name] = db_join_object.id
    new_joined_list_entry = db_object(**kwargs)
    session.add(new_joined_list_entry)
    session.commit()
    return new_joined_list_entry
