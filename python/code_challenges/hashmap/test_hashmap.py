import pytest
from hash_map import HashTable

hash_table = HashTable()


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


def test_retrieving_based_on_existing_key(tester):
    # arranged -> add("key", "value")
    # actual
    actual = hash_table.get("key")
    # expected
    expected = "value"
    # assert
    tester(actual, expected)


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
    actual = hash_table.contains("key")
    # expected
    expected = True
    # assert
    assert actual == expected


def test_retrieve_value_within_hashtable_has_collision(tester):
    # arranged -> add("yek", "another_Value")
    actual = hash_table.get("yek")
    # expected -> list of values extracted from the nodes.
    expected = "another_Value"
    # Assert
    tester(actual, expected)


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


