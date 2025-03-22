from enum import Enum

from dlake.base.util.str import StrUtil


class CryptType(Enum):
    GPG = 'GPG'
    AES = 'AES'
    RSA = 'RSA'

    @staticmethod
    def valueOf(s: str):
        try:
            return CryptType[StrUtil.upper(s)]
        except:
            return None