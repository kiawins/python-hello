import unzip_requirements
import os

def html(event, context):

    html = """
    <html>
        <body>
            <h1>
                Upload a csv to get the graphs
            </h1>
            <form action="graph" method="POST" enctype="multipart/form-data">
                <input type="file" name="file" accept="text/csv"/>
                <input type="submit"/>
            </form>
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
