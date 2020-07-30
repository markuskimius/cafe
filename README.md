# cafe
Organize your Unix packages


## What does it do?
Cafe lets you install a Unix package by simply untarring or git-cloning it.
Cafe takes care of setting up the environment, such as `$PATH`, `$PYTHONPATH`,
etc.  To uninstall, simply delete the package directory.


## Assumptions

Cafe assumes all packages are installed under a directory defined by `$CAFE`:

```bash
+-- $CAFE
    +-- cafe
    +-- MYPACKAGE1
    +-- MYPACKAGE2
    +-- MYPACKAGE3
    +-- ...
```

Packages are assumed to have the following layout:

```bash
+-- MYPACKAGE
    +-- bin
    +-- etc
    |   +-- vimrc
    +-- lib
    |   +-- __init__.py      # for python
    |   +-- pkgIndex.tcl     # for tcl
    +-- man
    +-- doc
    +-- ftdetect             # for vim
    +-- plugin               # for vim
    +-- syntax               # for vim
```

Packages that do not have the above layout may be installed by creating a
metpackage.


## Installation
Create a directory where you want to store your packages, git-clone cafe into
it, then source the cafe startup script from your bashrc:

```bash
$ mkdir ~/cafe
$ cd ~/cafe
$ git clone https://github.com/markuskimius/cafe.git
$ echo 'source "${HOME}/cafe/cafe/etc/bashrc"' >> ~/.bashrc
```

`$CAFE` is set by `bashrc` to the parent directory of wherever cafe is installed.


## Support

Cafe currently supports these Unix tools:


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

