from pyspark.sql import SparkSession

from dlake.base.component.ispark import ISpark


class SparkLocal(ISpark):
    def __init__(self, job_name):
        super().__init__(job_name)

    def init_session(self):
        self.spark:SparkSession = (
            SparkSession
            .builder
            .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
            .appName(self.job_name)
            .getOrCreate()
        )
        self.spark._jsc.hadoopConfiguration().set(
            "fs.s3a.aws.credentials.provider", 
            "com.amazonaws.auth.InstanceProfileCredentialsProvider,com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
        return self.spark

    def close_session(self):
        self.spark.stop()

