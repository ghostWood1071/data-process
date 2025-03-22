from enum import Enum

from dlake.base.util.str import StrUtil


class ENV(Enum):
    DEV = 'Develop Environment'
    SIT = 'System Integration Test Environment'
    UAT = 'User Acceptance Test Environment'
    PROD = 'Production Environment'

    @staticmethod
    def valueOf(s: str):
        try:
            return ENV[StrUtil.upper(s)]
        except:
            return None