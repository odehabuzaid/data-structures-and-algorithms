import pytest

from hash_map import HashTable


@pytest.fixture
def hashtable():
    return HashTable()


def test_hash(hashtable):
    expected = 700
    actual = hashtable._HashTable__hash("d")
    assert actual == expected


def test_hash_word(hashtable):
    expected = 376
    actual = hashtable._HashTable__hash("dd")
    assert actual == expected


def test_add(hashtable):
    hash_table = HashTable()
    actual = hashtable._HashTable__size
    expected = 1024
    assert actual == expected

    hash_table.add("key", "value")

    actual = hash_table.contains("key")
    expected = True
    assert actual == expected

    actual = hash_table.get("key")
    expected = "value"
    assert actual == expected

    actual = hash_table.contains("key_not_there")
    expected = None
    assert actual == expected


"""
"a"
ord("d") = 100
100 * 7 = 700
700 % 1024 = 700

-----------------
"dd"
200
200 * 7 = 1400
1400 % 1024 = 376
"""
