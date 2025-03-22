from enum import Enum

from dlake.base.util.str import StrUtil


class SourceType(Enum):
    DATABASE = 'database'
    S3 = 'S3'

    @staticmethod
    def valueOf(s: str):
        try:
            return SourceType[StrUtil.upper(s)]
        except:
            return None

class SourceSubType(Enum):
    CSV = 'CSV'
    EXCEL = 'EXCEL'
    ORACLE = 'ORACLE'
    MSSQL = 'MSSQL'

    @staticmethod
    def valueOf(s: str):
        try:
            return SourceSubType[StrUtil.upper(s)]
        except:
            return None
