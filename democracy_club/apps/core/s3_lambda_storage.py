import os
from distutils.dir_util import copy_tree

from pipeline.compilers.sass import SASSCompiler

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django.contrib.staticfiles.storage import ManifestFilesMixin
from pipeline.storage import PipelineMixin

from django.contrib.staticfiles.finders import FileSystemFinder


class ReadOnlySourceFileSystemFinder(FileSystemFinder):
    """
    A Django storage class for finding static files on a read only file system
    or directory.

    ## Why is this needed?

    Finding files doesn't require write permissions, however 3rd party
    projects like Django Pipeline can implement a `post_process` step.

    This step takes the list of files returned by `list` and processes them,
    in pipeline's case by converting them from scss to css etc.

    The `post_process` step can change the file name, but if the file isn't
    written to a path that a finder can find then it's ignored in later steps.

    For example, ManifestFilesMixin won't know about that file.

    To make everything work this Finder runs exactly like the normal
    FileSystemFinder, but then copies the whole assets tree to a writable
    location. It then updates the paths for all the files to that new location,
    meaning all other processing of that file can happen as normal.

    Manuel Both-Hanz pulled his hair out to bring you this information.
    """

    def list(self, ignore_patterns):
        for origin_path, dest_path in settings.READ_ONLY_PATHS:
            if dest_path.endswith('/'):
                raise ValueError(
                    "dest_path '{}' can't end with trailing /".format(
                        dest_path)
                )

        super_list = list(super(
            ReadOnlySourceFileSystemFinder, self).list(ignore_patterns))

        for filename, file_storage in super_list:
            location = file_storage.location
            for origin_path, dest_path in settings.READ_ONLY_PATHS:
                if location.startswith(origin_path):
                    new_location = location.replace(origin_path, dest_path)
                    copy_tree(location, new_location)
                    file_storage.location = new_location

        return super_list


class MediaStorage(S3Boto3Storage):
    """
    Store media files at MEDIAFILES_LOCATION, post-process with pipeline
    and then create manifest files for them.
    """
    location = settings.MEDIAFILES_LOCATION


class StaticStorage(PipelineMixin, ManifestFilesMixin, S3Boto3Storage):
    """
    Store static files at STATICFILES_LOCATION, post-process with pipeline
    and then create manifest files for them.
    """
    location = settings.STATICFILES_LOCATION


class LambdaSASSCompiler(SASSCompiler):
    """
    Use libsass's python API for converting scss files to css.

    The normal SASSCompiler opens a subprocess to call scss, but this confuses
    lambda as the script isn't on the PATH.

    """

    def compile_file(self, infile, outfile, outdated=False, force=False):
        for origin_path, dest_path in settings.READ_ONLY_PATHS:
            if outfile.startswith(origin_path):
                outfile = outfile.replace(origin_path, dest_path)
        import sass
        out_value = sass.compile(
            filename=infile,
            output_style='compressed',
            include_paths=settings.SASS_INCLUDE_PATHS
        )
        if type(out_value) == bytes:
            out_value = out_value.decode('utf8')
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        with open(outfile, 'w') as out:
            out.write(out_value)
