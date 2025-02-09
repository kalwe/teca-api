from enum import Enum


class GenderEnum(str, Enum):

  PRIMARY = 'Ensino Fundamental',
  SECONDARY = 'Ensino Médio',
  TERTIARY = 'Ensino Superior',
