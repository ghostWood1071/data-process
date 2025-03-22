from enum import Enum

from dlake.base.util.str import StrUtil


class LoadType(Enum):
    OVERWRITE = 'OVERWRITE'
    APPEND = 'APPEND'
    PARTITION_OVERWRITE = 'PARTITION_OVERWRITE'

    @staticmethod
    def valueOf(s: str):
        try:
            return LoadType[StrUtil.upper(s)]
        except:
            return None
