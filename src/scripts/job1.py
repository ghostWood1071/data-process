from dlake.base.type.env import ENV
from dlake.factory.usecase import USFactory


if __name__ == '__main__':
    USFactory.run(env=ENV.DEV, job_name='etl_ingestion_1')