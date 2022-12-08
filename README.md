# tsutil

This library provides various functions that are useful for users working with
tree sequences in Python. Note that the core [tskit](https://github.com/tskit-dev/tskit)
library already contains a large amount of built-in functionality via its
[Python API](https://tskit.dev/tskit/docs/stable/python-api.html): the `tsutil` package
aims to collect supplementary functions which are inappropriate to
include in `tskit`, for example because they require other software packages
which the developers do not want to list as core dependencies. These include routines to
generate plots of standard tree sequence summary measures (e.g., to help check
on the quality of inferred tree sequences), or to help
download tree sequence files from online repositories.

Functions in this library are intended to provide simple and useful defaults for users
who want to get going quickly, e.g. when dealing with tree sequences in tutorials or
performing basic exploratory analysis. For more complex functionality, users are
encouraged to develop their own functions. The [tutorials](https://tskit.dev/tutorials/)
are a good place to develop an understanding: for support in developing your own
functionality, or to contribute to this repository, you can ask the general
[tskit community](https://tskit.dev/community/).

Note that current versions of this library are not guaranteed to be
backwards-compatibility with older versions, nor produce identical outputs.