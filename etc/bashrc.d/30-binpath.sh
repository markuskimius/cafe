#!/bin/bash

##############################################################################
# CAFE: Organize your Unix packages
# https://github.com/markuskimius/cafe
#
# Copyright (c)2020 Mark K. Kim
# Released under the Apache license 2.0
# https://github.com/markuskimius/cafe/blob/master/LICENSE
##############################################################################

for __cafe_dir in "${CAFE}"/*/bin; do
    if [[ -d "$__cafe_dir" ]] && [[ ":${PATH}:" != *":${__cafe_dir}:"* ]]; then
        PATH="${__cafe_dir}:${PATH}"
    fi
done

unset __cafe_dir

