import pytest
from stack_queue_brackets import validate_brackets

valid_pattern_list = ['{}(){}','{}','(){}[[]]','{}{Code}[Fellows](())','()[[Extra Characters]]']
invalid_pattern_list = ['{(})','(](','{{} )]','[({}]']

# chech for valid pattern
def test_valid_brackets_balance():
  # Arrange
  all_valid = list()

  for pat in valid_pattern_list:
      all_valid.append(validate_brackets((pat)))

  #Expected
  expected = len(valid_pattern_list)
  # Actual
  actual = sum(all_valid)
  # Assert
  assert actual == expected


# chech for invalid pattern
def test_invalid_brackets_balance():
  # Arrange
  all_valid = list()

  for pat in invalid_pattern_list:
      all_valid.append(validate_brackets((pat)))

  #Expected
  expected = 0
  # Actual
  actual = sum(all_valid)
  # Assert
  assert actual == expected
