# cafe

Organize your Unix packages


## What does it do?

Cafe lets you install a Unix package by simply untarring or git-cloning it.
Cafe takes care of setting up the environment, such as `$PATH`, `$PYTHONPATH`,
etc.  To uninstall, simply delete the package directory.


## Assumptions

Packages are assumed to be installed under `$CAFE`:

```bash
+-- $CAFE
    +-- cafe (this package)
    +-- MYPACKAGE1
    +-- MYPACKAGE2
    +-- MYPACKAGE3
    +-- ...
```

Each package is assumed to have the following layout:

```bash
+-- MYPACKAGE
    +-- bin
    +-- etc
    |   +-- bashrc           # startup script
    |   +-- vimrc            # vim startup script
    |   +-- cafe-deps.json   # dependencies
    +-- lib
    |   +-- __init__.py      # python package
    |   +-- pkgIndex.tcl     # tcl package
    +-- man
    +-- doc
    +-- ftdetect             # vim package
    +-- plugin               # vim package
    +-- syntax               # vim package
```

Packages that do not have the above layout may be installed by creating a
metpackage.


## Requirements

Cafe requires:

* bash
* git
* jq
* python
* GNU readlink (in coreutils)
* enhanced getopt (in getopt or util-linux)


## Installation

Create a directory where you want to store your packages, git-clone cafe into
it, then source the cafe startup script from your bashrc:

```bash
$ mkdir ~/cafe
$ cd ~/cafe
$ git clone https://github.com/markuskimius/cafe.git
$ echo 'source "${HOME}/cafe/cafe/etc/bashrc"' >> ~/.bashrc
```

`$CAFE` is set by `cafe/etc/bashrc` to the parent directory of wherever cafe is installed.


## Usage

Cafe comes with following commands to simplify package management:

* `cafe install-git URL [PKGNAME]` - Installs `PKGNAME` from `URL` into
  `$CAFE` using `git clone`.  Also installs any dependencies required by
  `PKGNAME` if `PKGNAME` has `etc/cafe-deps.json`.
* `cafe install-deps [PKGNAME]` - Installs dependencies of `PKGNAME`.  If `PKGNAME` is
  omitted, installs the dependencies of all installed packages.
* `cafe update [PKGNAME]` - Updates `PKGNAME` and its dependencies.  If `PKGNAME` is
  omitted, updates all installed packages.


## Support

Cafe currently supports setting up the Unix environment for use with the
following:

### bash

* `MYPACKAGE/etc/bashrc`, if exists, is sourced at bash startup.
* `MYPACKAGE/bin` is added to `$PATH`.


### python

* `MYPACKAGE/lib` is added to `$PYTHONPATH` if it contains `__init__.py`.


### tcl

* `MYPACKAGE/lib` is added to `$TCLLIBPATH` if it contains `pkgIndex.tcl`.


### vim (version 8+)

* `MYPACKAGE/etc/vimrc`, if exists, is sourced at vim startup.
* `MYPACKAGE/{ftdetect,plugin,syntax,doc}` are loaded or made loadable.

cafe accomplishes the above by creating bash aliases `{vim,view,vimdiff,gvim}`
that source `$CAFE/cafe/etc/vimrc` at startup.  If your vim is already aliased,
add the `-u "$CAFE/cafe/etc/vimrc"` option to your alias to ensure the above
are actioned.


## License

[Apache 2.0]


[Apache 2.0]: <https://github.com/markuskimius/cafe/blob/master/LICENSE>

