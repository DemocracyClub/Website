# import mimetypes
# import os


from django.conf import settings

# from django.core.files.base import File
from storages.backends.s3boto3 import S3Boto3Storage  # , SpooledTemporaryFile


class PatchedS3Boto3Storage(S3Boto3Storage):
    pass

    # """
    # Note: We need to patch S3Boto3Storage
    # to apply a fix which stops botocore from throwing
    #
    # Invalid type for parameter ContentType, value: b'text/javascript',
    # type: <class 'bytes'>, valid types: <class 'str'>: ParamValidationError
    #
    # Unfortunately this lives in the middle of quite a long method
    # so we've got a big old chunk of copy+pasted code here :(
    #
    # Also we need to be really careful we don't upgrade the
    # django-storages package while this monkey-patch is in place
    # as this may yield unexpected behaviour.
    # """
    #
    # def _save(self, name, content):
    #     cleaned_name = self._clean_name(name)
    #     name = self._normalize_name(cleaned_name)
    #     parameters = self.object_parameters.copy()
    #     _type, encoding = mimetypes.guess_type(name)
    #     content_type = getattr(content, "content_type", None)
    #     content_type = content_type or _type or self.default_content_type
    #     if type(content_type) == bytes:
    #         content_type = content_type.decode("utf8")
    #
    #     # setting the content_type in the key object is not enough.
    #     parameters.update({"ContentType": content_type})
    #
    #     if self.gzip and content_type in self.gzip_content_types:
    #         content = self._compress_content(content)
    #         parameters.update({"ContentEncoding": "gzip"})
    #     elif encoding:
    #         parameters.update({"ContentEncoding": encoding})
    #
    #     encoded_name = self._encode_name(name)
    #     obj = self.bucket.Object(encoded_name)
    #     if self.preload_metadata:
    #         self._entries[encoded_name] = obj
    #
    #     if isinstance(content, File):
    #         content = content.file
    #
    #     self._save_content(obj, content, parameters=parameters)
    #     return cleaned_name
    #
    # def _save_content(self, obj, content, parameters):
    #     """
    #     We create a clone of the content file as when this is passed to boto3
    #     it wrongly closes the file upon upload where as the storage backend
    #     expects it to still be open
    #     """
    #     # Seek our content back to the start
    #     content.seek(0, os.SEEK_SET)
    #
    #     # Create a temporary file that will write to disk after a specified
    #     # size
    #     content_autoclose = SpooledTemporaryFile()
    #
    #     # Write our original content into our copy that will be closed by boto3
    #     content_autoclose.write(content.read())
    #     # Upload the object which will auto close the content_autoclose
    #     # instance
    #     super()._save_content(obj, content_autoclose, parameters)
    #
    #     # Cleanup if this is fixed upstream our duplicate should always close
    #     if not content_autoclose.closed:
    #         content_autoclose.close()


class MediaStorage(PatchedS3Boto3Storage):
    """
    Store media files at MEDIAFILES_LOCATION, post-process with pipeline
    and then create manifest files for them.
    """

    location = settings.MEDIAFILES_LOCATION
