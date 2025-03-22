import unittest

from dlake.base.type.env import ENV
from dlake.core.session.spark import SparkSessionInit


class SparkSessionInitTestCase(unittest.TestCase):
    def test_init(self): 
        session = SparkSessionInit(ENV.DEV)
        spark = session.spark
        df = spark.read.format("csv").options(header="true", inferSchema="true").load(
            "../../../../data/source/returns_data/partition_date=2023-01-01/part-00000-f192eabf-55e7-4e83-ad69-ae3bd26ec27d-c000.csv")
        df.show()
        session.close()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
