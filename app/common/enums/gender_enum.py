from enum import Enum


class GenderEnum(str, Enum):
    male = 'Masculino'
    female = 'Feminino'
    other = 'Outro'
    not_given = 'Não informado'
