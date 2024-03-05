import json
import urllib3
import os

def lambda_handler(event, context):
    
    http = urllib3.PoolManager()

    response = http.request('GET',
                        os.environ["data_url"],
                        retries = False)
    
    characters = json.loads(response.data.decode("utf-8"))

    if "queryStringParameters" in event: 
        queries = event["queryStringParameters"]
        
        hero_name = queries['hero']
        villain_name = queries['villain']
        
        hero = None
        villain = None
        winner = None
        
        for character in characters["items"]:
            if character["name"] == hero_name:
                hero = character
            if character["name"] == villain_name:
                villain = character
                
        winner = hero if hero["score"] >= villain["score"] else villain
        
    return {
        'statusCode': 200,
        'body': json.dumps(winner)
    }
