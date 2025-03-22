from enum import Enum

from dlake.base.util.str import StrUtil


class TargetType(Enum):
    DATABASE = 'database'
    S3 = 'S3'
    ICEBERG = 'ICEBERG'

    @staticmethod
    def valueOf(s: str):
        try:
            return TargetType[StrUtil.upper(s)]
        except:
            return None

class TargetSubType(Enum):
    CSV = 'CSV'
    EXCEL = 'EXCEL'
    ORACLE = 'ORACLE'
    MSSQL = 'MSSQL'

    @staticmethod
    def valueOf(s: str):
        try:
            return TargetSubType[StrUtil.upper(s)]
        except:
            return None
