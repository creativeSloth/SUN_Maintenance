from ast import Tuple
from typing import List, Optional

from sqlalchemy.orm import joinedload, sessionmaker

from database.classes.cls_article_data import (
    Articles,
    ArticleTypes,
    InverterTypes,
    Manufacturers,
    ModuleTypes,
    SpecializedFields,
)
from database.classes.cls_enums import (
    BatTypeEnum,
    CellMatEnum,
    InvClassesEnum,
    PhasesEnum,
    get_enum_value,
)
from database.classes.cls_project_data import Addresses
from database.utils.u_db_sess import BASE, create_session
from ui.classes.dialog_forms import ArticleAttrDialog, ManufacturerAttrDialog


def get_manufacturers_infos(
    manufacturer_id: Optional[int] = None,
) -> List[Manufacturers]:
    r"""
    Retrieves manufacturer information from the database based on the given manufacturer ID.

    :param manufacturer_id: The ID of the manufacturer whose information should be retrieved.
    :type manufacturer_id: Optional[int]
    :return: A list of manufacturers objects containing the requested manufacturer information.
    :rtype: List[Manufacturers]
    """

    sess: sessionmaker = create_session()
    try:
        query = sess.query(Manufacturers).options(
            joinedload(Manufacturers.specialized_fields),
            joinedload(Manufacturers.address),
        )

        if manufacturer_id is not None:
            query = query.filter(Manufacturers.id == manufacturer_id)

        manfac_infos: List[Manufacturers] = query.all()
        return manfac_infos
    finally:
        sess.close()


def refresh_mf_inf(window: ManufacturerAttrDialog, mf_inf: Manufacturers):
    mf_inf_old = None

    if mf_inf:
        mf_inf_old: type(BASE) = get_manufacturers_infos(mf_inf.id)[0]  # type: ignore
    sess: sessionmaker = create_session()
    try:
        if mf_inf_old:
            mf_inf = sess.merge(mf_inf_old)

        else:
            mf_inf = Manufacturers()
            sess.add(mf_inf)

        if not mf_inf.address:
            mf_inf.address = Addresses()

        if not mf_inf.specialized_fields:
            mf_inf.specialized_fields = SpecializedFields()

        if not mf_inf_old:
            mf_inf.user_id = window.session_user_id
        mf_inf.is_enabled = bool(window.ui.is_enabled_cbox.checkState())
        mf_inf.mf_name = window.ui.manufacturer_name_txt.text()
        mf_inf.address.address_line1 = window.ui.address_line_1_txt.text()
        mf_inf.address.address_line2 = window.ui.address_line_2_txt.text()
        mf_inf.address.city = window.ui.city_txt.text()
        mf_inf.address.postal_code = window.ui.postal_code_txt.text()
        mf_inf.address.state = window.ui.state_txt.text()
        mf_inf.address.country = window.ui.country_txt.text()

        mf_inf.specialized_fields.produces_modules = bool(
            window.ui.produces_modules_cbox.checkState()
        )
        mf_inf.specialized_fields.produces_inverters = bool(
            window.ui.produces_inverters_cbox.checkState()
        )
        mf_inf.specialized_fields.produces_batteries = bool(
            window.ui.produces_batteries_cbox.checkState()
        )
        mf_inf.specialized_fields.produces_chg_points = bool(
            window.ui.produces_chg_points_cbox.checkState()
        )
        mf_inf.specialized_fields.produces_com_products = bool(
            window.ui.produces_com_cbox.checkState()
        )
        mf_inf.specialized_fields.produces_misc = bool(
            window.ui.produces_misc_cbox.checkState()
        )

        sess.commit()

        window.mainwindow.on_menu_manufacturers_btn_click()

    except Exception as e:
        sess.rollback()  # Rollback bei einem Fehler
        print(f"Error occurred: {e}")

    finally:
        # Sitzung schließen
        sess.close()


def get_articles_infos(
    article_id: Optional[int] = None,
) -> List[Articles]:
    r"""
    Retrieves article information from the database based on the given article ID.

    :param article_id: The ID of the article whose information should be retrieved.
    :type article_id: Optional[int]
    :return: A list of articles objects containing the requested article information.
    :rtype: List[Articles]
    """

    sess: sessionmaker = create_session()
    try:
        query = sess.query(Articles).options(
            joinedload(Articles.article_types),
            joinedload(Articles.module_type),
            joinedload(Articles.inverter_type),
            joinedload(Articles.manufacturer),
        )

        if article_id is not None:
            query = query.filter(Articles.id == article_id)

        article_infos: List[Articles] = query.all()
        return article_infos
    finally:
        sess.close()


def refresh_article_inf(window: ArticleAttrDialog, articles_inf: type(BASE)):  # type: ignore
    # Erhalte die alte Artikelinformation, falls vorhanden
    articles_inf_old = None
    if articles_inf:
        articles_inf_old = get_articles_infos(articles_inf.id)[0]  # type: ignore

    sess: sessionmaker = create_session()

    try:
        # Wenn alte Artikelinformationen vorhanden sind, aktualisiere das Objekt
        if articles_inf_old:
            articles_inf = sess.merge(articles_inf_old)
        else:
            articles_inf = Articles()  # Neues Artikelobjekt erstellen
            sess.add(articles_inf)

        # Übertragen der Daten von der Benutzeroberfläche in das Artikelobjekt
        articles_inf.is_enabled = bool(window.ui.is_enabled_cbox.checkState())
        articles_inf.article_name = window.ui.article_name_txt.text()
        articles_inf.article_no = window.ui.article_no_txt.text()

        manfacs_lst: List[Manufacturers] = [
            manfac for manfac in get_manufacturers_infos()
        ]
        manfac_existed: bool = False
        for manfac in manfacs_lst:
            if window.ui.manufacturer_name_txt.text() == manfac.mf_name:
                articles_inf.manufacturer = sess.merge(
                    get_manufacturers_infos(manufacturer_id=manfac.id)[0]
                )
                manfac_existed = True
                break
        if not manfac_existed:
            articles_inf.manufacturer = Manufacturers(
                mf_name=window.ui.manufacturer_name_txt.text(),
                user_id=window.session_user_id,
            )

        # Artikeltyp
        if not articles_inf.article_types:
            articles_inf.article_types = ArticleTypes()

        articles_inf.article_types.is_battery = bool(
            window.ui.is_battery_cbox.checkState()
        )

        articles_inf.article_types.is_com_product = bool(
            window.ui.is_com_product_cbox.checkState()
        )
        articles_inf.article_types.is_module = bool(
            window.ui.is_module_cbox.checkState()
        )
        articles_inf.article_types.is_chg_point = bool(
            window.ui.is_chg_point_cbox.checkState()
        )
        articles_inf.article_types.is_misc = bool(window.ui.is_misc_cbox.checkState())
        articles_inf.article_types.is_inverter = bool(
            window.ui.is_inv_cbox.checkState()
        )

        # Modul-Attribute
        if not articles_inf.module_type:
            articles_inf.module_type = ModuleTypes()

        articles_inf.module_type.has_frame = bool(window.ui.has_frame_cbox.checkState())

        articles_inf.module_type.cell_material = get_enum_value(
            CellMatEnum, window.ui.cell_mat_cobox.currentText()
        )  # Enum-Wert
        articles_inf.module_type.description = window.ui.description_txt.text()
        articles_inf.module_type.length = window.ui.module_length_sbox.value()
        articles_inf.module_type.width = window.ui.module_width_sbox.value()
        articles_inf.module_type.height = window.ui.module_height_sbox.value()
        articles_inf.module_type.weight = window.ui.module_weight_sbox.value()
        articles_inf.module_type.P_MPP = window.ui.P_MPP_sbox.value()
        articles_inf.module_type.U_MPP = window.ui.U_MPP_sbox.value()
        articles_inf.module_type.I_MPP = window.ui.I_MPP_sbox.value()
        articles_inf.module_type.U_oc = window.ui.U_OC_sbox.value()
        articles_inf.module_type.I_sc = window.ui.I_SC_sbox.value()
        articles_inf.module_type.mue = window.ui.mue_sbox.value()
        articles_inf.module_type.alpha = window.ui.alpha_sbox.value()
        articles_inf.module_type.beta = window.ui.beta_sbox.value()
        articles_inf.module_type.gamma = window.ui.gamma_sbox.value()
        articles_inf.module_type.NOCT = window.ui.NOCT_sbox.value()

        # Wechselrichter-Attribute
        if not articles_inf.inverter_type:
            articles_inf.inverter_type = InverterTypes()

        articles_inf.inverter_type.description = window.ui.inv_description_txt.text()
        articles_inf.inverter_type.InvClass = get_enum_value(
            InvClassesEnum, window.ui.inv_type_cobox.currentText()
        )  # Enum-Wert
        articles_inf.inverter_type.length = window.ui.inv_length_sbox.value()
        articles_inf.inverter_type.width = window.ui.inv_width_sbox.value()
        articles_inf.inverter_type.height = window.ui.inv_height_sbox.value()
        articles_inf.inverter_type.weight = window.ui.inv_weight_sbox.value()
        articles_inf.inverter_type.T_ambient_min = window.ui.T_ambient_min_sbox.value()
        articles_inf.inverter_type.T_ambient_max = window.ui.T_ambient_max_sbox.value()
        articles_inf.inverter_type.P_dc_max = window.ui.P_dc_max_sbox.value()
        articles_inf.inverter_type.U_dc_min = window.ui.U_dc_min_sbox.value()
        articles_inf.inverter_type.U_dc_max = window.ui.U_dc_max_sbox.value()
        articles_inf.inverter_type.U_mpp_min = window.ui.U_MPP_min_sbox.value()
        articles_inf.inverter_type.U_mpp_max = window.ui.U_MPP_max_sbox.value()
        articles_inf.inverter_type.U_dc_nom = window.ui.U_dc_nom_sbox.value()
        articles_inf.inverter_type.U_start = window.ui.U_start_sbox.value()
        articles_inf.inverter_type.P_ac_nom = window.ui.P_ac_nom_sbox.value()
        articles_inf.inverter_type.S_ac_max = window.ui.S_ac_max_sbox.value()
        articles_inf.inverter_type.U_ac_min = window.ui.U_ac_min_sbox.value()
        articles_inf.inverter_type.U_ac_max = window.ui.U_ac_max_sbox.value()
        articles_inf.inverter_type.f_ac_nom = window.ui.f_ac_nom_sbox.value()
        articles_inf.inverter_type.U_ac_nom = window.ui.U_ac_nom_sbox.value()
        articles_inf.inverter_type.I_ac_max = window.ui.I_ac_max_sbox.value()
        articles_inf.inverter_type.cos_phi = window.ui.cos_phi_sbox.value()
        articles_inf.inverter_type.feed_phases = get_enum_value(
            PhasesEnum, window.ui.feed_phases_cobox.currentText()
        )  # Enum-Wert
        articles_inf.inverter_type.mue = window.ui.inv_mue_sbox.value()
        articles_inf.inverter_type.self_consumption = (
            window.ui.self_consumption_sbox.value()
        )
        articles_inf.inverter_type.has_trafo = bool(
            window.ui.has_trafo_cbox.checkState()
        )
        articles_inf.inverter_type.P_discharge_max = (
            window.ui.P_discharge_max_sbox.value()
        )
        articles_inf.inverter_type.P_charge_max = window.ui.P_charge_max_sbox.value()
        articles_inf.inverter_type.U_bat_min = window.ui.U_bat_min_sbox.value()
        articles_inf.inverter_type.U_bat_max = window.ui.U_bat_max_sbox.value()
        articles_inf.inverter_type.I_bat_discharge = (
            window.ui.I_bat_discharge_sbox.value()
        )
        articles_inf.inverter_type.I_bat_charge = window.ui.I_bat_charge_sbox.value()
        articles_inf.inverter_type.bat_type = get_enum_value(
            BatTypeEnum, window.ui.bat_type_cobox.currentText()
        )
        articles_inf.inverter_type.bat_count = window.ui.bat_count_sbox.value()
        articles_inf.inverter_type.I_backup = window.ui.I_backup_sbox.value()

        # User ID setzen, falls neu
        if not articles_inf_old:
            articles_inf.user_id = window.session_user_id

        # Änderungen speichern
        sess.commit()
        window.mainwindow.on_menu_articles_btn_click()  # Aktualisiere die Hauptansicht

    except Exception as e:
        sess.rollback()  # Rollback bei einem Fehler
        print(f"Error occurred: {e}")

    finally:
        sess.close()  # Sitzung schließen
