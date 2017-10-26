#-*-encoding:utf-8-*-

import os
import tools.packerng as packer

ARCHIVE_FORMAT = '${name}-${market}${ext}'

if __name__ == '__main__':
    print '--------- start ---------'

    apkfile = None
    for s in os.listdir("."):
        if s.endswith(".apk"):
            apkfile = s
            break

    if apkfile:
        packer._check(apkfile=apkfile, format=ARCHIVE_FORMAT)
    else:
        print 'Please put your apk in root dir first !'

    os.system("pause")
