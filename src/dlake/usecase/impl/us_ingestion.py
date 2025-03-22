import json

from dlake.base.util.logger import Logger
from dlake.core.session.spark import SparkSession
from dlake.factory.etl import ETLFactory
from dlake.usecase.usecase import UseCase
from dlake.base.util.date import DateUtil
from dlake.base.model.meta_scenario import MetaScenario
from dlake.base.model.meta_history import HistoryMeta

LOGGER = Logger.get_logger("IngestionUseCaseImpl")


class IngestionUseCaseImpl(UseCase):
    def process(self):
        LOGGER.info("[process] starting ingestion with job_name = %s", self.metadata.job_name)
        spark_session = SparkSession(metadata=self.metadata)
        self.responses.job_name = self.metadata.job_name
        errors = []
        for scenario in self.metadata.scenarios:
            try:
                params = self.get_params(scenario)
                self.responses.source_object = scenario.extracts[0].source_object
                LOGGER.debug("[process] scenario = %s", json.dumps(scenario.extracts[0].source_object))
                LOGGER.info("[process] Execute Pre Function...")
                LOGGER.info("[process] Extracting...")
                extract_result = ETLFactory.extract(
                    spark=spark_session.spark, 
                    extract_meta=scenario.extracts[0],
                    args = params
                )
                df = extract_result.get("data")
                LOGGER.info("[process] Transforming...")
                df = ETLFactory.transforms(dataframe=df,udf_infos=scenario.udf_infos)
                LOGGER.info("[process] Loading...")
                ETLFactory.load(dataframe=df, load_meta=scenario.load)
                LOGGER.info("[process] Execute Post Function...")
                self.responses.status = "SUCCESS"
                self.responses.criteria_value = extract_result.get("criteria_value")
            except Exception as e:
                self.responses.status = "FAILED"
                self.responses.message = str(e)
                errors.append(str(e))
            self.metadata.save_history(self.responses)
            if len(errors) > 0:
                raise Exception(str(errors))
    def get_params(self, meta: MetaScenario):
        latest_date = self.metadata.get_latest_history(meta.extracts[0], meta.load)
        LOGGER.debug("latest date from history: %s", latest_date)
        to_date = DateUtil.now()
        LOGGER.debug("to_date: %s", to_date)
        return {
            "from_date": latest_date,
            "to_date": to_date
        }

