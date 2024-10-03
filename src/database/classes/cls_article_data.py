from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.classes.cls_enums import (
    CellMatEnum,
    CommInterfaceEnum,
    InvClassesEnum,
    PhasesEnum,
)
from database.constants.c_db_classes import *
from database.utils.u_db_sess import BASE


class Manufacturers(BASE):
    r"""
    Represents a manufacturer.

    Attributes:
        id (int): Primary key for the manufacturer.
        mf_name (str): Name of the manufacturer.
        user_id (int): Foreign key referencing the user.
        address_id (int): Foreign key referencing the address.
        is_enabled (bool): Indicates if the manufacturer is enabled.
        date_created (str): Date when the manufacturer was created.
        specialized_fields (relationship): Many-to-one relationship with SpecializedFields.

        Relationships:
        user (relationship): Many-to-one relationship with Users.
    """

    __tablename__ = DB_TABLENAME_MANUFACTURERS
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"), nullable=False)

    address_id = Column(Integer, ForeignKey(DB_TABLENAME_ADDRESSES + ".id"))

    mf_name = Column(String, nullable=False)

    is_enabled = Column(Boolean, default=True)
    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )

    specialized_fields = relationship(
        "SpecializedFields", back_populates="manufacturer", uselist=False
    )
    user = relationship("Users", back_populates="manufacturers")
    address = relationship(
        "Addresses",
        foreign_keys=[address_id],
        back_populates="manufacturers_address",
    )
    articles = relationship("Articles", back_populates="manufacturer")


class SpecializedFields(BASE):
    r"""
    Represents a specialized field for a manufacturer.

    Attributes:
        id (int): Primary key for the specialized field.
        manfac_id (int): Foreign key referencing the manufacturer.
        produces_modules (bool): Indicates if the manufacturer produces modules.
        produces_inverters (bool): Indicates if the manufacturer produces inverters.
        produces_batteries (bool): Indicates if the manufacturer produces batteries.
        produces_chg_points (bool): Indicates if the manufacturer produces charge points.
        produces_com_products (bool): Indicates if the manufacturer produces communication products.
        produces_misc (bool): Indicates if the manufacturer produces miscellaneous products.

        Relationships:
        manufacturer (relationship): Many-to-one relationship with Manufacturers.
    """

    __tablename__ = DB_TABLENAME_SPECIALIZED_FIELDS
    id = Column(Integer, primary_key=True)
    manfac_id = Column(
        Integer, ForeignKey(DB_TABLENAME_MANUFACTURERS + ".id"), nullable=False
    )

    produces_modules = Column(Boolean, nullable=False)
    produces_inverters = Column(Boolean, nullable=False)
    produces_batteries = Column(Boolean, nullable=False)
    produces_chg_points = Column(Boolean, nullable=False)
    produces_com_products = Column(Boolean, nullable=False)
    produces_misc = Column(Boolean, nullable=False)

    manufacturer = relationship(
        "Manufacturers", back_populates="specialized_fields", uselist=False
    )


class Articles(BASE):
    r"""
    Represents an article produced by a manufacturer.

    Attributes:
        id (int): Primary key for the article.
        manfac_id (int): Foreign key referencing the manufacturer.
        article_name (str): Name of the article.
        article_no (str): Unique identifier for the article.
        date_created (str): Date when the article was created.

        Relationships:
        manufacturer (relationship): Many-to-one relationship with Manufacturers.
        article_types (relationship): Many-to-one relationship with ArticleTypes.
        module_details (relationship): Many-to-one relationship with ModuleDetails.
        inverter_details (relationship): Many-to-one relationship with InvertersDetails.
        user (relationship): Many-to-one relationship with Users.

    """

    __tablename__ = DB_TABLENAME_ARTICLES
    id = Column(Integer, primary_key=True)
    manfac_id = Column(
        Integer, ForeignKey(DB_TABLENAME_MANUFACTURERS + ".id"), nullable=False
    )
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"), nullable=False)

    article_name = Column(String, nullable=False)
    article_no = Column(String, nullable=False, unique=True)

    date_created = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        nullable=False,
    )

    article_types = relationship(
        "ArticleTypes", back_populates="article", uselist=False
    )
    module_types = relationship("ModuleTypes", back_populates="article", uselist=False)
    inverter_types = relationship(
        "InverterTypes", back_populates="article", uselist=False
    )
    sys_inverters = relationship("SystemInverters", back_populates="inverter_type")
    PV_generators = relationship("PVGenerators", back_populates="module_type")

    user = relationship("Users", back_populates="articles")
    manufacturer = relationship("Manufacturers", back_populates="articles")


class ArticleTypes(BASE):
    r"""
    Represents the type of an article.

    Attributes:
        id (int): Primary key for the article type.
        article_id (int): Foreign key referencing the article.
        is_module (bool): Indicates if the article is a module.
        is_inverter (bool): Indicates if the article is an inverter.
        is_battery (bool): Indicates if the article is a battery.
        is_chg_point (bool): Indicates if the article is a charge point.
        is_com_product (bool): Indicates if the article is a communication product.

        Relationships:
        article (relationship): Many-to-one relationship with Articles.
        article_types (relationship): Many-to-one relationship with ArticleTypes.
    """

    __tablename__ = DB_TABLENAME_ARTICLE_TYPES
    id = Column(Integer, primary_key=True)
    article_id = Column(
        Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"), nullable=False
    )

    description = Column(String, nullable=True)

    is_module = Column(Boolean, default=False)
    is_AC_inverter = Column(Boolean, default=False)
    is_bat_inverter = Column(Boolean, default=False)
    is_hyb_inverter = Column(Boolean, default=False)
    is_battery = Column(Boolean, default=False)
    is_chg_point = Column(Boolean, default=False)
    is_com_product = Column(Boolean, default=False)
    is_misc = Column(Boolean, default=False)

    article = relationship("Articles", back_populates="article_types", uselist=False)


class ModuleTypes(BASE):
    r"""
    Represents the details of a module.

    Attributes:
        id (int): Primary key for the module type.
        article_id (int): Foreign key referencing the article.
        description (str): Description of the module.
        cell_material (str): Material of the module's cells.
        length (int): Length of the module.
        width (int): Width of the module.
        height (int): Height of the module.
        weight (int): Weight of the module.
        has_frame (bool): Indicates if the module has a frame.
        P_MPP (float): Maximum power point power.
        U_MPP (float): Maximum power point voltage.
        I_MPP (float): Maximum power point current.
        U_oc (float): Open circuit voltage.
        I_sc (float): Short circuit current.
        μ (float): Wirkungsgrad.
        alpha (float): Temperaturkoeffizient für I_sc.
        beta (float): Temperaturkoeffizient für U_oc.
        gamma (float): Temperaturkoeffizient für P_MPP.
        cell_mat (CellMatEnum): Material of the module's cells.
        Relationships:
        article (relationship): Many-to-one relationship with Articles.
        module_type (relationship): Many-to-one relationship with ModuleTypes.
    """

    __tablename__ = DB_TABLENAME_MODULE_TYPES
    id = Column(Integer, primary_key=True)
    article_id = Column(
        Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"), nullable=False
    )

    description = Column(String, nullable=True)
    cell_material = Column(Enum(CellMatEnum), nullable=True)  # mono, poly, amorph
    length = Column(Integer, nullable=True)  # [mm]
    width = Column(Integer, nullable=True)  # [mm]
    height = Column(Integer, nullable=True)  # [mm]
    weight = Column(Integer, nullable=True)  # [kg]
    has_frame = Column(Boolean, default=True)

    P_MPP = Column(Float, nullable=True)
    U_MPP = Column(Float, nullable=True)
    I_MPP = Column(Float, nullable=True)
    U_oc = Column(Float, nullable=True)
    I_sc = Column(Float, nullable=True)

    mü = Column(Float, nullable=True)  # Wirkungsgrad
    alpha = Column(Float, nullable=True)  # Temperaturkoeffizient für I_sc
    beta = Column(Float, nullable=True)  # Temperaturkoeffizient für U_oc
    gamma = Column(Float, nullable=True)  # temperaturkoeffizient für P_MPP

    article = relationship("Articles", back_populates="module_types")


class InverterTypes(BASE):
    r"""
    Represents detailed specifications for an inverter.

    Attributes
    ----------
    :param int id:
        Primary key for the inverter type.
    :param int article_id:
        Foreign key referencing the article.
    :param str description:
        Description of the inverter.
    :param InvClassesEnum InvClass:
        Class of the inverter, categorizing its usage or design.

    Physical Dimensions
    -------------------
    :param int depth:
        Depth of the inverter in millimeters.
    :param int width:
        Width of the inverter in millimeters.
    :param int height:
        Height of the inverter in millimeters.
    :param int weight:
        Weight of the inverter in kilograms.

    Ambient Conditions
    ------------------
    :param float T_ambient_min:
        Minimum ambient temperature the inverter can operate in (°C).
    :param float T_ambient_max:
        Maximum ambient temperature the inverter can operate in (°C).

    DC Input Data
    -------------
    :param int P_dc_max:
        Maximum DC power in watts.
    :param int U_dc_min:
        Minimum DC voltage in volts.
    :param int U_dc_max:
        Maximum DC voltage in volts.
    :param int U_mpp_min:
        Minimum voltage of the maximum power point tracking (MPP) range in volts.
    :param int U_mpp_max:
        Maximum voltage of the maximum power point tracking (MPP) range in volts.
    :param int U_dc_nom:
        Nominal DC voltage in volts.
    :param int U_start:
        Start voltage in volts.
    :param float I_sc_max:
        Maximum short-circuit current for battery inverters in amperes.
    :param int mpp_trackers:
        Number of MPP trackers.
    :param int strings_per_tracker:
        Number of strings per MPP tracker.

    AC Output Data
    --------------
    :param int P_ac_nom:
        Nominal AC power in watts.
    :param int S_ac_max:
        Maximum AC apparent power in volt-amperes.
    :param str U_ac_nom:
        Nominal AC voltage in volts.
    :param int U_ac_min:
        Minimum AC voltage range in volts.
    :param int U_ac_max:
        Maximum AC voltage range in volts.
    :param float f_ac_nom:
        Nominal AC grid frequency in hertz.
    :param float I_ac_max:
        Maximum AC output current in amperes.
    :param float cos_phi:
        Power factor (cos ϕ) of the inverter.
    :param PhasesEnum feed_phases:
        Number of phases used for feeding power into the grid.
    :param float mü:
        Efficiency of the inverter as a decimal.
    :param float self_consumption:
        Self-consumption of energy by the inverter in watts.
    :param bool has_trafo:
        Indicates whether the inverter includes a transformer.

    Battery Inverter Attributes
    ---------------------------
    :param int P_discharge_max:
        Maximum discharge power from the battery in watts.
    :param int P_charge_max:
        Maximum charge power to the battery in watts.
    :param int U_bat_min:
        Minimum voltage for charging and discharging the battery in volts.
    :param int U_bat_max:
        Maximum voltage for charging and discharging the battery in volts.
    :param int I_bat_discharge:
        Maximum discharge current from the battery in amperes.
    :param int I_bat_charge:
        Maximum charge current to the battery in amperes.
    :param str bat_type:
        Type of battery compatible with the inverter.
    :param int bat_count:
        Maximum number of batteries that can be connected.
    :param int I_backup:
        Maximum current that can be supplied to each of the three backup circuits in amperes.

    Relationships
    -------------
    :param Articles article:
        The article associated with the inverter type.
    :param MPPTracker MPP_trackers:
        Relationship to MPP tracker configurations for the inverter.

    """

    __tablename__ = DB_TABLENAME_INVERTER_TYPES
    id = Column(Integer, primary_key=True)
    article_id = Column(
        Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"), nullable=False
    )

    description = Column(String, nullable=True)

    InvClass = Column(Enum(InvClassesEnum), nullable=False)  # Class of Inverter

    # Physical dimensions
    depth = Column(Integer, nullable=True)  # [mm]
    width = Column(Integer, nullable=True)  # [mm]
    height = Column(Integer, nullable=True)  # [mm]
    weight = Column(Integer, nullable=True)  # [kg]

    # Ambient parameters
    T_ambient_min = Column(Float, nullable=True)  # min ambiuent temperature
    T_ambient_max = Column(Float, nullable=True)  # max ambiuent temperature

    # DC input data
    P_dc_max = Column(Integer, nullable=True)  # Max. DC power [W]
    U_dc_min = Column(Integer, nullable=True)  # Min. DC voltage [V]
    U_dc_max = Column(Integer, nullable=True)  # Max. DC voltage [V]
    U_mpp_min = Column(Integer, nullable=True)  # MPP voltage range (min) [V]
    U_mpp_max = Column(Integer, nullable=True)  # MPP voltage range (max) [V]
    U_dc_nom = Column(Integer, nullable=True)  # Nominal DC voltage [V]
    U_start = Column(Integer, nullable=True)  # Start voltage [V]

    mpp_trackers = Column(Integer, nullable=True)  # Number of MPP trackers
    strings_per_tracker = Column(Integer, nullable=True)  # Strings per MPP tracker

    # AC output data
    P_ac_nom = Column(Integer, nullable=True)  # Nominal AC power [W]
    S_ac_max = Column(Integer, nullable=True)  # Max. AC apparent power [VA]
    U_ac_nom = Column(String, nullable=True)  # Nominal AC voltage [V]
    U_ac_min = Column(Integer, nullable=True)  # AC voltage range (min) [V]
    U_ac_max = Column(Integer, nullable=True)  # AC voltage range (max) [V]
    f_ac_nom = Column(Float, nullable=True)  # AC grid frequency [Hz]
    I_ac_max = Column(Float, nullable=True)  # Max. AC output current [A]
    cos_phi = Column(Float, nullable=True)  # Power factor (cos ϕ)
    feed_phases = Column(Enum(PhasesEnum), nullable=True)  # Feed phases
    mü = Column(Float, nullable=True)  # efficiency
    self_consumption = Column(Float, nullable=True)  # Energy self-consumption
    has_trafo = Column(Boolean, default=False)  # Has transformator

    # Battery Inverter attributes

    P_discharge_max = Column(Integer, nullable=True)  # Max. Discharge power [W]
    P_charge_max = Column(Integer, nullable=True)  # Max. Charge power [W]
    U_bat_min = Column(
        Integer, nullable=True
    )  # Minimum voltage for charging and discharging battery [V]
    U_bat_max = Column(
        Integer, nullable=True
    )  # Maximum voltage for charging and discharging battery [V]
    I_bat_discharge = Column(
        Integer, nullable=True
    )  # Maximum current for discharging battery [A]
    I_bat_charge = Column(
        Integer, nullable=True
    )  # Maximum current for charging battery [A]
    bat_type = Column(String, nullable=True)  # Type of battery
    bat_count = Column(
        Integer, nullable=True
    )  # Number of batteries that can be connected
    I_backup = Column(
        Integer, nullable=True
    )  # Current that can be used in each of 3 curcuits in backup

    # Communication parameters
    com_interface = Column(
        Enum(CommInterfaceEnum), nullable=True
    )  # Communication Interface

    article = relationship("Articles", back_populates="inverter_types")
    MPP_trackers = relationship("MPPTracker", back_populates="inverter_type")


class MPPTracker(BASE):
    """
    A class to represent MPP tracker configurations for inverter types.

    Attributes
    :param int id:
    :param int inv_types_id:
    :param str tracker_name:
    :param int string_count:
    :param float I_dc_max:
    :param float I_sc_max:
    Relationships
    :param InverterTypes inverter_type:
        The inverter type associated with the MPP tracker configuration.
    """

    __tablename__ = DB_TABLENAME_MPP_TRACKERS
    id = Column(Integer, primary_key=True)
    inv_types_id = Column(
        Integer, ForeignKey(DB_TABLENAME_INVERTER_TYPES + ".id"), nullable=False
    )
    tracker_name = Column(String, nullable=True)  # tracker name
    string_count = Column(Integer, nullable=True)  # string count
    I_dc_max = Column(Float, nullable=True)  # Max. DC input current [A]
    I_sc_max = Column(Float, nullable=True)  # Max. short curcuit current

    inverter_type = relationship("InverterTypes", back_populates="MPP_trackers")
