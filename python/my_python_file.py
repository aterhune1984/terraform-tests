import json

def lambda_handler(event, context):
   message = 'Hello World!'
   return {
       'statusCode': 200,
       'body': json.dumps(message)
   }
