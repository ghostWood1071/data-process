from dlake.base.type.env import ENV
from dlake.base.type.spark import SparkEnv
from dlake.base.util.common import Utils


class ISpark:
    def __init__(self, job_name):
        self.job_name = job_name
        self.config = None
        self.spark = None
        self.args = {}

    def init_session(self):
        pass

    def close_session(self):
        pass

    @staticmethod
    def init(env: ENV, job_name: str):
        match Utils.get_spark_env(env):
            case SparkEnv.LOCAL:
                from dlake.base.component.spark.spark_local import SparkLocal
                return SparkLocal(job_name)
            case SparkEnv.GLUE:
                from dlake.base.component.spark.spark_glue import SparkGlue
                return SparkGlue(job_name)
            case _:
                return ISpark(job_name)
