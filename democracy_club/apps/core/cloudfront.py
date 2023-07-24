import os
from datetime import datetime


def invalidate_paths(path_list):
    # Only run on Lambda
    if "AWS_EXECUTION_ENV" not in os.environ:
        return None
    # We don't always have boto, because we're not always on Lambda
    # and it's not a dependancy of this project. Fail nicely in this case.
    try:
        import boto3
    except ImportError:
        return None
    cloudfront = boto3.client("cloudfront")

    # Find the dist ARN for a given cname
    dist_id = None
    for dist in cloudfront.list_distributions()["DistributionList"]["Items"]:
        cnames = [a["CNAME"] for a in dist["AliasICPRecordals"]]
        if os.environ.get("FQDN") in cnames:
            dist_id = dist["ARN"].split("/")[-1]

    if not dist_id:
        return None

    for i, path in enumerate(path_list):
        if not path.startswith("/"):
            path_list[i] = f"/{path}"

    return cloudfront.create_invalidation(
        DistributionId=dist_id,
        InvalidationBatch={
            "Paths": {"Quantity": len(path_list), "Items": path_list},
            "CallerReference": "django-invalidate-{}".format(datetime.now()),
        },
    )
