'''CAFE: Organize your Unix packages
  
https://github.com/markuskimius/cafe
'''

import os
from glob import glob

__copyright__ = 'Copyright 2021 Mark Kim'


##############################################################################
# FUNCTIONS

def find(filepattern, basedir='.', subdir='*'):
    '''Find a file using a glob pattern.  The pattern may specify an absolute
    path pattern, relative path pattern (whose base directory may be changed by
    setting `basedir`), otherwise the file is searched for in $CAFE/*/subdir.
    '''
    is_absolute = filepattern.startswith(os.path.sep)
    is_relative = os.path.sep in filepattern and not is_absolute
    CAFE = os.getenv('CAFE')

    if   is_absolute : pass
    elif is_relative : filepattern = os.path.join(basedir, filepattern)
    elif CAFE        : filepattern = os.path.join(CAFE, '*', subdir, filepattern)

    return glob(filepattern, recursive=True)


def merge_dict(*dicts):
    '''Merge multiple dictionaries into a new dictionary.  On key collision,
    any values of type 'dict' are recursively merged, 'list' are appended, and
    any other are overwritten by the latter dictionary's instance.
    '''
    merged = {}

    for d in dicts:
        # Ensure it is a dictionary
        if   isinstance(d, dict)  : pass
        elif isinstance(d, list)  : d = { 'list'  : d }
        elif isinstance(d, str)   : d = { 'str'   : d }
        elif isinstance(d, int)   : d = { 'int'   : d }
        elif isinstance(d, float) : d = { 'float' : d }
        elif isinstance(d, bool)  : d = { 'bool'  : d }
        else                      : d = {  None   : d }

        for k in d:
            if   k in merged and isinstance(merged[k], dict) : merged[k] = merge_dict(merged[k], d[k])
            elif k in merged and isinstance(merged[k], list) : merged[k] = merge_list(merged[k], d[k])
            else                                             : merged[k] = d[k]

    return merged


def merge_list(*lists):
    '''Merge multiple lists into a new list.
    '''
    merged = []

    for l in lists:
        # Ensure it is a list
        if not isinstance(l, list) : l = [l]

        merged += l

    return merged

