import logging

from dlake.base.type.env import ENV
from dlake.base.type.spark import SparkEnv

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s - %(levelname)s %(name)s - %(message)s"
LOG_DATE_FORMAT = "%m/%d/%Y %I:%M:%S %p"
TEMP_PATH = '/tmp/'
GLUE_CATALOG = 'glue_catalog'
JOB_NAME_DEFAULT = 'job_name'

WAREHOUSE_PATH = {
    ENV.DEV: "../../data/target/",
    ENV.SIT: "../../data/target/",
    ENV.UAT: "../../data/target/",
    ENV.PROD: "../../data/target/",
}

CRAWLER_ROLE = {
    ENV.DEV: "ARN_ROLE",
    ENV.SIT: "ARN_ROLE",
    ENV.UAT: "ARN_ROLE",
    ENV.PROD: "ARN_ROLE",
}

SPARK_ENV = SparkEnv.GLUE

DATE_FORMAT_DEFAULT = ""

JOB_DEFAULT_PARAMS = ["JOB_NAME", "JOB_TYPE"]
