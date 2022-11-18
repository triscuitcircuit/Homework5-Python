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

"""
This module sorts lists of integers...
"""


def bubble(int_list):
    """
    Args:
        int_list: This is the list of integers to be sorted

    Returns:
        nil
    """

    list_size = len(int_list)
    a_swap_occurred = False

    for i in range(list_size):
        for j in range(0, list_size - i - 1):
            if int_list[j] > int_list[j+1]:
                a_swap_occurred = True
                temp = int_list[j]
                int_list[j] = int_list[j+1]
                int_list[j+1] = temp

        if not a_swap_occurred:
            # simply exit if no swaps were needed - it's already in order
            return

    print("bubble sort")

def quick(int_list):
    """
    Args:
        int_list: This is the list of integers to be sorted

    Returns:
        nil
    """
    print("quick sort")


def insertion(int_list):
    """
    Args:
        int_list: This is the list of integers to be sorted

    Returns:
        nil
    """
    print("insertion sort")

    #git pull
    # add files
    # commit
    # change whatever I need to