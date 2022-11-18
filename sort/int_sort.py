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
    This function takes a list and sorts it by comparing each element to the
    following element, swapping them when nescessary

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

def partition(int_list, left_index, right_index):
    """
    This function partitions the list around its last element.
    As in, the list is modified so that every element less than the
    last element is on the left of the last element, and every element
    greater than the last element is on the right. The position of
    the last element (the pivot point) after the list
    is modified is returned

    Args:
        int_list: This is the list of integers to be sorted
        left_index: The leftmost index of the given list
        right_index: The rightmost index of the given list

    Returns:
        partition_index: The position of the pivot point after modification
    """

    pivot_point = int_list[right_index]
    compare_ptr = left_index - 1

    for i in range(left_index, right_index):
        if int_list[i] <= pivot_point:
            compare_ptr+=1
            temp = int_list[compare_ptr]
            int_list[compare_ptr] = int_list[i]
            int_list[i] = temp

    temp = int_list[compare_ptr+1]
    int_list[compare_ptr+1] = int_list[right_index]
    int_list[right_index] = temp

    partition_index = compare_ptr + 1

    return partition_index
        
def quick(int_list, left_index, right_index):
    """
    Args:
        int_list: This is the list of integers to be sorted
        left_index: The leftmost index of the given list
        right_index: The rightmost index of the given list

    Returns:
        nil
    """
    if left_index < right_index:
        partition_index = partition(int_list, left_index, right_index)

        quick(int_list, left_index, partition_index - 1) # left of pivot
        quick(int_list, partition_index + 1, right_index) # right of pivot

    print("quick sort")

def insertion(int_list):
    """
    This function loops over the list, comparing each element to the next one,
    inserting the next element in its proper position if it is out of order

    Args:
        int_list: This is the list of integers to be sorted

    Returns:
        nil
    """

    for i in range(1, len(int_list)):
        current = int_list[i]
        j = i - 1

        while current < int_list[j] and j >= 0:
            int_list[j + 1] = int_list[j]
            j-=1

        int_list[j + 1] = current

    print("insertion sort")