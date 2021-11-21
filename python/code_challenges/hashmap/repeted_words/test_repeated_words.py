from .repeated import repeated_word


def test_repeated_multible_words_returns_first_repeated_word_1():
    string = "Once upon a time, there was a brave princess who..."
    # actual
    actual = repeated_word(string)
    # expected
    expected = "a"
    # assert
    assert actual == expected


def test_repeated_multible_words_returns_first_repeated_word_2():
    string = (
        "It was the best of times, it was the worst of times,"
        + "it was the age of wisdom, it was the age of foolishness,"
        + "it was the epoch of belief,"
    )
    # arrange
    actual = repeated_word(string)
    # expected
    expected = "it"
    # assert
    assert actual == expected


def test_repeated_multible_words_returns_first_repeated_word_3():
    string = (
        "It was a queer, sultry summer, the summer they,"
        + "electrocuted the Rosenbergs, and I didn’t know "
        + "what I was doing in New York..."
    )
    # actual
    actual = repeated_word(string)
    # expected
    expected = "summer"
    # assert
    assert actual == expected


def test_repeated_multible_words_returns_first_repeated_word_4():
    string = "and she asked me, What's your name? i told her my name and i ...."

    # actual
    actual = repeated_word(string)
    # expected
    expected = "name"
    # assert
    assert actual == expected
