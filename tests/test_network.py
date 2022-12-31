# MIT License
#
# Copyright (c) 2022 University of Oxford
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Test cases for the network functionality for tsutil.
"""
import pytest

import tskit
import tsutil
import tszip

class TestNetwork:

    def test_local_file(self, tmp_path):
        ts = tskit.Tree.generate_balanced(5).tree_sequence
        ts.dump(tmp_path / "test.trees")
        ts2 = tsutil.download("file://" + str(tmp_path / "test.trees"))
        assert ts == ts2

    def test_compressed_local_file(self, tmp_path):
        ts = tskit.Tree.generate_balanced(5).tree_sequence
        tszip.compress(ts, tmp_path / "test.tsz")
        ts2 = tsutil.download("file://" + str(tmp_path / "test.tsz"))
        assert ts == ts2
