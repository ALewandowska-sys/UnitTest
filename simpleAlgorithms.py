import pytest

def findMin(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1,len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index


def sort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findMin(arr)
    newArr.append(arr.pop(smallest))
  return newArr


def sumOfDigit(a:int) -> int:
  digit_str = list( str(a) )
  digit_int = [] 
  for digit in digit_str:
      digit_int.append( int(digit) ) 
  
  print( sum(digit_int) )
  

def sum(list):
  if list == []:
   return 0
  return list[0] + sum(list[1:])


class TestResult:
  @pytest.fixture
  def listWithNumbers(self):
    return [4, 9, 11, 30, 2]

  
  def test_find_max(self, listWithNumbers):
    assert findMin(listWithNumbers) == 4

  
  def test_sort(self, listWithNumbers):
    assert sort(listWithNumbers) == [2, 4, 9, 11, 30]

  
  def test_sum_of_digit(self, capsys):
    sumOfDigit(2840)
    out, err = capsys.readouterr()
    assert out == '14\n'
