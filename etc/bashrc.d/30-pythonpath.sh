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
    [[ ":${PYTHONPATH-}:" == *":${__cafe_dir}:"* ]] && continue    # Already in $PYTHONPATH
    ls "${__cafe_dir}"/*.py* &> /dev/null || continue              # No Python files in the directory

    PYTHONPATH="${__cafe_dir}:${PYTHONPATH}"
done

unset __cafe_dir

