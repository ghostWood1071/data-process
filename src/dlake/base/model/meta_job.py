import json
from datetime import datetime

from dlake.base.type.usecase import USType
from dlake.base.util.json import JsonUtil
from dlake.base.util.logger import Logger

LOGGER = Logger.get_logger(__name__)

"""
    @Job Meta Data
"""


class MetaJob:
    id: int
    name: str
    flow_name: dict
    type: USType
    schedule: str
    trigger: str
    status: bool
    created_at: datetime
    updated_at: datetime

    def __init__(self, extract_data: dict = None):
        if extract_data is not None:
            extract_flat = JsonUtil.flatten_json(extract_data)
            for key, value in extract_flat.items():
                self.setattr(key, value)

    def setattr(self, key, value):
        try:
            match key:
                case 'type':
                    self.set_type(value)
                case _:
                    self.__setattr__(key, value)

        except Exception as ex:
            LOGGER.debug("[setattr] key=%s value=%s msg=%s", key, value, ex)

    def __str__(self):
        return json.dumps(self.__dict__)

    def set_type(self, type):
        self.type = USType.valueOf(type)
