import unzip_requirements
import os

def html(event, context):

    html = """
    <html>
        <body>
            <h1>
                Hello world
            </h1>
        </body>
    </html>
    """

    # create a response
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html
    }

    return response
