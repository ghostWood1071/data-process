from enum import Enum
from dlake.base.util.str import StrUtil

class KeyType(Enum):
    PRIVATE_KEY = 'PrivateKey'
    PUBLIC_KEY = 'PublicKey'
    PASSPHRASE = 'Passphrase'

    @staticmethod
    def valueOf(s: str):
        try:
            return KeyType[StrUtil.upper(s)]
        except:
            return None