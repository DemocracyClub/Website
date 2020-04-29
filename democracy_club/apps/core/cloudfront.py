from datetime import datetime

import boto3

from django.conf import settings


def invalidate_paths(path_list):
    if not hasattr(settings, "ZAPPA_STAGE"):
        return
    cloudfront = boto3.client("cloudfront")

    cloudfront.create_invalidation(
        DistributionId=settings.AWS_CLOUD_FRONT_ID,
        InvalidationBatch={
            "Paths": {"Quantity": len(path_list), "Items": path_list},
            "CallerReference": "django-invalidate-{}".format(datetime.now()),
        },
    )
