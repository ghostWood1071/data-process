from dlake.core.session.job import JobSession
from dlake.base.type.env import ENV
from dlake.base.util.logger import Logger
from dlake.base.util.str import StrUtil
from dlake.usecase.usecase import UseCase

LOGGER = Logger.get_logger("USFactory")


class USFactory:
    @staticmethod
    def run(env: ENV = ENV.DEV, job_name: str = None):
        # try:
        LOGGER.info("[run] init job session env=%s", env.name)
        session = JobSession(env=env)
        if not StrUtil.isblank(job_name):
            session.name = job_name
        LOGGER.info("[run] init use case")
        us = UseCase.init(session)
        LOGGER.info("[run] processing use case logic")
        us.process()
        LOGGER.info("[run] done!")
        # except Exception as ex:
        #     LOGGER.error("[run] msg=%s",ex)


if __name__ == '__main__':
    USFactory.run(env=ENV.DEV, job_name='etl_ingestion_1')
