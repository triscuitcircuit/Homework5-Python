# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

import pytest
import numpy as np
from SortPackage.int_sort import bubble, quick, insertion


def is_sorted(self, int_list):
    """
    Testing oracle. Tests if list is sorted
    """
    if int_list.sort() == self:
        return True
    else:
        return False


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3, 2, 1], [1, 1, 1], np.random.randint(low=-10, high=200, size=5)]


def test_bubble(int_lists):
    for ch in int_lists:
        assert is_sorted(bubble(ch), ch), "Bubble list not sorted"


def test_quick(int_lists):
    for list_to_check in int_lists:
        assert is_sorted(
            quick(list_to_check, -1, 0), list_to_check
        ), "Quick sort list not sorted"


def test_insertion(int_lists):
    for list_to_check in int_lists:
        assert is_sorted(
            insertion(list_to_check), list_to_check
        ), "Insertion list not sorted"
