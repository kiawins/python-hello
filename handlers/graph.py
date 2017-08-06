import unzip_requirements
import json
from cgi import parse_header, parse_multipart
from io import BytesIO
from StringIO import StringIO
import pandas as pd


from handlers import decimalencoder

def post(event, context):
    c_type, c_data = parse_header(event['headers']['content-type'])
    assert c_type == 'multipart/form-data'
    body = event['body'].encode('utf8')
    form_data = parse_multipart(BytesIO(body), c_data)
    csv_str = form_data['file'][0]

    html = """
    <html>
        <body>
            <h1>
                Here are the results
            </h1>
            <div>{data}</div>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </body>
    </html>
    """.format(data=pd.read_csv(StringIO(csv_str)))



    # create a response
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html
        # "body": json.dumps(
        #   result,
        #   cls=decimalencoder.DecimalEncoder
        # )
    }

    return response
