import unzip_requirements
import json



def update(event, context):

  result = {
    "foo": "bar"
  }

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(
          result,
          cls=decimalencoder.DecimalEncoder
        )
    }

    return response
