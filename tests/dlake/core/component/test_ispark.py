import unittest

from dlake.base.type.env import ENV
from dlake.base.component.ispark import ISpark


class ISparkTestCase(unittest.TestCase):
    def test_spark_local_init(self):
        from pyspark.sql.types import StructType, StructField, StringType, IntegerType
        spark_session = ISpark.init(job_name='UNIT_TEST_LOCAL', env=ENV.DEV)
        spark = spark_session.init_session()
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

        spark_session.close_session()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
