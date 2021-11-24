import inspect
import os
import sys

# region imports requirements
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
# endregion

from hashmap.hash_map import HashTable


def left_join(left_map: HashTable, right_map: HashTable) -> list:
    # region docs
    """[summary]
    LEFT JOINs two hashmaps into a single data structure.

    Args:
        left_map (Hashable): Hashmap class instance
        right_map (Hashable): Hashmap class instance

    Returns:
        list: containing the key,value of left_map and if any value match the key in right_map Or None
    """
    # endregion

    left_joind_right_values = []
    for linked_list in left_map._HashTable__buckets:
        if linked_list is not None:

            current = linked_list.head

            key = current.value[0]
            values = current.value[1]

            if right_map.contains(key):

                right_value = right_map.get(key)
                values.append(right_value[0])

            left_joind_right_values.append([key, values])

    return left_joind_right_values
