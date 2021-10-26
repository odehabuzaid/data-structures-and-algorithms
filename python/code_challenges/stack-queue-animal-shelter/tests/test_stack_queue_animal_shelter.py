import pytest
from stack_queue_animal_shelter import __version__, queue
from stack_queue_animal_shelter.shelter import AnimalShelter


def test_version():
    assert __version__ == '0.1.0'

shelter = AnimalShelter()

def test_animal_shelter_enqueue():
    # actual output
    actual = shelter.dog.front.data
    # Assert
    expected = "dog"
    assert actual == expected

def test_upper_case():
    # Arrange any data that you need to run your test
    shelter.enqueue("CAT")
    shelter.enqueue("DOG")
    # actual output
    actual = shelter.dequeue("CAT")
    # Assert
    expected = "cat"
    assert actual == expected

def test_animal_shelter_dequeue_cat():
    # actual output
    actual = shelter.dequeue("cat")
    # Assert
    expected = "cat"
    assert actual == expected

def test_animal_shelter_dequeue_dog():
    # actual output
    actual = shelter.dequeue("dog")
    # Assert
    expected = "dog"
    assert actual == expected

def test_animal_shelter_dequeue_other_animal():
    # actual output
    actual = shelter.dequeue()
    # Assert
    expected = 'rabbit'
    assert actual != expected

@pytest.fixture(autouse=True)
def arrange():
    for _ in range(5):
        shelter.enqueue("cat")
        shelter.enqueue("dog")

    waiting_animals = ['rabbit','parrot','goat','hamster','kaggle']
    for animal in waiting_animals:
        shelter.enqueue(animal)

