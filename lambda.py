def function(event, context):
    print(event)
    return {
        "statusCode": 200,
        "body": "Test"
    }
