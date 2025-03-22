from enum import Enum

from dlake.base.util.str import StrUtil


class CompressType(Enum):
    ZIP = 'zip'

    @staticmethod
    def valueOf(s: str):
        try:
            return CompressType[StrUtil.upper(s)]
        except:
            return None