import json

def response(statusCode, message, data=None):
    
    return {
            'statusCode': statusCode,
            'body': json.dumps({
                'message' : message,
                'data': data
            })
        }

def response_error(statusCode, message):
    
    return {
            'statusCode': statusCode,
            'body': json.dumps({
                'message' : message,                
            })
        }
    
def get_input_data(event:dict):
    
    method = event['requestContext']['http']['method'] 
    
    _data = {
        'GET'  : 'queryStringParameters',
        'POST' : 'body',
        'PUT'  : 'body',
    }
    
    data = _data.get(method)
    
    if method == 'GET':
        return event[data]
        
    return json.loads(event[data])