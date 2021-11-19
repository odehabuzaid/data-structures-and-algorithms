import pytest
from hash_map import HashTable

hash_table = HashTable()

# no need ,
@pytest.fixture
def tester():
    return assert_generator_values


def test_add_key_value_to_hashtable():
    # arrange
    hash_table.add("key", "value")
    # actual
    actual = hash_table.contains("key")
    # expected
    expected = True
    # assert
    assert actual == expected


def test_retrieving_based_on_existing_key():
    # arranged -> add("key", "value")
    # actual
    actual = list(hash_table.get("key"))
    # expected
    expected = ["value"]
    # assert
    assert actual == expected


def test_retrieving_based_on_not_existing_key():
    # actual
    actual = hash_table.contains("key_not_there")
    # expected
    expected = None
    # assert
    assert actual == expected


def test_successfully_handle_collision_within_hashtable():
    # arrange
    # add key,value ->
    # Where the key hashes to the same index of another key
    # 'key' hashed index -> 255
    # 'yek' hashed index -> 255

    hash_table.add("yek", "another_Value")
    # actual
    actual = hash_table.contains("yek")
    # expected
    expected = True
    # assert
    assert actual == expected


def test_retrieve_value_within_hashtable_has_collision():
    # arranged -> add("yek", "another_Value")
    actual = list(hash_table.get("yek"))
    # expected -> list of values extracted from the nodes.
    expected = ["another_Value"]
    # Assert
    assert actual == expected


def test_hash_to_in_range_value():
    # actual
    actual = hash_table._HashTable__hash("the_quick_brown_fox_jumps_over_the_lazy_dog")
    # expected
    expected = 407
    # assert
    assert actual == expected

    expected = 700
    actual = hash_table._HashTable__hash("d")
    assert actual == expected


"""
HashMap can be used to store key-value pairs.
But sometimes you may want to store multiple values for the same key.

For example:

For Key A, you want to store - Apple, Aeroplane

For Key B, you want to store - Bat, Banana

For Key C, you want to store – Cat, Car
"""


def test_retrieving_based_on_existing_key_added_multible_times():
    # arranged
    hash_table.add("C", "Car")
    hash_table.add("C", "Cat")
    # actual
    actual = list(hash_table.get("C"))
    # expected
    expected = ["Cat", "Car"]
    # assert
    assert actual == expected


# no need ,
def assert_generator_values(actual, expected):
    """
    function to assert values from HashTable generator (get) method

    Args:
        actual ([generator]): [description]
        expected ([type]): [description]
    """
    actual = list(actual)

    # case : if the bucket contains one node
    if len(actual) == 1:
        assert actual[0] == expected
        return

    # case : if the bucket contains more than one node
    # ( same key different values )
    for idx, value in enumerate(actual):
        assert value == expected[idx]

    # case None will pass since no assert statement applied to expect it.
