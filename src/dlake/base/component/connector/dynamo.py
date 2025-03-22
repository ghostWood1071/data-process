from boto3.dynamodb.conditions import ComparisonCondition

from dlake.base.component.iconnector import IConnector
from dlake.base.util.logger import Logger
import boto3

LOGGER = Logger.get_logger('DynamoConnector')


class DynamoConnector(IConnector):

    def connect(self):
        LOGGER.debug("[connect] Init aws resource dynamodb")
        self.conn = boto3.resource('dynamodb')
        return self

    def select(self, table_name: str, condition: dict, limit: int = 100):
        LOGGER.debug('[select] starting ...')
        table = self.conn.Table(table_name)
        filter = {}
        if condition is not None:
            for key, value in condition:
                filter_item = {
                    'AttributeValueList': [
                        value
                    ],
                    'ComparisonOperator': 'EQ'
                }
                filter.__setattr__(key, filter_item)
        resource = table.scan(
            Limit=limit,
            Select='ALL_ATTRIBUTES',
            ScanFilter=filter
        )
        LOGGER.debug('[select] response = %s', resource)
        return resource.get('Items')

    def select_one(self, table_name: str, condition: dict):
        LOGGER.debug('[select_one] table_name=%s condition=%s', table_name, condition)
        # TODO:

    def update(self, table_name: str, data: dict, condition: dict):
        LOGGER.debug('[update] table_name=%s data=%s condition=%s', table_name, data, condition)
        # TODO:

    def delete(self, table_name: str, condition: dict):
        LOGGER.debug('[delete] table_name=%s condition=%s', table_name, condition)
        # TODO:

    def insert(self, table_name: str, obj: dict):
        LOGGER.debug('[insert] table_name=%s data=%s', table_name, obj)
        # TODO:

    def execute(self, sql: str):
        LOGGER.debug('[execute] sql=%s', sql)
        # TODO:

    def scan_by_condition(self, table_name: str, condition: dict | ComparisonCondition = {}, projections: list = [],
                          limit: int = 100):
        LOGGER.debug('[scan_by_condition] table_name=%s conditions=%s', table_name, condition)
        params = {}
        if type(condition) == dict:
            if len(condition.keys()) > 0:
                params['FilterExpression'] = condition
        elif type(condition) == ComparisonCondition:
            params['FilterExpression'] = condition
        if len(projections) > 0:
            params['ProjectionExpression'] = projections
        else:
            params['Select'] = 'ALL_ATTRIBUTES'
        table = self.conn.Table(table_name)
        params['Limit'] = limit
        response = table.scan(**params)
        results = response.get('Items',[])
        LOGGER.debug('[scan_by_condition] done scan with %s records',len(results))
        return results

    def close(self):
        LOGGER.warn('[close] no support')
