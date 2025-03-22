from dlake.base.service.extract import Extract
from dlake.base.type.param import ParamKey
from dlake.base.util.logger import Logger
from dlake.base.util.str import StrUtil
from dlake.base.util.data import DataUtil


LOGGER = Logger.get_logger("CSVExtract")


class CSVExtract(Extract):

    def process(self):
        # paths = self.get_path()
        # LOGGER.debug("this is paths: %s", paths)
        self.get_date_filter()
        list_objects = DataUtil.get_list_objects(self.extract_meta, self.from_date, self.to_date)
        LOGGER.debug("this is paths: %s", list_objects)
        spark_reader = self.spark.read.format("csv")
        if not StrUtil.isblank(self.extract_meta.params.get(ParamKey.HEADER)):
            LOGGER.debug("[process] set header for df")
            spark_reader = spark_reader.option(header=self.extract_meta.params.get(ParamKey.HEADER))
        if not StrUtil.isblank(self.extract_meta.schema):
            LOGGER.debug("[process] set schema for df: %s", self.extract_meta.schema)
            spark_reader = spark_reader.schema(self.extract_meta.schema)
        
        df = None
        for object in list_objects:
            try:
                LOGGER.debug("[process] path=%s",object)
                if df is None:
                    df = spark_reader.load(object)
                    continue
                df = df.union(spark_reader.load(object))
            except Exception as e:
                LOGGER.debug("[process] object cause error: %s", object)
                raise e      
        LOGGER.debug("[process] criteria_value: %s", self.to_date)        
        return {
            "data": df,
            "criteria_value": self.to_date
        }

    


    


