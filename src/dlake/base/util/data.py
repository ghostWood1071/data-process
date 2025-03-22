from dlake.base.type.source import SourceType, SourceSubType
from dlake.base.model.meta_extract import ExtractMeta
from dlake.base.util.logger import Logger
from dlake.base.util.str import StrUtil
from dlake.base.util.date import DateUtil
from datetime import datetime
import zoneinfo
import boto3
import re
import io

LOGGER = Logger.get_logger(__name__)

class DataUtil:
    @staticmethod
    def get_dict_value(args: dict, key: str):
        if key in args.keys():
            return args[key]
        else:
            return None
    
    @staticmethod
    def get_list_objects(extract_meta: ExtractMeta, from_date:datetime = None, to_date:datetime = None):
        is_get_all = from_date is None and to_date is None
        if from_date is not None:
            from_date = DateUtil.to_utc(from_date)
        if to_date is not None:
            to_date = DateUtil.to_utc(to_date)
        s3_client = boto3.client("s3")
        paginator = s3_client.get_paginator("list_objects_v2")
        file_name, date_format, extension = StrUtil.split_file_name(extract_meta.source_object)
        date_pattern = StrUtil.reformated_date_pattern(date_format)
        object_key_pattern = StrUtil.build_string(
            extract_meta.source_schema, 
            f"{file_name}{date_pattern}{extension}$",
            separator="/"
        )
        prefix = StrUtil.build_string(extract_meta.source_schema,file_name,separator="/")
        LOGGER.debug("file prefix : %s", prefix)
        LOGGER.debug("filter pattern : %s", object_key_pattern)
        pages = paginator.paginate(Bucket=extract_meta.source_zone, Prefix=prefix)
        paths = []
        for page in pages:
            if 'Contents' in page:
                for obj in page["Contents"]:
                    LOGGER.debug("object: %s", obj)
                    if re.match(object_key_pattern, obj["Key"]):
                        if is_get_all:
                            paths.append(f"s3a://{extract_meta.source_zone}/{obj['Key']}")
                            continue
                        if from_date <= obj["LastModified"] <= to_date:
                            paths.append(f"s3a://{extract_meta.source_zone}/{obj['Key']}")
        return paths
    
    @staticmethod
    def read_s3_object(bucket:str, obj_key:str):
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket, Key=obj_key)
        return io.BytesIO(obj["Body"].read())
    
    @staticmethod
    def write_s3_object(bucket:str, object_key:str, data):
        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket, Key=object_key, Body=data, ContentType="application/octet-stream")