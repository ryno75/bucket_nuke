#!/usr/bin/env python
'''
Ryan Kennedy (ryno75@gmail.com), 2016-07-12
'''
version = '0.4.0'


class Result():
    # Result base class
    def __init__(self, name, objects, object_versions):
        self.name = name
        self.objects = objects
        self.object_versions = object_versions


def nuke_buckets(buckets, region=None, profile=None, debug=False):
    '''
    nuke_buckets

    :type buckets: list
    :param buckets: list of S3 bucket names (strings) to wipe

    :type region: string
    :param buckets: AWS s3 region

    :type verbose: bool
    :param buckets: enable verbose printing
    '''
    import boto3
    from botocore.client import Config
    results = []
    aws = boto3.Session(profile_name=profile, region_name=region)
    s3 = aws.resource('s3', config=Config(signature_version='s3v4'))
    B = [b for b in s3.buckets.all() if b.name in buckets]
    for b in B:
        o_list = [o.key for o in b.objects.all()]
        ov_list = [ov.key for ov in b.object_versions.all()]
        if o_list:
            b.objects.delete()
        if ov_list:
            b.object_versions.delete()
        b.delete()
        results.append(Result(b.name, o_list, ov_list))

    return results
