from dlake.base.model.meta_extract import ExtractMeta
from dlake.base.model.meta_load import LoadMeta
from dlake.base.model.meta_scenario import MetaScenario
from dlake.core.session.job import JobSession
from dlake.base.util.common import Utils

from dlake.base.util.logger import Logger

LOGGER = Logger.get_logger('IMetadata')


class IMetadata:
    job_name: str
    scenarios: list[MetaScenario]
    session: JobSession
    responses: list
    histories: list

    def __init__(self, session: JobSession):
        self.session = session
        self.job_name = session.name
        self.scenarios = []
        self.histories = []
        self.responses = []

    def load_scenarios(self):
        pass

    def save_history(self, history):
        pass

    def get_latest_history(self, meta_extract: ExtractMeta, meta_load: LoadMeta):
        pass

    def get_quality_rules(self):
        pass

    @staticmethod
    def init(session: JobSession):
        from dlake.base.type.spark import SparkEnv
        match Utils.get_spark_env(env=session.env):
            case SparkEnv.LOCAL:
                # from dlake.base.component.metadata.local import LocalMetadata
                # meta = LocalMetadata(session)
                from dlake.base.component.metadata.s3 import S3Metadata
                meta = S3Metadata(session)
            case SparkEnv.GLUE:
                # from dlake.base.component.metadata.dynamo import DynamoMetadata
                # meta = DynamoMetadata(session)
                from dlake.base.component.metadata.s3 import S3Metadata
                meta = S3Metadata(session)
            case _:
                LOGGER.error('Metadata Type not support = %s', type)
                raise Exception('Metadata Type not support = %s', type)
        meta.load_scenarios()
        return meta
