from datetime import datetime

from dlake.base.config import Constants
from dlake.base.type.env import ENV
from dlake.base.type.spark import SparkEnv
from dlake.base.type.usecase import USType
from dlake.base.util.common import Utils
from dlake.base.util.data import DataUtil
from dlake.base.util.date import DateUtil
from dlake.base.util.logger import Logger

LOGGER = Logger.get_logger("JobSession")


class JobSession():
    run_id: str
    name: str
    type: USType
    run_time: datetime
    completed_time: datetime
    env: ENV
    warehouse_path: str
    responses: list

    def __init__(self, env: ENV = ENV.DEV, args_option: list = None):
        self.env = env
        args = self.get_args(env, args_option)
        self.run_time = DateUtil.now()
        self.name = DataUtil.get_dict_value(args, "JOB_NAME")
        self.run_id = DataUtil.get_dict_value(args, "JOB_RUN_ID")
        self.type = USType.valueOf(DataUtil.get_dict_value(args, "JOB_TYPE"))
        self.responses = []

    def get_args(self, env: ENV, args_option: list = None):
        spark_env = Utils.get_spark_env(env=env)
        LOGGER.debug("[get_args] SPARK ENV = %s", spark_env)
        match spark_env:
            case SparkEnv.GLUE:
                from awsglue.utils import getResolvedOptions
                import sys
                if args_option:
                    args = getResolvedOptions(sys.argv, args_option)
                else:
                    args = getResolvedOptions(sys.argv, Constants.JOB_DEFAULT_PARAMS)
                return args
            case SparkEnv.LOCAL:
                return {'JOB_NAME': 'demo', 'JOB_RUN_ID': 'xyz', 'JOB_TYPE': 'INGESTION'}
            case _:
                raise Exception("[get_args] Don't spark_env=%s env=%s", spark_env, env)
