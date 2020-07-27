#!/bin/bash

##############################################################################
# CAFE: Organize your Unix packages
# https://github.com/markuskimius/cafe
#
# Copyright (c)2020 Mark K. Kim
# Released under the Apache license 2.0
# https://github.com/markuskimius/cafe/blob/master/LICENSE
##############################################################################

for __cafe_file in "${CAFE}"/*/etc/bashrc; do
    if ! [[ "$__cafe_file" -ef "${CAFE}/cafe/etc/bashrc" ]]; then
        source "$__cafe_file"
    fi
done

unset __cafe_file

