from __future__ import print_function

import boto3
import time

def lambda_handler(event, context):
    for items in event["Records"]:
        path = "/*"                                          #It update the content all whatever inside origin update it over cloudfront
        #path = "/" + items["s3"]["object"]["key"]           //fetch latest updated file or object in s3 bucket and invalidate it on cloudfront
        print(path)
        client = boto3.client('cloudfront')
        invalidation = client.create_invalidation(DistributionId='CDN_Distribution_ID',       #"CDN_Distribution_ID" in place add cdn disritbution id
            InvalidationBatch={
            'Paths': {
            'Quantity': 1,
            'Items': [path]
            },
            'CallerReference': str(time.time())
            })