# -*- coding: utf-8 -*-

# Copyright (c) 2012 theo crevon
#
# See the file LICENSE for copying permission.

PUREFTPD_SERVICE_NAME = 'pure-ftpd'
PUREFTPD_CONF_DIR = '/etc/pure-ftpd/conf'

PUREFTPD_OPTIONS = [
    "NoTruncate",
    "LogPid",
    "ipv4only",
    "ipv6only",
    "TrustedGid",
    "ChrootEveryone",
    "Daemonize",
    "MaxClientsNumber",
    "MaxClientsPerIP",
    "VerboseLog",
    "DisplayDotFiles",
    "AnonymousOnly",
    "NoAnonymous",
    "SyslogFacility",
    "FortunesFile",
    "PidFile",
    "DontResolve",
    "AnonymousCantUpload",
    "MaxIdleTime",
    "CreateHomeDir",
    "MaxDiskUsage",
    "KeepAllFiles",
    "login",
    "LimitRecursion",
    "MaxLoad",
    "AnonymouScanCreateDirs",
    "NatMode",
    "AltLog",
    "PassivePortRange",
    "ForcePassiveIP",
    "AnonymousRatio",
    "UserRatio",
    "AutoRename",
    "NoChmod",
    "AntiWarez",
    "UserBandwidth",
    "AnonymousBandwidth",
    "MinUID",
    "Umask",
    "TrustedIP",
    "ProhibitDotFilesWrite",
    "ProhibitDotFilesRead",
    "PeruserLimits",
    "AllowDotFiles",
]