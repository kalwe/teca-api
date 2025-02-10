from enum import Enum


class ScholarityEnum(str, Enum):
    PRIMARY = 'Ensino Fundamental'
    SECONDARY = 'Ensino Médio'
    TERTIARY = 'Ensino Superior'
