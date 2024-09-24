from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.classes.cls_enums import CellMatEnum, PhasesEnum
from database.constants.c_db_classes import *
from database.utils.u_db_sess import BASE


class Manufacturers(BASE):
    r"""
    Represents a manufacturer.

    Attributes:
        id (int): Primary key for the manufacturer.
        mf_name (str): Name of the manufacturer.
        user_id (int): Foreign key referencing the user.
        is_enabled (bool): Indicates if the manufacturer is enabled.
        date_created (str): Date when the manufacturer was created.
        specialized_fields (relationship): Many-to-one relationship with SpecializedFields.

        Relationships:
        user (relationship): Many-to-one relationship with Users.
    """

    __tablename__ = DB_TABLENAME_MANUFACTURERS
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"))

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
    manfac_id = Column(Integer, ForeignKey(DB_TABLENAME_MANUFACTURERS + ".id"))

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
    manfac_id = Column(Integer, ForeignKey(DB_TABLENAME_MANUFACTURERS + ".id"))
    user_id = Column(Integer, ForeignKey(DB_TABLENAME_USERS + ".id"))

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
    module_details = relationship(
        "ModuleDetails", back_populates="article", uselist=False
    )
    inverter_details = relationship(
        "InvertersDetails", back_populates="article", uselist=False
    )
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
    article_id = Column(Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"))

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


class ModuleDetails(BASE):
    r"""
    Represents the details of a module.

    Attributes:
        id (int): Primary key for the module details.
        article_id (int): Foreign key referencing the article.
        description (str): Description of the module.
        cell_material (str): Material of the module's cells.
        lenght (int): Length of the module.
        width (int): Width of the module.
        height (int): Height of the module.
        weight (int): Weight of the module.
        frame (bool): Indicates if the module has a frame.
        P_MPP (float): Maximum power point power.
        U_MPP (float): Maximum power point voltage.
        I_MPP (float): Maximum power point current.
        U_oc (float): Open-circuit voltage.
        I_sc (float): Short-circuit current.
        μ (float): Wirkungsgrad.
        alpha (float): Temperaturkoeffizient für I_sc.
        beta (float): Temperaturkoeffizient für U_oc.
        gamma (float): Temperaturkoeffizient für P_MPP.

        Relationships:
        article (relationship): Many-to-one relationship with Articles.
        module_details (relationship): Many-to-one relationship with ModuleDetails.

    """

    __tablename__ = DB_TABLENAME_MODULE_DETAILS
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"))

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

    article = relationship("Articles", back_populates="module_details")


class InvertersDetails(BASE):
    r"""
    Represents detailed specifications for an inverter.

    Attributes:
        id (int): Primary key for the inverter details.
        article_id (int): Foreign key referencing the associated article.
        description (str): Description of the inverter model.

        # Physical dimensions
        depth (int): Depth of the inverter in millimeters.
        width (int): Width of the inverter in millimeters.
        height (int): Height of the inverter in millimeters.
        weight (int): Weight of the inverter in kilograms.

        # Ambient parameters
        T_ambient (float): Ambient temperature in degrees Celsius.

        # DC input data
        P_dc_max (int): Maximum DC power input in watts.
        U_dc_max (int): Maximum DC voltage in volts.
        U_mpp_min (int): Minimum voltage in the MPP (Maximum Power Point) range.
        U_mpp_max (int): Maximum voltage in the MPP range.
        U_dc_nom (int): Nominal DC voltage.
        U_dc_min (int): Minimum DC voltage.
        U_start (int): Start voltage for the inverter.
        I_dc_max (float): Maximum DC input current in amperes.
        mpp_trackers (int): Number of MPP trackers available.
        strings_per_tracker (int): Number of strings per MPP tracker.

        # AC output data
        P_ac_nom (int): Nominal AC power output in watts.
        S_ac_max (int): Maximum AC apparent power in volt-amperes (VA).
        U_ac_nom (str): Nominal AC voltage.
        U_ac_min (int): Minimum AC voltage.
        U_ac_max (int): Maximum AC voltage.
        f_ac_nom (float): Nominal AC grid frequency in Hertz.
        I_ac_max (float): Maximum AC output current in amperes.
        cos_phi (float): Power factor (cos φ) of the inverter.
        feed_phases (Enum): The number of feed phases (single-phase, three-phase, etc.).

        # Efficiency and consumption
        mü (float): Efficiency of the inverter (Wirkungsgrad).
        self_consumption (float): Self-consumption of energy in watts.
        has_trafo (bool): Whether the inverter has an integrated transformer.

        article (relationship): Relationship to the Articles table for accessing associated article data.
    """

    __tablename__ = DB_TABLENAME_INVERTERS_DETAILS
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey(DB_TABLENAME_ARTICLES + ".id"))

    description = Column(String, nullable=True)

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
    I_sc_max = Column(
        Float, nullable=True
    )  # Max. Short circuit corrent (Bat-inverters)
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

    article = relationship("Articles", back_populates="inverter_details")
    MPP_trackers = relationship("MPPTracker", back_populates="inverter_details")


class MPPTracker(BASE):
    __tablename__ = DB_TABLENAME_MPP_TRACKERS
    id = Column(Integer, primary_key=True)
    inv_det_id = Column(
        Integer, ForeignKey(DB_TABLENAME_INVERTERS_DETAILS + ".id"), nullable=False
    )
    tracker_name = Column(String, nullable=True)  # tracker name
    string_count = Column(Integer, nullable=True)  # string count
    I_dc_max = Column(Float, nullable=True)  # Max. DC input current [A]

    inverters_detail = relationship("InvertersDetails", back_populates="MPP_trackers")
