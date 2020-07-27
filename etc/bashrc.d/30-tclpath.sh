#!/bin/bash

##############################################################################
# CAFE: Organize your Unix packages
# https://github.com/markuskimius/cafe
#
# Copyright (c)2020 Mark K. Kim
# Released under the Apache license 2.0
# https://github.com/markuskimius/cafe/blob/master/LICENSE
##############################################################################

for __cafe_dir in "${CAFE}"/*/lib; do
    [[ -d "${__cafe_dir}" ]] || continue                           # Not a directory
    [[ ":${TCLLIBPATH-}:" == *":${__cafe_dir}:"* ]] && continue    # Already in $TCLLIBPATH
    ls "${__cafe_dir}"/pkgIndex.tcl &> /dev/null || continue       # No pkgIndex.tcl in the directory

    TCLLIBPATH="${__cafe_dir}:${TCLLIBPATH}"
done

unset __cafe_dir

