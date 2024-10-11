import enum
from typing import Dict, List

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QDialog

from database.classes.cls_enums import (
    BatTypeEnum,
    CellMatEnum,
    CommInterfaceEnum,
    InvClassesEnum,
    PhasesEnum,
)
from database.classes.cls_user_role_system import Users
from database.utils.u_db_sess import BASE
from styles.styles_Handler import initialize_ui_style
from ui.forms.articleattrform import Ui_ArticleAttrDialog
from ui.forms.manfacattrform import Ui_ManFacAttrDialog
from ui.forms.usrattrform import Ui_UsrAttrDialog


class UserAttrDialog(QDialog):

    def __init__(self, usr_inf: type(BASE) = None, parent=None):  # type: ignore
        super().__init__(parent)

        self.ui = Ui_UsrAttrDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Benutzerinformation")
        self.setFixedSize(500, 550)
        self.mainwindow = parent

        self.ui.is_enabled_cbox.setCheckState(
            Qt.Checked if usr_inf.is_enabled else Qt.Unchecked
        )
        self.ui.usrname_txt.setText(usr_inf.username)
        self.ui.name_txt.setText(usr_inf.user_profile.name)
        self.ui.family_name_txt.setText(usr_inf.user_profile.family_name)

        self.set_roles_combo_box(usr_inf)

        self.ui.buttonBox.accepted.connect(
            lambda u=usr_inf: self.on_accept_btn_click(usr_inf=u)
        )
        initialize_ui_style(self)

    def set_roles_combo_box(self, usr_inf):
        from database.queries.q_role_system import get_all_roles

        for role in get_all_roles():
            self.ui.roles_comboBox.addItem(role.role_name)
        usr_role: str = usr_inf.roles[0].role_name
        index = self.ui.roles_comboBox.findText(usr_role)
        if index >= 0:
            self.ui.roles_comboBox.setCurrentIndex(index)

    def on_accept_btn_click(self, usr_inf: type(BASE)):  # type: ignore
        from database.queries.q_users import refresh_usr_inf

        refresh_usr_inf(window=self, usr_inf=usr_inf)

        self.accept()


class ManufacturerAttrDialog(QDialog):

    def __init__(self, session_user_id: int = None, mf_inf: type(BASE) = None, parent=None):  # type: ignore
        super().__init__(parent)

        self.ui = Ui_ManFacAttrDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Herstellerinformation")
        self.setFixedSize(650, 600)
        self.mainwindow = parent
        self.session_user_id: int = session_user_id

        if mf_inf:
            self.ui.is_enabled_cbox.setCheckState(
                Qt.Checked if mf_inf.is_enabled else Qt.Unchecked
            )
            self.ui.manufacturer_name_txt.setText(mf_inf.mf_name)
            if mf_inf.address:
                self.ui.address_line_1_txt.setText(mf_inf.address.address_line1)
                self.ui.address_line_2_txt.setText(mf_inf.address.address_line2)
                self.ui.city_txt.setText(mf_inf.address.city)
                self.ui.postal_code_txt.setText(mf_inf.address.postal_code)
                self.ui.state_txt.setText(mf_inf.address.state)
                self.ui.country_txt.setText(mf_inf.address.country)

            if mf_inf.specialized_fields:
                self.ui.produces_modules_cbox.setCheckState(
                    Qt.Checked
                    if mf_inf.specialized_fields.produces_modules
                    else Qt.Unchecked
                )
                self.ui.produces_inverters_cbox.setCheckState(
                    Qt.Checked
                    if mf_inf.specialized_fields.produces_inverters
                    else Qt.Unchecked
                )
                self.ui.produces_batteries_cbox.setCheckState(
                    Qt.Checked
                    if mf_inf.specialized_fields.produces_batteries
                    else Qt.Unchecked
                )
                self.ui.produces_chg_points_cbox.setCheckState(
                    Qt.Checked
                    if mf_inf.specialized_fields.produces_chg_points
                    else Qt.Unchecked
                )
                self.ui.produces_com_cbox.setCheckState(
                    Qt.Checked
                    if mf_inf.specialized_fields.produces_com_products
                    else Qt.Unchecked
                )
                self.ui.produces_misc_cbox.setCheckState(
                    Qt.Checked
                    if mf_inf.specialized_fields.produces_misc
                    else Qt.Unchecked
                )

        self.ui.buttonBox.accepted.connect(
            lambda mf=mf_inf: self.on_accept_btn_click(mf_inf=mf)
        )
        initialize_ui_style(self)

    def on_accept_btn_click(self, mf_inf: type(BASE)):  # type: ignore
        from database.queries.q_ref_data import refresh_mf_inf

        refresh_mf_inf(window=self, mf_inf=mf_inf)

        self.accept()


class ArticleAttrDialog(QDialog):

    def __init__(self, session_user_id: int = None, article_infs: type(BASE) = None, parent=None):  # type: ignore
        super().__init__(parent)

        self.ui = Ui_ArticleAttrDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Artikelinformation")
        self.setFixedSize(1500, 850)
        self.mainwindow = parent
        self.session_user_id: int = session_user_id
        self.combo_boxes_content: List[tuple[QComboBox, enum.Enum]] = [
            (self.ui.cell_mat_cobox, CellMatEnum),
            (self.ui.inv_type_cobox, InvClassesEnum),
            (self.ui.feed_phases_cobox, PhasesEnum),
            (self.ui.bat_type_cobox, BatTypeEnum),
        ]

        for combo_box in self.combo_boxes_content:
            self.set_combo_box(cobox=combo_box[0], enum_obj=combo_box[1])

        if article_infs:
            ############################### General Article Infos ###############################

            self.ui.is_enabled_cbox.setCheckState(
                Qt.Checked if article_infs.is_enabled else Qt.Unchecked
            )
            self.ui.article_name_txt.setText(article_infs.article_name)
            self.ui.article_no_txt.setText(article_infs.article_no)
            self.ui.manufacturer_name_txt.setText(article_infs.manufacturer.mf_name)

            ############################### Product Types ###############################
            self.ui.is_battery_cbox.setCheckState(
                Qt.Checked if article_infs.article_types.is_battery else Qt.Unchecked
            )
            self.ui.is_com_product_cbox.setCheckState(
                Qt.Checked
                if article_infs.article_types.is_com_product
                else Qt.Unchecked
            )
            self.ui.is_module_cbox.setCheckState(
                Qt.Checked if article_infs.article_types.is_module else Qt.Unchecked
            )
            self.ui.is_chg_point_cbox.setCheckState(
                Qt.Checked if article_infs.article_types.is_chg_point else Qt.Unchecked
            )
            self.ui.is_misc_cbox.setCheckState(
                Qt.Checked if article_infs.article_types.is_misc else Qt.Unchecked
            )
            self.ui.is_inv_cbox.setCheckState(
                Qt.Checked if article_infs.article_types.is_inverter else Qt.Unchecked
            )

            ############################### Module Properties ###############################
            if article_infs.module_type:
                self.ui.has_frame_cbox.setCheckState(
                    Qt.Checked if article_infs.module_type.has_frame else Qt.Unchecked
                )
                article_infs.module_type.cell_material

                self.set_combo_box(
                    cobox=self.ui.cell_mat_cobox,
                    Enum_element=article_infs.module_type.cell_material,
                    enum_obj=CellMatEnum,
                )
                self.ui.description_txt.setText(article_infs.module_type.description)

                self.ui.module_length_sbox.setValue(article_infs.module_type.length)
                self.ui.module_width_sbox.setValue(article_infs.module_type.width)
                self.ui.module_height_sbox.setValue(article_infs.module_type.height)
                self.ui.module_weight_sbox.setValue(article_infs.module_type.weight)
                self.ui.P_MPP_sbox.setValue(article_infs.module_type.P_MPP)
                self.ui.U_MPP_sbox.setValue(article_infs.module_type.U_MPP)
                self.ui.I_MPP_sbox.setValue(article_infs.module_type.I_MPP)
                self.ui.U_OC_sbox.setValue(article_infs.module_type.U_oc)
                self.ui.I_SC_sbox.setValue(article_infs.module_type.I_sc)
                self.ui.mue_sbox.setValue(article_infs.module_type.mue)
                self.ui.alpha_sbox.setValue(article_infs.module_type.alpha)
                self.ui.beta_sbox.setValue(article_infs.module_type.beta)
                self.ui.gamma_sbox.setValue(article_infs.module_type.gamma)
                self.ui.NOCT_sbox.setValue(article_infs.module_type.NOCT)

            ############################### Inverter Properties ###############################
            if article_infs.inverter_type:
                self.ui.inv_description_txt.setText(
                    article_infs.inverter_type.description
                )

                # Set the Inverter Class ComboBox
                self.set_combo_box(
                    cobox=self.ui.inv_type_cobox,
                    Enum_element=article_infs.inverter_type.InvClass,
                    enum_obj=InvClassesEnum,
                )

                # Physical Dimensions
                self.ui.inv_length_sbox.setValue(article_infs.inverter_type.length)
                self.ui.inv_width_sbox.setValue(article_infs.inverter_type.width)
                self.ui.inv_height_sbox.setValue(article_infs.inverter_type.height)
                self.ui.inv_weight_sbox.setValue(article_infs.inverter_type.weight)

                # Ambient Conditions
                self.ui.T_ambient_min_sbox.setValue(
                    article_infs.inverter_type.T_ambient_min
                )
                self.ui.T_ambient_max_sbox.setValue(
                    article_infs.inverter_type.T_ambient_max
                )

                # DC Input Data
                self.ui.P_dc_max_sbox.setValue(article_infs.inverter_type.P_dc_max)
                self.ui.U_dc_min_sbox.setValue(article_infs.inverter_type.U_dc_min)
                self.ui.U_dc_max_sbox.setValue(article_infs.inverter_type.U_dc_max)
                self.ui.U_MPP_min_sbox.setValue(article_infs.inverter_type.U_mpp_min)
                self.ui.U_MPP_max_sbox.setValue(article_infs.inverter_type.U_mpp_max)
                self.ui.U_dc_nom_sbox.setValue(article_infs.inverter_type.U_dc_nom)
                self.ui.U_start_sbox.setValue(article_infs.inverter_type.U_start)
                # self.ui.mpp_trackers_sbox.setValue(
                #     article_inf.inverter_type.mpp_trackers
                # )

                # AC Output Data
                self.ui.P_ac_nom_sbox.setValue(article_infs.inverter_type.P_ac_nom)
                self.ui.S_ac_max_sbox.setValue(article_infs.inverter_type.S_ac_max)
                self.ui.U_ac_min_sbox.setValue(article_infs.inverter_type.U_ac_min)
                self.ui.U_ac_max_sbox.setValue(article_infs.inverter_type.U_ac_max)
                self.ui.f_ac_nom_sbox.setValue(article_infs.inverter_type.f_ac_nom)
                self.ui.U_ac_nom_sbox.setValue(article_infs.inverter_type.U_ac_nom)
                self.ui.I_ac_max_sbox.setValue(article_infs.inverter_type.I_ac_max)
                self.ui.cos_phi_sbox.setValue(article_infs.inverter_type.cos_phi)

                # Set the Feed Phases ComboBox
                self.set_combo_box(
                    cobox=self.ui.feed_phases_cobox,
                    Enum_element=article_infs.inverter_type.feed_phases,
                    enum_obj=PhasesEnum,
                )

                self.ui.inv_mue_sbox.setValue(article_infs.inverter_type.mue)
                self.ui.self_consumption_sbox.setValue(
                    article_infs.inverter_type.self_consumption
                )
                self.ui.has_trafo_cbox.setCheckState(
                    Qt.Checked if article_infs.inverter_type.has_trafo else Qt.Unchecked
                )

                # Battery Inverter Attributes
                self.ui.P_discharge_max_sbox.setValue(
                    article_infs.inverter_type.P_discharge_max
                )
                self.ui.P_charge_max_sbox.setValue(
                    article_infs.inverter_type.P_charge_max
                )
                self.ui.U_bat_min_sbox.setValue(article_infs.inverter_type.U_bat_min)
                self.ui.U_bat_max_sbox.setValue(article_infs.inverter_type.U_bat_max)
                self.ui.I_bat_discharge_sbox.setValue(
                    article_infs.inverter_type.I_bat_discharge
                )
                self.ui.I_bat_charge_sbox.setValue(
                    article_infs.inverter_type.I_bat_charge
                )

                self.set_combo_box(
                    cobox=self.ui.bat_type_cobox,
                    Enum_element=article_infs.inverter_type.bat_type,
                    enum_obj=BatTypeEnum,
                )

                self.ui.bat_count_sbox.setValue(article_infs.inverter_type.bat_count)
                self.ui.I_backup_sbox.setValue(article_infs.inverter_type.I_backup)

                # Set the Communication Interface ComboBox
                # self.set_combo_box(
                #     cobox=self.ui.com_interface_cobox,
                #     value=article_inf.inverter_type.com_interface.value,
                #     enum_obj=CommInterfaceEnum,
                # )

        self.ui.buttonBox.accepted.connect(
            lambda article=article_infs: self.on_accept_btn_click(article_inf=article)
        )
        initialize_ui_style(self)

    def set_combo_box(
        self,
        cobox: QComboBox,
        Enum_element: Dict = None,
        enum_obj: enum.Enum = None,
    ) -> None:
        cobox.clear()
        enum_values = [member.value for member in enum_obj]
        cobox.addItems(enum_values)
        if Enum_element is None:
            return
        if Enum_element.value and Enum_element.value in enum_values:
            cobox.setCurrentText(Enum_element.value)
        else:
            cobox.setCurrentIndex(-1)

    def on_accept_btn_click(self, article_inf: type(BASE)):  # type: ignore
        from database.queries.q_ref_data import refresh_article_inf

        refresh_article_inf(window=self, articles_inf=article_inf)

        self.accept()
