from ast import Try
from typing import List, Optional

import pandas as pd
from sqlalchemy import or_
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
from database.classes.cls_project_data import Addresses, Projects
from database.utils.u_db_sess import BASE, create_session
from ui.classes.dlg_address import AddressAttrDialog
from ui.classes.dlg_article import ArticleAttrDialog
from ui.classes.dlg_manufacturer import ManufacturerAttrDialog
from ui.classes.dlg_project import ProjectAttrDialog


def get_manufacturers_infos(
    manufacturer_id: Optional[int] = None,
    manufacturer_search_string: str = None,
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

        if manufacturer_search_string:
            query = query.filter(
                Manufacturers.mf_name.ilike(f"{manufacturer_search_string}")
                .order_by(Manufacturers.mf_name)
                .limit(5)
            )

        manfac_infos: List[Manufacturers] = query.all()
        return manfac_infos
    except Exception as e:
        sess.rollback()
        print(f"Error occurred: {e}")
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

    except Exception as e:
        sess.rollback()  # Rollback bei einem Fehler
        print(f"Error occurred: {e}")

    finally:
        # Sitzung schließen
        sess.close()


def get_articles_infos(
    article_id: Optional[int] = None,
    article_no: Optional[int] = None,
    article_name: Optional[str] = None,
) -> List[Articles]:
    r"""
    Retrieves article information from the database based on the given criteria.
    Filters by article ID, article number, or article name, applying the filters
    in the specified priority order: article_id > article_no > article_name.

    :param article_id: The ID of the article whose information should be retrieved.
    :type article_id: Optional[int]
    :param article_no: The article number to filter by, if provided.
    :type article_no: Optional[int]
    :param article_name: The article name or part of it to filter by, case insensitive.
    :type article_name: Optional[str]
    :return: A list of `Articles` objects containing the requested article information.
    :rtype: List[Articles]
    """

    # Create a new database session
    sess: sessionmaker = create_session()
    try:
        # Begin the query, loading related data for better performance with joinedload
        query = sess.query(Articles).options(
            joinedload(Articles.article_types),
            joinedload(Articles.module_type),
            joinedload(Articles.inverter_type),
            joinedload(Articles.manufacturer),
        )

        # Apply filters based on provided parameters
        if article_id is not None:
            query = query.filter(Articles.id == article_id)
        else:
            conditions: List = []
            if article_no is not None:
                conditions.append(Articles.article_no == article_no)
            if article_name is not None:
                conditions.append(Articles.article_name.ilike(f"%{article_name}%"))
            # Apply the OR condition if there are any filters
            if conditions:
                query = query.filter(or_(*conditions))

        # Execute the query and retrieve results
        article_infos: List[Articles] = query.all()
        return article_infos
    except Exception as e:
        sess.rollback()
        print(f"Error occurred: {e}")

    finally:
        # Close the session to avoid resource leaks
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

    except Exception as e:
        sess.rollback()
        print(f"Error occurred: {e}")

    finally:
        sess.close()


def import_articles_from_df(self, df: pd.DataFrame = None):  # type: ignore
    """
    Imports articles from a DataFrame and adds them to the database or updates them if they already exist.

    Parameters:
    self: The window from which the user session ID and UI information is retrieved.
    df (pd.DataFrame): DataFrame containing articles data with columns 'Artikelnummer', 'Artikelname', and 'Hersteller'.
    """

    # Create a new database session
    sess: sessionmaker = create_session()
    try:
        # Pre-fetch all manufacturers and store in a dictionary for quick access
        mf_infos = get_manufacturers_infos()
        manufacturers_dict = {m.mf_name: m for m in mf_infos}
        # Iterate over each row in the DataFrame
        for _, row in df.iterrows():
            article_no = row["Artikelnummer"]
            article_name = row["Artikelname"]
            mf_name = row["Hersteller"]
            try:
                # Check if the article already exists in the database
                existing_articles: List[Articles] = get_articles_infos(
                    article_name=article_name, article_no=article_no
                )
                article = (
                    existing_articles[0] if existing_articles else Articles()
                )  # Use first result or create a new article

                # Update article attributes
                article.is_enabled = True
                article.article_name = article_name
                article.article_no = article_no

                article = sess.merge(article)

                # Assign manufacturer (use dictionary for faster lookup)
                if mf_name not in manufacturers_dict:
                    new_manufacturer = Manufacturers(
                        mf_name=mf_name, user_id=self.session_user_id
                    )
                    sess.add(new_manufacturer)
                    article.manufacturer = new_manufacturer
                    manufacturers_dict[mf_name] = new_manufacturer
                else:
                    article.manufacturer = sess.merge(manufacturers_dict[mf_name])

                # Optionally set article types based on checkboxes in the UI
                # Uncomment if these types are needed
                # if not article.article_types:
                #     article.article_types = ArticleTypes()
                # article.article_types.is_battery = bool(window.ui.is_battery_cbox.checkState())
                # article.article_types.is_com_product = bool(window.ui.is_com_product_cbox.checkState())
                # article.article_types.is_module = bool(window.ui.is_module_cbox.checkState())
                # article.article_types.is_chg_point = bool(window.ui.is_chg_point_cbox.checkState())
                # article.article_types.is_misc = bool(window.ui.is_misc_cbox.checkState())
                # article.article_types.is_inverter = bool(window.ui.is_inv_cbox.checkState())

                # Set user ID if it's a new article
                if not existing_articles:
                    article.user_id = self.session_user_id
                # Commit changes to database
                sess.commit()

            except Exception as e:
                sess.rollback()  # Roll back any changes if an error occurs
                print(f"Error occurred while processing article {article_name}: {e}")

        # Refresh UI after changes
        self.on_menu_articles_btn_click()
    finally:
        # Close the session after all rows are processed
        sess.close()


def get_project_s_infos(projects_id: Optional[int] = None) -> List[Projects]:
    """
    Retrieves all projects from the database or a specific project by its ID.

    Parameters:
    projects_id (int): ID of the project to retrieve.

    Returns:
    List[Projects]: List of projects matching the query criteria.
    """
    sess: sessionmaker = create_session()
    try:
        query = sess.query(Projects).options(
            joinedload(Projects.sub_systems),
            joinedload(Projects.user),
            joinedload(Projects.loc_address),
            joinedload(Projects.customer_address),
        )
        if projects_id is not None:
            query = query.filter(Projects.id == projects_id)

        projects_infos: List[Projects] = query.all()
        return projects_infos
    except Exception as e:
        sess.rollback()
        print(f"Error occurred: {e}")
    finally:
        sess.close()


def refresh_project_inf(window: ProjectAttrDialog):
    """
    Updates the project attributes in the UI based on the provided project information.

    Parameters:
    window (ProjectAttrDialog): The window containing the UI elements.
    project_inf (Projects): The project information to be displayed.

    Returns:
    None
    """

    sess: sessionmaker = create_session()
    try:
        # Load existing project or create a new one
        if window.project_id:
            project_inf = get_project_s_infos(projects_id=window.project_id)[0]
            project_inf = sess.merge(project_inf)
        else:
            project_inf = Projects()
            sess.add(project_inf)

        project_inf.user_id = window.session_user_id
        project_inf.project_no = window.ui.project_no_txt.text()
        project_inf.project_name = window.ui.project_name_txt.text()
        project_inf.sys_perf = window.ui.sys_perf_txt.text()
        project_inf.comission_date = window.ui.comission_date_txt.text()
        # project_inf.customer_address = window.customer_address
        # project_inf.loc_address = window.loc_address

        sess.commit()
        window.project_id = project_inf.id

    except Exception as e:
        sess.rollback()
        print(f"Error occurred: {e}")
    finally:
        sess.close()


def get_address_s_infos(**kwargs) -> List[Addresses]:
    """
    Retrieves all addresses from the database or a specific address by its ID.

    Parameters:
    address_id (int): ID of the address to retrieve.

    Returns:
    List[Addresses]: List of addresses matching the query criteria.
    """

    sess: sessionmaker = create_session()
    try:
        query = sess.query(Addresses)
        if "address_id" in kwargs:
            address_id = kwargs.get("address_id")
            if address_id is None:
                return []
            else:
                query = query.filter(Addresses.id == address_id)

        addresses_infos: List[Addresses] = query.all()
        return addresses_infos if addresses_infos else []
    except Exception as e:
        sess.rollback()
        print(f"Error occurred: {e}")
    finally:
        sess.close()


def refresh_address_inf(window: AddressAttrDialog = None):
    """
    Updates the address attributes in the UI based on the provided address information.
    Parameters:
    window (AdressAttrDialog): The window containing the UI elements.
    address_inf (Addresses): The address information to be displayed.
    Returns:
    None
    """

    sess: sessionmaker = create_session()
    try:

        # Load existing project or create a new one
        if window.address_id is None:
            address_inf = Addresses()
            sess.add(address_inf)
        else:
            address_inf = get_address_s_infos(address_id=window.address_id)[0]
            address_inf = sess.merge(address_inf)

        address_inf.address_line1 = window.ui.address_line_1_txt.text()
        address_inf.address_line2 = window.ui.address_line_2_txt.text()
        address_inf.city = window.ui.city_txt.text()
        address_inf.postal_code = window.ui.postal_code_txt.text()
        address_inf.state = window.ui.state_txt.text()
        address_inf.country = window.ui.country_txt.text()

        if window.mode in ["customer_address", "loc_address"]:
            project_infos = get_project_s_infos(window.parent.project_id)

            if not project_infos:
                raise ValueError(f"No project found with ID {window.parent.project_id}")
            project_inf = sess.merge(project_infos[0])

            if window.mode == "customer_address":
                project_inf.customer_address = sess.merge(address_inf)
            elif window.mode == "loc_address":
                project_inf.loc_address = sess.merge(address_inf)

        sess.commit()
        window.address_id = address_inf.id

    except Exception as e:
        sess.rollback()
        print(f"Error occurred: {e}")
    finally:
        sess.close()
