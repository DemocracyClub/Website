from datetime import datetime

from django.conf import settings


def invalidate_paths(path_list):
    if not hasattr(settings, "ZAPPA_STAGE"):
        return
    # We don't always have boto, because we're not always on Lambda
    # and it's not a dependancy of this project. Fail nicely in this case.
    try:
        import boto3
    except ImportError:
        return
    cloudfront = boto3.client("cloudfront")

    cloudfront.create_invalidation(
        DistributionId=settings.AWS_CLOUD_FRONT_ID,
        InvalidationBatch={
            "Paths": {"Quantity": len(path_list), "Items": path_list},
            "CallerReference": "django-invalidate-{}".format(datetime.now()),
        },
    )
