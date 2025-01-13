import json

def lambda_handler(event, context):
    """
    AWS Lambda handler function.

    Parameters:
    - event (dict): The event data passed to the function.
    - context (object): Provides methods and properties that provide information about the invocation, function, and execution environment.

    Returns:
    - dict: Response containing status code and body.
    """
    # Log the received event (useful for debugging)
    print("Received event:", json.dumps(event))

    # Example processing: Extract a name from the event, if provided
    name = event.get('name', 'World')

    # Create a response message
    message = f"Hello, {name}!"

    # Return the response in the expected format
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message
        })
    }
