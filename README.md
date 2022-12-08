# tsutil

This library provides various functions that are useful for users working with
tree sequences in Python. Note that the core [tskit](https://github.com/tskit-dev/tskit)
library already contains a large amount of build-in functionality via its
[Python API](https://tskit.dev/tskit/docs/stable/python-api.html): the `tsutil` package
aims to collect supplementary functions which are inappropriate to include in the core
library, for example routines to generate default quality (QC) plots, or to aid
in downloading tree sequence files from online repositories.

Functions in this library are intended to provide simple and useful defaults for users
who want to get going quickly, e.g. when dealing with tree sequences in tutorials or
performing basic exploratory analysis. For more complex functionality, users are
encouraged to develop their own functions. The [tutorials](https://tskit.dev/tutorials/)
are a good place to develop an understanding: for support in developing your own
functionality, or to contribute to this repository, you can ask the general
[tskit community](https://tskit.dev/community/).

Note that new versions of this library are not guaranteed to maintain
backwards-compatibility with older versions, nor produce identical outputs.