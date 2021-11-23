import inspect
import os
import sys

# region imports requirements
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
# endregion

from hashmap.hash_map import HashTable


def left_join(map1: HashTable, map2: HashTable) -> list:
    # region docs
    """[summary]
    LEFT JOINs two hashmaps into a single data structure.

    Args:
        map1 (Hashable): Hashmap class instance
        map2 (Hashable): Hashmap class instance

    Returns:
        list: containing the key,value of map1 and if any value match the key in map2 Or None
    """
    # endregion

    pass
