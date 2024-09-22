from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.constants.c_db_classes import *
from database.utils.u_db_sess import BASE


class Manufacturers(BASE):
    __tablename__ = DB_TABLENAME_MANUFACTURERS
    id = Column(Integer, primary_key=True)

    mf_name = Column(String, nullable=False)
    user_id = Column(Boolean, default=False)

    is_enabled = Column(Boolean, default=True)
    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )

    specialized_fields = relationship(
        "SpecializedFields", back_populates="manufacturer", uselist=False
    )
    user = relationship("Users", back_populates=DB_TABLENAME_MANUFACTURERS)


class SpecializedFields(BASE):
    __tablename__ = DB_TABLENAME_SPECIALIZED_FIELDS
    id = Column(Integer, primary_key=True)
    produces_modules = Column(Boolean, nullable=False)
    produces_inverters = Column(Boolean, nullable=False)
    produces_batteries = Column(Boolean, nullable=False)
    produces_chg_points = Column(Boolean, nullable=False)
    produces_com_products = Column(Boolean, nullable=False)
    produces_misc = Column(Boolean, nullable=False)

    manufacturer = relationship(
        "Manufacturers", back_populates=DB_TABLENAME_SPECIALIZED_FIELDS, uselist=False
    )
