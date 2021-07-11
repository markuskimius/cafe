'''CAFE: Organize your Unix packages
  
https://github.com/markuskimius/cafe
'''

import os
import sys
import json
import cafe_util
import cafe_error

__copyright__ = 'Copyright 2021 Mark Kim'


##############################################################################
# PUBLIC

CAFE = os.getenv('CAFE', '.')
CAFE_WORKDIR = os.getenv('CAFE_WORKDIR', '.')
INDENT = None

def create(filepattern=None):
    cfg = CafeCfg()

    if filepattern is not None:
        cfg.open(filepattern)

    return cfg


##############################################################################
# CLASSES

class CafeCfg:
    def __init__(self):
        self.node = JsonNode()
        self.sources = []

    def open(self, filepattern, cwd=None):
        for filename in cafe_util.find(filepattern, subdir='etc'):
            with open(filename) as f:
                json_data = json.load(f)
                self.merge(json_data)
                self.sources += [filename]

        return self

    def merge(self, json_data):
        self.node.merge(json_data)

        return self

    def enter(self, path):
        self.node = self.node.enter(path)

        return self

    def exit(self):
        self.node = self.node.parent

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.exit()

    def names(self):
        return self.node.names()

    def get(self, name, default=None):
        return self.node.get(name, default)

    def __getitem__(self, name):
        return self.node[name]

    def __str__(self):
        return str(self.node)


class JsonNode:
    def __init__(self, json_data=None, path=[], parent=None):
        self.json = json_data
        self.path = path
        self.parent = parent

    def merge(self, json_data):
        if   self.json is None           : self.json = json_data
        elif isinstance(self.json, dict) : self.json = cafe_util.merge_dict(self.json, json_data)
        elif isinstance(self.json, list) : self.json = cafe_util.merge_list(self.json, json_data)
        else                             : self.json = json_data

        if self.path:
            last = self.path[-1]
            self.parent.json[last] = self.json

        return self

    def enter(self, name):
        next_json = self.json[name]
        next_path = self.path + [name]

        return JsonNode(next_json, path=next_path, parent=self)

    def names(self):
        return self.json.keys()

    def items(self):
        return self.json.items()

    def get(self, name=None, default=None):
        if name is None : return self.json
        else            : return self.json.get(name, default)

    def __getitem__(self, name):
        return self.json[name]

    def __str__(self):
        separators = (',', ':') if INDENT is None else None  # Compact output if INDENT is None

        return json.dumps(self.json, separators=separators, indent=INDENT)


##############################################################################
# ENTRY POINT

if __name__ == '__main__':
    cfg = create()

    for filename in sys.argv[1:]:
        cfg.open(filename)

    print(cfg)

