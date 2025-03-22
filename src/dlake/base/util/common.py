from dlake.base.config import Constants
from dlake.base.type.env import ENV
from dlake.base.type.spark import SparkEnv


class Utils:

    @staticmethod
    def get_spark_env(env: ENV):
        spark_env = Constants.SPARK_ENV
        if env == ENV.DEV:
            spark_env = SparkEnv.LOCAL
        return spark_env