#
# This file is part of pySMT.
#
#   Copyright 2014 Andrea Micheli and Marco Gario
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import os
import pytest

from pysmt.logics import QF_LRA
from pysmt.test.smtlib.parser_utils import execute_script_fname, SMTLIB_TEST_FILES, SMTLIB_DIR

def _get_tests():
    for (logic, f, expected_result) in SMTLIB_TEST_FILES:
        smtfile = os.path.join(SMTLIB_DIR, f)
        if logic == QF_LRA:
            yield smtfile, logic, expected_result

@pytest.mark.parametrize("smtfile, logic, expected_result", list(_get_tests()))
def test_qf_lra(smtfile, logic, expected_result):
    execute_script_fname(smtfile, logic, expected_result)
