from enum import Enum

from dlake.base.util.str import StrUtil


class MetaType(Enum):
    LOCAL = 1
    ICEBERG = 2
    DYNAMODB = 3

    @staticmethod
    def valueOf(s: str):
        try:
            return MetaType[StrUtil.upper(s)]
        except:
            return None