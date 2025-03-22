from pyspark.sql import DataFrame

from dlake.base.model.meta_extract import ExtractMeta
from dlake.base.model.meta_load import LoadMeta
from dlake.base.service.udf import UDF
from dlake.base.type.source import SourceType, SourceSubType
from dlake.base.type.target import TargetType, TargetSubType
from dlake.base.util.logger import Logger
from dlake.core.service.extract.database import DatabaseExtract

LOGGER = Logger.get_logger("ETLFactory")

class ETLFactory():
    
    @staticmethod
    def extract(extract_meta: ExtractMeta, spark, args:dict):
        match extract_meta.source_type:
            case SourceType.S3:
                match extract_meta.source_sub_type:
                    case SourceSubType.CSV:
                        from dlake.core.service.extract.s3_csv import CSVExtract
                        extract = CSVExtract(extract_meta=extract_meta, spark=spark, args=args)
                    case _:
                        raise Exception("[extract] dont support source_type=%s source_sub_type",
                                        extract_meta.source_type, extract_meta.source_sub_type)
            case SourceType.DATABASE:
                extract = DatabaseExtract(extract_meta=extract_meta, spark=spark, args=args)
            case _:
                raise Exception("[extract] dont support source_type=%s", extract_meta.source_type)
        return extract.process()

    @staticmethod
    def load(dataframe, load_meta: LoadMeta):
        match load_meta.target_type:
            case TargetType.S3:
                match load_meta.target_sub_type:
                    case TargetSubType.CSV:
                        from dlake.core.service.load.csv import CSVLoadImpl
                        load = CSVLoadImpl(dataframe=dataframe, load_meta=load_meta)
                    case _:
                        raise Exception("[load] dont support target_type=%s target_sub_type",
                                        load_meta.target_type, load_meta.target_sub_type)
            # case TargetType.DATABASE:
            #     extract = DatabaseExtract(extract_meta=extract_meta, spark=spark)
            case _:
                raise Exception("[load] dont support target_type=%s", load_meta.target_type)
        load.process()

    @staticmethod
    def transforms(dataframe: DataFrame, udf_infos: list = None):
        return UDF.transforms(dataframe=dataframe, udf_infos=udf_infos)
