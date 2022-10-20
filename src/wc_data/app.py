import json
import requests
from services.WorldCup import WCData

def lambda_handler(event, context):
    try:
        host = event['queryStringParameters']['host']
        wrapper = WCData("simple-test")
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
