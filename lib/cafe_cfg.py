'''CAFE: Organize your Unix packages
  
https://github.com/markuskimius/cafe
'''

import os
import sys
import json
import cafe_util

__copyright__ = 'Copyright 2021 Mark Kim'


##############################################################################
# PUBLIC

CAFE = os.getenv('CAFE', '.')
CAFE_WORKDIR = os.getenv('CAFE_WORKDIR', '.')
INDENT = None

def create(filepattern=None):
    cfg = CafeCfg()
    cfg.add_filter(ImportFilter())

    if filepattern is not None:
        cfg.open(filepattern)

    return cfg


##############################################################################
# CLASSES

class CafeCfg:
    def __init__(self):
        self.node = JsonNode()
        self.filters = []

    def add_filter(self, filter):
        self.filters += [filter]

    def open(self, filepattern, cwd=None):
        cwd = os.getcwd()

        for filename in cafe_util.find(filepattern, subdir='etc'):
            # chdir to the filename's directory so we can import files relative to its path
            filename = os.path.abspath(filename)
            dirname = os.path.dirname(filename)
            os.chdir(dirname)

            with open(filename) as f:
                json_data = json.load(f)
                self.merge(json_data)

        os.chdir(cwd)

        return self

    def merge(self, json_data):
        # Filter the data
        for f in self.filters:
            json_data = f(json_data)

        # Merge the data
        if json_data is not None:
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
        self.json = cafe_util.merge_json(self.json, json_data)

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


class ImportFilter:
    def __call__(self, json_data):
        if isinstance(json_data, dict):
            imported = None

            for k,v in json_data.items():
                if k == '#import' : imported = self.open(v)
                else              : json_data[k] = self.__call__(v)

            if imported is not None:
                del json_data['#import']

                if json_data : json_data = cafe_util.merge_dict(json_data, imported)
                else         : json_data = imported

        elif isinstance(json_data, list):
            for i,v in enumerate(json_data):
                json_data[i] = self.__call__(v)

        return json_data

    def open(self, filepattern):
        merged = None
        cwd = os.getcwd()

        for filename in cafe_util.find(filepattern, subdir='etc'):
            # chdir to the filename's directory so we can import files relative to its path
            filename = os.path.abspath(filename)
            dirname = os.path.dirname(filename)
            os.chdir(dirname)

            with open(filename) as f:
                json_data = json.load(f)
                json_data = self.__call__(json_data)

                merged = cafe_util.merge_json(merged, json_data)

        os.chdir(cwd)

        return merged


##############################################################################
# ENTRY POINT

if __name__ == '__main__':
    cfg = create()

    for filename in sys.argv[1:]:
        cfg.open(filename)

    print(cfg)

