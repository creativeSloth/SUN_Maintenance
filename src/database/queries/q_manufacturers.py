from typing import List, Optional

from sqlalchemy.orm import joinedload, sessionmaker

from database.classes.cls_article_data import Manufacturers, SpecializedFields
from database.classes.cls_project_data import Addresses
from database.classes.cls_user_role_system import Users
from database.utils.u_db_sess import create_session
from ui.classes.dialog_forms import ManufacturerAttrDialog


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

        usrs_infos: List[Manufacturers] = query.all()
        return usrs_infos
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
