
import unittest
from dlake.base.type.env import ENV
from dlake.factory.usecase import USFactory


class UseCaseTestCase(unittest.TestCase):
    def test_run(self):
        USFactory.run(env=ENV.DEV, job_name='etl_ingestion_1')


# UseCaseTestCase().test_run()