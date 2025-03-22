from pyspark.sql import DataFrame

from dlake.base.type.udf import UDFParam
from dlake.base.util.logger import Logger

LOGGER = Logger.get_logger("UDF")


class UDF:
    df: DataFrame

    def __init__(self, dataframe: DataFrame):
        self.df = dataframe

    def str_ptime(self, args:dict=None):
        LOGGER.info("[str_ptime] args=%s",args)
        #TODO:

    @staticmethod
    def transforms(dataframe: DataFrame, udf_infos:list=None) -> DataFrame:
        LOGGER.debug("[transfroms] udf_infos=%s",udf_infos)
        udf_infos = sorted(udf_infos, key=lambda  x:x[UDFParam.INDEX])
        udf = UDF(dataframe=dataframe)
        for udf_info in udf_infos:
            f_name = udf_info.get(UDFParam.TYPE).lower()
            f_args = udf_info.get(UDFParam.ARGS)
            func = udf.__getattribute__(f_name)
            func(f_args)
        return udf.df

