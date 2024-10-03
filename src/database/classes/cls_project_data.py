from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.constants.c_db_classes import *
from database.constants.c_db_classes import DB_TABLENAME_PROJECTS
from database.utils.u_db_sess import BASE


class Projects(BASE):
    r"""
    Represents a project in the system.

    Attributes
    ----------
    :param int id:
        Primary key for the project.
    :param int user_id:
        Foreign key referencing the user who created the project.
    :param int loc_address_id:
        Foreign key referencing the address where the project is located.
    :param int customer_address_id:
        Foreign key referencing the address of the customer.
    :param str date_created:
        Timestamp indicating when the project was created in ISO 8601 format.
    :param str project_no:
        Unique identifier for the project.
    :param str project_name:
        Descriptive name of the project.
    :param str sys_perf:
        Performance metrics related to the system.
    :param str comission_date:
        Date when the project was officially commissioned.
    :param str description:
        Detailed description of the project.

    Relationships
    --------------
    :param Users user:
        Reference to the Users table indicating the creator of the project.
    :param Addresses loc_address:
        Reference to the Addresses table for the project's location.
    :param Addresses customer_address:
        Reference to the Addresses table for the customer's address.
    :param list[SubSystem] sub_systems:
        Reference to the SubSystem table representing subsystems associated with the project.
    """

    __tablename__ = DB_TABLENAME_PROJECTS
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"))

    loc_address_id = Column(Integer, ForeignKey(DB_TABLENAME_ADDRESSES + ".id"))
    customer_address_id = Column(Integer, ForeignKey(DB_TABLENAME_ADDRESSES + ".id"))

    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )

    project_no = Column(String, nullable=False, unique=True)
    project_name = Column(String, nullable=False)
    sys_perf = Column(String, nullable=True)

    comission_date = Column(DateTime, nullable=True)

    description = Column(String, nullable=True)

    user = relationship(
        "Users", back_populates="projects"
    )  # Beziehungen zu den Adressen: Standort und Kundenadresse
    loc_address = relationship(
        "Addresses",
        foreign_keys=[loc_address_id],
        back_populates="projects_loc_address",
    )
    customer_address = relationship(
        "Addresses",
        foreign_keys=[customer_address_id],
        back_populates="projects_customer_address",
    )
    sub_systems = relationship("SubSystem", back_populates="project")


class Addresses(BASE):
    r"""
    Represents an address in the system.

    Attributes
    ----------
    :param int id:
        Primary key for the address.
    :param str address_line1:
        First line of the address.
    :param str address_line2:
        Second line of the address (optional).
    :param str city:
        City of the address.
    :param str state:
        State of the address.
    :param str country:
        Country of the address.
    :param str postal_code:
        Postal code of the address.

    Relationships
    --------------
    :param list[Projects] projects_loc_address:
        Reference to Projects table for location addresses.
    :param list[Projects] projects_customer_address:
        Reference to Projects table for customer addresses.
    """

    __tablename__ = DB_TABLENAME_ADDRESSES
    id = Column(Integer, primary_key=True)
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)

    projects_loc_address = relationship(
        "Projects",
        back_populates="loc_address",
        foreign_keys=[Projects.loc_address_id],
    )
    projects_customer_address = relationship(
        "Projects",
        back_populates="customer_address",
        foreign_keys=[Projects.customer_address_id],
    )
    manufacturers_address = relationship("Manufacturers", back_populates="address")


class SubSystem(BASE):
    r"""
    Represents a subsystem within a larger project, such as a photovoltaic (PV) system.
    A subsystem can have distinct properties like tilt and orientation that differ from other parts of the project.
    If the system as a whole cannot be divided into distinct subsystems, this class can represent the main system itself.

    Attributes:
        id (int):
            The primary key that uniquely identifies the subsystem in the database.

        project_id (int):
            Foreign key referencing the associated project. This indicates which project this subsystem belongs to.

        part_sys_name (str):
            The name of the subsystem. This is typically used to distinguish this part from other subsystems within the same project.

        description (str):
            A textual description providing more details about the subsystem's characteristics, function, or any other relevant information.

        tilt (float):
            The tilt angle of the subsystem, representing the vertical inclination of the system or solar panels. This is usually measured in degrees.

        orientation (float):
            The orientation angle of the subsystem, representing the horizontal direction the system is facing (e.g., south-facing or east-facing). This is also typically measured in degrees.

        is_enabled (bool):
            A flag indicating whether this subsystem is active or enabled. If True, the subsystem is considered active; if False, it is disabled.

        Relationships:
            project (relationship):
                Defines a many-to-one relationship with the 'Project' class.
                Each subsystem belongs to one project, but a project can have multiple subsystems.

            sys_inverters (relationship):
                Defines a many-to-one relationship with the 'SystemInverter' class.
                This represents the inverters associated with the subsystem, where one subsystem may have multiple inverters.
    """

    __tablename__ = DB_TABLENAME_SUB_SYSTEMS
    id = Column(Integer, primary_key=True)
    project_id = Column(
        Integer, ForeignKey(DB_TABLENAME_PROJECTS + ".id"), nullable=False
    )
    part_sys_name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    tilt = Column(Float, nullable=True)
    orientation = Column(Float, nullable=True)
    is_enabled = Column(Boolean, default=True)

    project = relationship("Projects", back_populates="sub_systems")
    sys_inverters = relationship("SystemInverters", back_populates="sub_systems")


class SystemInverters(BASE):
    r"""
    Represents a system inverter within a larger subsystem, such as a photovoltaic (PV) inverter.
    A system inverter can have distinct properties like serial number and whether it is enabled or disabled.

    Attributes:
        id (int):
            The primary key that uniquely identifies the system inverter in the database.

        part_sys_id (int):
            Foreign key referencing the associated subsystem. This indicates which subsystem this system inverter belongs to.

        inverter_id (int):
            Foreign key referencing the associated article. This indicates which article this system inverter belongs to.

        prev_sys_inv_id (int):
            Foreign key referencing the associated system inverter that this system inverter is connected to.

        next_sys_inv_id (int):
            Foreign key referencing the associated system inverter that this system inverter is connected to.

        ser_no (str):
            The serial number of the system inverter.

        is_enabled (bool):
            A flag indicating whether this system inverter is active or enabled. If True, the system inverter is considered active; if False, it is disabled.

        Relationships:
            sub_systems (relationship):
                Defines a many-to-one relationship with the 'SubSystem' class.
                Each system inverter belongs to one subsystem, but a subsystem can have multiple system inverters.

            PV_generators (relationship):
                Defines a many-to-one relationship with the 'PVGenerators' class.
                This represents the photovoltaic modules associated with the system inverter, where one system inverter
                may have multiple modules.

            inverter_type (relationship):
                Defines a many-to-one relationship with the 'Articles' class.
                Each system inverter belongs to one article, but an article can have multiple system inverters.

    """

    __tablename__ = DB_TABLENAME_SYSTEM_INVERTERS
    id = Column(Integer, primary_key=True)
    part_sys_id = Column(
        Integer, ForeignKey(DB_TABLENAME_SUB_SYSTEMS + ".id"), nullable=False
    )
    inverter_id = Column(
        Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"), nullable=False
    )
    prev_sys_inv_id = Column(
        Integer, ForeignKey(DB_TABLENAME_SYSTEM_INVERTERS + ".id"), nullable=True
    )
    next_sys_inv_id = Column(
        Integer, ForeignKey(DB_TABLENAME_SYSTEM_INVERTERS + ".id"), nullable=True
    )
    sys_inv_name = Column(String, nullable=True)
    ser_no = Column(String, nullable=True)
    date_installed = Column(DateTime, nullable=True)
    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )

    is_enabled = Column(Boolean, default=True)

    sub_systems = relationship("SubSystem", back_populates="sys_inverters")
    PV_generators = relationship("PVGenerators", back_populates="sys_inverter")
    inverter_type = relationship("Articles", back_populates="sys_inverters")


class PVGenerators(BASE):
    r"""
    Represents a photovoltaic (PV) module string within a system inverter.
    A module string is a series of connected PV modules, which can have distinct properties,
    such as the module type and whether it is enabled or disabled.

    Attributes:
        id (int):
            The primary key that uniquely identifies the PV module string in the database.

        sys_inverter_id (int):
            Foreign key that references the associated system inverter. This indicates which system inverter this module string is connected to.

        module_id (int):
            Foreign key that references the associated article (module type). This indicates which specific module type (or article) is used in this module string.

        module_count (int):
            The total number of PV modules in the module string. It represents how many modules are connected in this string.

        is_enabled (bool):
            A boolean flag indicating if the module string is active or enabled. If True, the module string is operational; if False, it is disabled or inactive.

    Relationships:

        module_type (relationship):

            Defines a many-to-one relationship with the 'Articles' class.
            Each PV module string is associated with one article (module type), but an article can be part of multiple module strings.

        sys_inverter (relationship):
            Defines a many-to-one relationship with the 'SystemInverters' class.
            Each PV module string is linked to one system inverter, but a system inverter can manage multiple module strings.
    """

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

    module_type = relationship("Articles", back_populates="PV_generators")
    sys_inverter = relationship("SystemInverters", back_populates="PV_generators")
