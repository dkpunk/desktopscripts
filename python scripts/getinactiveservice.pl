#!/usr/bin/perl

$OUT=`systemctl --all | grep "inactive"`;
print $OUT;
exit 0

