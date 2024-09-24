from ast import For
from datetime import datetime
from enum import Enum
from faulthandler import is_enabled
from turtle import tilt

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, Nullable, String
from sqlalchemy.orm import relationship

from database.constants.c_db_classes import *
from database.constants.c_db_classes import DB_TABLENAME_PROJECTS
from database.utils.u_db_sess import BASE


class Projects(BASE):
    __tablename__ = DB_TABLENAME_PROJECTS
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"))

    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )

    project_no = Column(String, nullable=False, unique=True)
    project_name = Column(String, nullable=False)
    sys_perf = Column(String, nullable=True)

    comission_date = Column(String, nullable=True)

    loc_address = Column(String, nullable=True)
    customer_address = Column(String, nullable=True)

    description = Column(String, nullable=True)

    user = relationship("Users", back_populates="projects")
    partial_systems = relationship("PartialSystems", back_populates="project")


class PartialSystems(BASE):
    __tablename__ = DB_TABLENAME_PARTIAL_SYSTEMS
    id = Column(Integer, primary_key=True)
    project_id = Column(
        Integer, ForeignKey(DB_TABLENAME_PROJECTS + ".id"), nullable=False
    )
    part_sys_name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    tilt = Column(Float, nullable=True)
    orientation = Column(Float, nullable=True)
    is_enabled = Column(Boolean, default=True)

    project = relationship("Projects", back_populates="partial_systems")
    sys_inverters = relationship("SystemInverters", back_populates="partial_system")


class SystemInverters(BASE):
    __tablename__ = DB_TABLENAME_SYSTEM_INVERTERS
    id = Column(Integer, primary_key=True)
    part_sys_id = Column(
        Integer, ForeignKey(DB_TABLENAME_PARTIAL_SYSTEMS + ".id"), nullable=False
    )
    inverter_id = Column(
        Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"), nullable=False
    )
    is_enabled = Column(Boolean, default=True)

    partial_system = relationship("PartialSystems", back_populates="sys_inverters")
    PV_generators = relationship("PVGenerators", back_populates="system_inverter")
    inverter = relationship("Articles", back_populates="system_inverters")


class PVGenerators(BASE):
    __tablename__ = DB_TABLENAME_PV_GENERATORS
    id = Column(Integer, primary_key=True)
    sys_inverter_id = Column(
        Integer, ForeignKey(DB_TABLENAME_SYSTEM_INVERTERS + ".id"), nullable=False
    )
    module_id = Column(
        Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"), nullable=False
    )
    module_count = Column(Integer, nullable=False)

    is_enabled = Column(Boolean, default=True)

    module = relationship("Articles", back_populates="PV_generators")
    system_inverter = relationship("SystemInverters", back_populates="PV_generators")
