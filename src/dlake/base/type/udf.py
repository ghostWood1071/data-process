from enum import Enum

from dlake.base.util.str import StrUtil


class UDF(Enum):
    FAKE_DATA = 'Fake data'
    MASKING = 'Masking sensitive value'
    REPLACE = 'Replace data'
    HASHING = 'Hashing sensitive value'
    ADD_FILE_PATH = 'Add Input File Path'
    REGEX_IN_COL = 'Regex String In Column'
    STR_PTIME = 'Convert String to Datetime by Format'
    DROP_COL = 'Convert String to Datetime by Format'
    DROP_COLS = 'Convert String to Datetime by Format'
    ADD_COL = 'Convert String to Datetime by Format'

    @staticmethod
    def valueof(name: str):
        try:
            return UDF[StrUtil.upper(name)]
        except:
            return None


class UDFParam:
    ARGS = 'ARGS'
    TYPE = 'TYPE'
    COLS = 'COLS'
    COL = 'COL'
    INDEX = 'INDEX'

