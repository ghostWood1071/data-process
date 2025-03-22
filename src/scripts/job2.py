from main.dlake import ISpark
from main.dlake import ENV

session = ISpark.init(ENV.DEV, 'TEST')
spark = session.init_session()

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

empty_rdd = spark.sparkContext.emptyRDD()
schema = StructType(
    [
        StructField("Column1", StringType(), True),
        StructField("Column2", IntegerType(), True),
        StructField("Column3", StringType(), True),
    ]
)
empty_df = spark.createDataFrame(empty_rdd, schema)
empty_df.show()

spark.stop()