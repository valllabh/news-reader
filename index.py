def handler(event):
    print("Function was invoked with event: {}".format(event))
    
    # get post param "url" from event
    url = event.get("queryStringParameters", {}).get("url", "")
    
    return {
        "statusCode": 200,
        "body": f"URL: {url}"
    }
