#!/usr/bin/env python
# coding: utf-8

import commands
import sys


def get_vms_status(arg):
    tmp = []
    if arg == 'StraightHairScan':
        _, result = commands.getstatusoutput('/usr/bin/curl -o /dev/null -s -w '
                                             '"%{time_total}" '
                                             '"http://wms.demo.com/xxx.php?op=StraightHairScan"')
        tmp.append(result)
    elif arg == 'CheckProcessCode':
        _, result = commands.getstatusoutput('/usr/bin/curl -o /dev/null -s -w '
                                             '"%{time_total}" '
                                             '"http://wms.demo.com/yyy.php?op=CheckProcessCode"')
        tmp.append(result)
    elif arg == 'ScanProcessCode':
        _, result = commands.getstatusoutput('/usr/bin/curl -o /dev/null -s -w '
                                             '"%{time_total}" '
                                             '"http://wms.demo.com/zzz.php?op=ScanProcessCode"')
        tmp.append(result)
    else:
        print "ERROR: --- wrong arg ---"
        sys.exit(2)

    print int(float(tmp[0]) * 1000)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "ERROR: " + sys.argv[0] + " <arg>"
        sys.exit(2)
    else:
        get_vms_status(arg=sys.argv[1])
