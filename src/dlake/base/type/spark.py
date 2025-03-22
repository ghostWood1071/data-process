from enum import Enum

from dlake.base.util.str import StrUtil


class SparkEnv(Enum):
    LOCAL = 'Local'
    GLUE = 'AWS Glue'
    PROTO = 'Databricks Proton'

    @staticmethod
    def valueOf(s: str):
        try:
            return SparkEnv[StrUtil.upper(s)]
        except:
            return None