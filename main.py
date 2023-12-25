import sys
from tt_util.qiniu_util import QiniuFunction

if len(sys.argv) != 3:
    print('传参数量不对')
    exit(1)
else:
    local_file = sys.argv[1]
    remote_file = sys.argv[2]
    qiniu = QiniuFunction()
    ret, info = qiniu.upload_file(local_file, remote_file)
    if info.status_code != 200:
        print('上传失败')
        exit(1)
    else:
        print('上传成功')
        exit(0)