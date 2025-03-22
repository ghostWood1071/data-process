from enum import Enum

from dlake.base.util.str import StrUtil


class ExtractType(Enum):
    FULL_LOAD = 'FULL_LOAD'
    INCREMENTAL = 'INCREMENTAL'
    DAILY = 'DAILY'
    MONTHLY = 'MONTHLY'
    WEEKLY = 'WEEKLY'
    YEARLY = 'YEARLY'
    DATE_RANGE = 'DATE_RANGE'

    @staticmethod
    def valueOf(s: str):
        try:
            return ExtractType[StrUtil.upper(s)]
        except:
            return None
