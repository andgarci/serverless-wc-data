import json
import boto3
from services.WorldCup import WCData
from symbol import parameters

def lambda_handler(event, context):
    try:
        host = event['queryStringParameters']['host']
        ssm_client = boto3.client('ssm')
        parameter = ssm_client.get_parameter(
            Name='/development/dynamo_table',
            WithDecryption=False
        )
        table_name = parameter['Parameter']['Value']
        wrapper = WCData(table_name)
        items = wrapper.get_host(host)
        status = 200
    except Exception as e:
        status = 400
        items = {"message": "Cant obtain information for provided host", "error": str(e)}
        print(e)

    return {
        "statusCode": status,
        "body": json.dumps({
            "message": items
        }, indent=4, sort_keys=True, default=str),
    }
