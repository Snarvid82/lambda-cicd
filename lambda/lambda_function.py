import json

def lambda_handler(event, contect):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello updated lambda from vscode')
    }