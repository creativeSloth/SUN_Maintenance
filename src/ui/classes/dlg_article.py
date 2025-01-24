import enum
from typing import Dict, List

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCompleter, QDialog

from database.classes.cls_enums import (
    BatTypeEnum,
    CellMatEnum,
    InvClassesEnum,
    PhasesEnum,
)
from database.utils.u_db_sess import BASE
from styles.styles_Handler import initialize_ui_style
from ui.forms.articleattrform import Ui_ArticleAttrDialog


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
                Qt.Checked
                if getattr(article_infs, "is_enabled", False)
                else Qt.Unchecked
            )
            self.ui.article_name_txt.setText(getattr(article_infs, "article_name", ""))
            self.ui.article_no_txt.setText(getattr(article_infs, "article_no", ""))
            self.ui.manufacturer_name_txt.setText(
                getattr(getattr(article_infs, "manufacturer", None), "mf_name", "")
            )

            ############################### Product Types ###############################
            article_types = getattr(article_infs, "article_types", None)
            if article_types:
                self.ui.is_battery_cbox.setCheckState(
                    Qt.Checked if article_types.is_battery else Qt.Unchecked
                )
                self.ui.is_com_product_cbox.setCheckState(
                    Qt.Checked if article_types.is_com_product else Qt.Unchecked
                )
                self.ui.is_module_cbox.setCheckState(
                    Qt.Checked if article_types.is_module else Qt.Unchecked
                )
                self.ui.is_chg_point_cbox.setCheckState(
                    Qt.Checked if article_types.is_chg_point else Qt.Unchecked
                )
                self.ui.is_misc_cbox.setCheckState(
                    Qt.Checked if article_types.is_misc else Qt.Unchecked
                )
                self.ui.is_inv_cbox.setCheckState(
                    Qt.Checked if article_types.is_inverter else Qt.Unchecked
                )

            ############################### Module Properties ###############################
            module_type = getattr(article_infs, "module_type", None)
            if module_type:
                self.ui.has_frame_cbox.setCheckState(
                    Qt.Checked if module_type.has_frame else Qt.Unchecked
                )
                self.set_combo_box(
                    cobox=self.ui.cell_mat_cobox,
                    Enum_element=getattr(module_type, "cell_material", None),
                    enum_obj=CellMatEnum,
                )
                self.ui.description_txt.setText(getattr(module_type, "description", ""))

                # Use getattr with default values
                self.ui.module_length_sbox.setValue(getattr(module_type, "length", 0))
                self.ui.module_width_sbox.setValue(getattr(module_type, "width", 0))
                self.ui.module_height_sbox.setValue(getattr(module_type, "height", 0))
                self.ui.module_weight_sbox.setValue(getattr(module_type, "weight", 0))
                self.ui.P_MPP_sbox.setValue(getattr(module_type, "P_MPP", 0))
                self.ui.U_MPP_sbox.setValue(getattr(module_type, "U_MPP", 0))
                self.ui.I_MPP_sbox.setValue(getattr(module_type, "I_MPP", 0))
                self.ui.U_OC_sbox.setValue(getattr(module_type, "U_oc", 0))
                self.ui.I_SC_sbox.setValue(getattr(module_type, "I_sc", 0))
                self.ui.mue_sbox.setValue(getattr(module_type, "mue", 0))
                self.ui.alpha_sbox.setValue(getattr(module_type, "alpha", 0))
                self.ui.beta_sbox.setValue(getattr(module_type, "beta", 0))
                self.ui.gamma_sbox.setValue(getattr(module_type, "gamma", 0))
                self.ui.NOCT_sbox.setValue(getattr(module_type, "NOCT", 0))

            ############################### Inverter Properties ###############################
            inverter_type = getattr(article_infs, "inverter_type", None)
            if inverter_type:
                self.ui.inv_description_txt.setText(
                    getattr(inverter_type, "description", "")
                )

                # Set the Inverter Class ComboBox
                self.set_combo_box(
                    cobox=self.ui.inv_type_cobox,
                    Enum_element=getattr(inverter_type, "InvClass", None),
                    enum_obj=InvClassesEnum,
                )

                # Physical Dimensions
                self.ui.inv_length_sbox.setValue(getattr(inverter_type, "length", 0))
                self.ui.inv_width_sbox.setValue(getattr(inverter_type, "width", 0))
                self.ui.inv_height_sbox.setValue(getattr(inverter_type, "height", 0))
                self.ui.inv_weight_sbox.setValue(getattr(inverter_type, "weight", 0))

                # Ambient Conditions
                self.ui.T_ambient_min_sbox.setValue(
                    getattr(inverter_type, "T_ambient_min", 0)
                )
                self.ui.T_ambient_max_sbox.setValue(
                    getattr(inverter_type, "T_ambient_max", 0)
                )

                # DC Input Data
                self.ui.P_dc_max_sbox.setValue(getattr(inverter_type, "P_dc_max", 0))
                self.ui.U_dc_min_sbox.setValue(getattr(inverter_type, "U_dc_min", 0))
                self.ui.U_dc_max_sbox.setValue(getattr(inverter_type, "U_dc_max", 0))
                self.ui.U_MPP_min_sbox.setValue(getattr(inverter_type, "U_mpp_min", 0))
                self.ui.U_MPP_max_sbox.setValue(getattr(inverter_type, "U_mpp_max", 0))
                self.ui.U_dc_nom_sbox.setValue(getattr(inverter_type, "U_dc_nom", 0))
                self.ui.U_start_sbox.setValue(getattr(inverter_type, "U_start", 0))

                # AC Output Data
                self.ui.P_ac_nom_sbox.setValue(getattr(inverter_type, "P_ac_nom", 0))
                self.ui.S_ac_max_sbox.setValue(getattr(inverter_type, "S_ac_max", 0))
                self.ui.U_ac_min_sbox.setValue(getattr(inverter_type, "U_ac_min", 0))
                self.ui.U_ac_max_sbox.setValue(getattr(inverter_type, "U_ac_max", 0))
                self.ui.f_ac_nom_sbox.setValue(getattr(inverter_type, "f_ac_nom", 0))
                self.ui.U_ac_nom_sbox.setValue(getattr(inverter_type, "U_ac_nom", 0))
                self.ui.I_ac_max_sbox.setValue(getattr(inverter_type, "I_ac_max", 0))
                self.ui.cos_phi_sbox.setValue(getattr(inverter_type, "cos_phi", 0))

                # Set the Feed Phases ComboBox
                self.set_combo_box(
                    cobox=self.ui.feed_phases_cobox,
                    Enum_element=getattr(inverter_type, "feed_phases", None),
                    enum_obj=PhasesEnum,
                )

                self.ui.inv_mue_sbox.setValue(getattr(inverter_type, "mue", 0))
                self.ui.self_consumption_sbox.setValue(
                    getattr(inverter_type, "self_consumption", 0)
                )
                self.ui.has_trafo_cbox.setCheckState(
                    Qt.Checked
                    if getattr(inverter_type, "has_trafo", False)
                    else Qt.Unchecked
                )

                # Battery Inverter Attributes
                self.ui.P_discharge_max_sbox.setValue(
                    getattr(inverter_type, "P_discharge_max", 0)
                )
                self.ui.P_charge_max_sbox.setValue(
                    getattr(inverter_type, "P_charge_max", 0)
                )
                self.ui.U_bat_min_sbox.setValue(getattr(inverter_type, "U_bat_min", 0))
                self.ui.U_bat_max_sbox.setValue(getattr(inverter_type, "U_bat_max", 0))
                self.ui.I_bat_discharge_sbox.setValue(
                    getattr(inverter_type, "I_bat_discharge", 0)
                )
                self.ui.I_bat_charge_sbox.setValue(
                    getattr(inverter_type, "I_bat_charge", 0)
                )

                self.set_combo_box(
                    cobox=self.ui.bat_type_cobox,
                    Enum_element=getattr(inverter_type, "bat_type", None),
                    enum_obj=BatTypeEnum,
                )

                self.ui.bat_count_sbox.setValue(getattr(inverter_type, "bat_count", 0))
                self.ui.I_backup_sbox.setValue(getattr(inverter_type, "I_backup", 0))

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
        self.set_completer()

    def set_completer(self) -> None:
        from database.queries.q_ref_data import get_manufacturers_infos

        mf_infos = get_manufacturers_infos()
        mf_names = [mf_info.mf_name for mf_info in mf_infos]
        mf_completer = QCompleter(mf_names)
        mf_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.manufacturer_name_txt.setCompleter(mf_completer)

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
        self.mainwindow.on_menu_articles_btn_click()

        self.accept()
