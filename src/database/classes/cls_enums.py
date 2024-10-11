import enum


class CellMatEnum(enum.Enum):
    EMPTY = ""
    POLY_MAT = "polykristallin"
    MONO_MAT = "monokristallin"
    AMORPH_MAT = "amorph"


class PhasesEnum(enum.Enum):
    EMPTY = ""
    SINGLE_PHASE = "einphasig"
    THREE_PHASE = "dreiphasig"


class InvClassesEnum(enum.Enum):
    EMPTY = ""
    STRING_INV = "String-Wechselrichter"
    HYBRID_INV = "Hybrid-Wechselrichter"
    BAT_INV = "Batterie-Wechselrichter"
    CENTRAL_INV = "Zentral-Wechselrichter"


class CommInterfaceEnum(enum.Enum):
    EMPTY = ""
    RS_485_1 = "RS485 via DM-485CB-10"
    RS_485_2 = "RS485 via 485PB-NR"
    SPEEDWIRE_1 = "Webconnect via WLAN/WIFI"
    SPEEDWIRE_2 = "Webconnect via LAN"
    SPEEDWIRE_3 = "Webconnect via SWDM-10"
    BT_PB = "Bluetooth Piggy-Back - BTBINV-NR"


class BatTypeEnum(enum.Enum):
    EMPTY = ""
    BAD_TYPE_1 = "Lithium-Ionen-Batterie"


def get_enum_value(enum_class, ui_value: str):
    """converts ui_value to enum value"""
    for member in enum_class:
        if member.value == ui_value:
            return member
    return enum_class.EMPTY  # Fallback if enum value cannot be converted
