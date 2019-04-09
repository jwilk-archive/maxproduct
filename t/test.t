#!/bin/sh

# Copyright © 2019 Jakub Wilk <jwilk@jwilk.net>
# SPDX-License-Identifier: MIT

set -e -u

here="${0%/*}"
prog="$here/../maxproduct"
echo 1..1
n=$(wc -l < "$here/output.txt")
tmpfile=$(mktemp -t printfify.XXXXXX)
"$prog" "$n" "$here/forenames.txt" "$here/surnames.txt" > "$tmpfile"
if cmp -s "$here/output.txt" "$tmpfile"
then
    echo ok 1
else
    diff -u "$here/output.txt" "$tmpfile" | sed -e 's/^/# /'
    echo not ok 1
fi
rm "$tmpfile"

# vim:ts=4 sts=4 sw=4 et ft=sh
