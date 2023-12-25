#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from yaml_util import read_yaml

from qiniu import put_file, Auth, BucketManager, build_batch_delete


class QiniuFunction(object):
    def __init__(self, access_key=read_yaml('access_key', 'config'), secret_key=read_yaml('secret_key', 'config'),
                 bucket=str(read_yaml('bucket_name', 'config'))):
        self.bucket = bucket
        self.q = Auth(access_key, secret_key)

    def upload_file(self, local_file, remote_file):
        # 上传后保存的文件名
        token = self.q.upload_token(self.bucket, remote_file, 999999)
        ret, info = put_file(token, remote_file, local_file, version='v2')
        return ret, info