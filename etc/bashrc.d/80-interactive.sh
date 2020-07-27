#!/bin/bash

##############################################################################
# CAFE: Organize your Unix packages
# https://github.com/markuskimius/cafe
#
# Copyright (c)2020 Mark K. Kim
# Released under the Apache license 2.0
# https://github.com/markuskimius/cafe/blob/master/LICENSE
##############################################################################

# This script runs only in interactive mode
[[ "$-" == *i* ]] || return

alias vim='vim -u "${CAFE}/cafe/etc/vimrc"'
alias view='vim -Ru "${CAFE}/cafe/etc/vimrc"'
alias vimdiff='vim -du "${CAFE}/cafe/etc/vimrc"'
alias gvim='gvim -u "${CAFE}/cafe/etc/vimrc"'

