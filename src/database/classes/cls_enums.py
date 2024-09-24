import enum


class CellMatEnum(enum.Enum):
    POLY_MAT = "polykristallin"
    MONO_MAT = "monokristallin"
    AMORPH_MAT = "monokristallin"


class PhasesEnum(enum.Enum):
    SINGLE_PHASE = "einphasig"
    THREE_PHASE = "dreiphasig"
