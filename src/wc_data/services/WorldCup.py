import logging
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class WCData:
    def __init__(self, table):
        self.dynclient = boto3.resource('dynamodb')
        self.table = self.dynclient.Table(table)

    def get_host(self, host):
        try:
            result = self.table.query(
                KeyConditionExpression=Key('host').eq(str(host))
            )
            print(result)
        except ClientError as err:
            logger.error(
                "Couldn't get world cup host %s from table %s. Here's why: %s: %s",
                host, self.table.name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
        else:
            return result['Items']
