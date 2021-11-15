from merge_sort import merge_sort


def test_zero_length_list():
    # Arrange
    lst = []
    # Act
    actual = merge_sort(lst)
    # Expected
    expected = []
    # Assert
    assert actual == expected


def test_length_is_one():
    # Arrange
    lst = [1]
    # Act
    actual = merge_sort(lst)
    # Expected
    expected = [1]
    # Assert
    assert actual == expected


def test_list():
    # Arrange
    lst = [8, 4, 23, 42, 16, 15]
    # Act
    actual = merge_sort(lst)
    # Expected
    expected = [8, 4, 23, 42, 16, 15]
    # Assert
    assert actual == expected


def test_list_with_negative_element():
    # Arrange
    lst = [20, 18, 12, 8, 5, -2]
    # Act
    actual = merge_sort(lst)
    # Expected
    expected = [20, 18, 12, 8, 5, -2]
    # Assert
    assert actual == expected


def test_list_dublicate_elements():
    # Arrange
    lst = [5, 12, 7, 5, 5, 7]
    # Act
    actual = merge_sort(lst)
    # Expected
    expected = [5, 12, 7, 5, 5, 7]
    # Assert
    assert actual == expected


def test_list_nearly_sorted():
    # Arrange
    lst = [2, 3, 5, 7, 13, 11]
    # Act
    actual = merge_sort(lst)
    # Expected
    expected = [2, 3, 5, 7, 13, 11]
    # Assert
    assert actual == expected
