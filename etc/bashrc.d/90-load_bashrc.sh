#!/bin/bash

##############################################################################
# CAFE: Organize your Unix packages
# https://github.com/markuskimius/cafe
#
# Copyright (c)2020 Mark K. Kim
# Released under the Apache license 2.0
# https://github.com/markuskimius/cafe/blob/master/LICENSE
##############################################################################

__cafe_sourced=""

function __cafe_source() {
    local __cafe_pkg=$1
    local __cafe_bashrc="${CAFE}/${__cafe_pkg}/etc/bashrc"
    local __cafe_depfile="${CAFE}/${__cafe_pkg}/etc/cafe-deps.json"
    local __cafe_is_sourced=0
    local __cafe_pkg_deps=()
    local __cafe_dep

    # Check whether this package has already been sourced
    if [[ ":${__cafe_sourced}:" == *":${__cafe_pkg}:"* ]]; then
        __cafe_is_sourced=1
    fi

    # Update the sourced list.  Do this early to avoid circular dependency
    if (( ! __cafe_is_sourced )); then
        __cafe_sourced+=":${__cafe_pkg}"
    fi

    # Get the dependency list
    if (( ! __cafe_is_sourced )) && [[ -e "$__cafe_bashrc" ]] && [[ -e "$__cafe_depfile" ]]; then
        local line

        while IFS= read -r line; do
            __cafe_pkg_deps+=( "$line" )
        done < <(jq -r '.[].name' "$__cafe_depfile")
    fi

    # Source the bashrc of the packages it depends on
    for __cafe_dep in "${__cafe_pkg_deps[@]}"; do
        __cafe_source "$__cafe_dep"
    done

    # Source this package's bashrc
    if (( ! __cafe_is_sourced )) && [[ -e "$__cafe_bashrc" ]]; then
        source "$__cafe_bashrc"
    fi
}

function __cafe_sourceall() {
    local __cafe_path
    local __cafe_pkg

    for __cafe_path in "${CAFE}"/*; do
        __cafe_pkg=$(basename "$__cafe_path")

        if [[ "$__cafe_pkg" != "cafe" ]]; then
            __cafe_source "$__cafe_pkg"
        fi
    done
}

__cafe_sourceall

unset __cafe_sourceall
unset __cafe_sourced
unset __cafe_source

