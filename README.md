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

Cafe also assumes the package has the following layout:

```bash
+-- MYPACKAGE
    +-- bin
    +-- etc
    |   +-- vimrc
    +-- lib
        +-- __init__.py
        +-- pkgIndex.tcl
```


## Support

Cafe currently supports these Unix tools:

* bash
* python
* tclsh
* vim


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


## License

[Apache 2.0]


[Apache 2.0]: <https://github.com/markuskimius/cafe/blob/master/LICENSE>

