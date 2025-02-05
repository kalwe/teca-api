from enum import Enum


class MaritalStatus(str, Enum):
    SINGLE = 'SINGLE'
    MARRIED = 'MARRIED'
    DIVORCED = 'DIVORCED'
