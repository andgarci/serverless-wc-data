import json
import boto3
from services.WorldCup import WCData

def lambda_handler(event, context):
    #try:
        #for record in event['Records']:
            #pull the body out & json load it
            #jsonmaybe=(record["body"])
            #jsonmaybe=json.loads(jsonmaybe)
            
            #now the normal stuff works
            #world_cup_event = jsonmaybe["Records"][0]["world_cup"]
            #print(world_cup_event)
    # except Exception as e:
    #     status = 400
    #     items = {"message": "Can't obtain Records", "error": str(e)}
    #     print(e)

    status = 200
    items = []

    return {
        "statusCode": status,
        "body": json.dumps({
            "message": event
        }, indent=4, sort_keys=True, default=str),
    }
