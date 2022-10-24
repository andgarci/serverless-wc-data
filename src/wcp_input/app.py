import json
import boto3
from services.WorldCup import WCData

def lambda_handler(event, context):
    # try:
    #     host = event['queryStringParameters']['host']
    #     ssm_client = boto3.client('ssm')
    #     table_name = ssm_client.get_parameter(
    #         Names='/development/dynamo_table',
    #         WithDecryption=False
    #     )
    #     wrapper = WCData("simple-test")
    #     items = wrapper.get_host(host)
    #     status = 200
    # except Exception as e:
    #     status = 400
    #     items = {"message": "Cant obtain information for provided host", "error": str(e)}
    #     print(e)

    status = 200
    items = []

    return {
        "statusCode": status,
        "body": json.dumps({
            "message": event
        }, indent=4, sort_keys=True, default=str),
    }
