from typing import Any

from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker


def commit_new_entry(db_object: Any, session: sessionmaker, **kwargs: Any) -> Any:
    r"""
    Commits a new entry in the database using the given object type and session with the
    provided keyword arguments that match the object's attributes.

    :param db_object: The SQLAlchemy model class representing the database table.
    :type db_object: db_object's `class`
    :param session: The SQLAlchemy session instance used to interact with the database.
    :type session: `sqlalchemy.orm.sessionmaker`
    :param kwargs: Keyword arguments that correspond to the attributes of the `db_object`.
    :return: The newly created database entry.
    :rtype: `db_object` instance.
    """

    new_entry = db_object(**kwargs)
    session.add(new_entry)
    session.commit()
    return new_entry


def commit_new_joined_list_entry(
    db_object: Any,
    session: sessionmaker,
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
