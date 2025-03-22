from enum import Enum

from dlake.base.util.str import StrUtil


class USType(str,Enum):
    DECRYPTION = 'DECRYPTION'
    ENCRYPTION = 'ENCRYPTION'
    INGESTION = 'INGESTION'
    SOURCING = 'SOURCING'
    LANDING = 'LANDING'
    WAREHOUSING = 'WAREHOUSING'

    @staticmethod
    def valueOf(s: str):
        try:
            return USType[StrUtil.upper(s)]
        except:
            return None