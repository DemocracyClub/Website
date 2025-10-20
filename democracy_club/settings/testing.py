from .base import *  # noqa


STORAGES["staticfiles"] = {"BACKEND": "pipeline.storage.PipelineStorage"}  # noqa F405

SITE_TITLE = "democracy club"
