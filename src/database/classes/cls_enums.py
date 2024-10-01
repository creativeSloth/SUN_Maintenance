import enum


class CellMatEnum(enum.Enum):
    POLY_MAT = "polykristallin"
    MONO_MAT = "monokristallin"
    AMORPH_MAT = "monokristallin"


class PhasesEnum(enum.Enum):
    SINGLE_PHASE = "einphasig"
    THREE_PHASE = "dreiphasig"


class InvClassesEnum(enum.Enum):
    STRING_INV = "String_Wechselrichter"
    HYBRID_INV = "Hybrid-Wechselrichter"
    BAT_INV = "Batterie-Wechselrichter"
    CENTRAL_INV = "Central-Wechselrichter"


class CommInterfaceEnum(enum.Enum):
    RS_485_1 = "RS485 via DM-485CB-10"
    RS_485_2 = "RS485 via 485PB-NR"
    SPEEDWIRE_1 = "Webconnect via WLAN/WIFI"
    SPEEDWIRE_2 = "Webconnect via LAN"
    SPEEDWIRE_3 = "Webconnect via SWDM-10"
    BT_PB = "Bluetooth Piggy-Back - BTBINV-NR"
