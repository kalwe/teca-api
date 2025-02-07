from enum import Enum


class MaritalStatusEnum(str, Enum):
    SINGLE = 'Solteiro'
    MARRIED = 'Casado'
    DIVORCED = 'Divorciado'
    LIVING_TOGETHER = "Amasiado/Concubinado"
    STABLE_UNION = "União Estável"
    WIDOWER = "Viúvo"
