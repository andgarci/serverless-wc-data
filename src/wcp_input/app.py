import logging
import json
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    try:
        client = boto3.client('dynamodb')
        ssm_client = boto3.client('ssm')

        parameter = ssm_client.get_parameter(
            Name='/development/dynamo_table',
            WithDecryption=False
        )
        table_name = parameter['Parameter']['Value']
    except Exception as e:
        status = 500
        items = {"message": "Can't create resources", "error": str(e)}
        logger.error(items)

    try:
        for message in event['Records']:
            json_item = json.loads(message["body"])
            response = client.put_item(
                Item=json_item,
                ReturnConsumedCapacity='TOTAL',
                TableName=table_name,
            )
            logger.info(response)

    except Exception as e:
        status = 400
        items = {"message": "Can't obtain Records", "error": str(e)}
        logger.error(items)

    status = 200
    items = []

    return {
        "statusCode": status,
        "body": json.dumps({
            "message": items
        }, indent=4, sort_keys=True, default=str),
    }
