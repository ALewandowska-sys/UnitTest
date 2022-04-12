import math
import pytest


class SomeError(Exception):
  pass


def  pierwiastki(a:int, b:int, c:int):
  if a == 0:
      raise SomeError("Your a is 0, but it can't")
    
  delta = ((b ** 2) - (4 * a * c))
  
  if delta == 0:
    x = (-b) / ( 2 * a ) 
    return x  
  
  elif delta > 0:
    pierwiastek = math.sqrt(delta) 
    x1 = ( - b  - pierwiastek) / ( 2 * a )
    x2 = ( - b  + pierwiastek) / ( 2 * a )
    return x1, x2
    
  elif delta < 0:
    return 0


def test_pierwiastki():
  with pytest.raises(SomeError):
    pierwiastki(0, 3, 0)
  assert pierwiastki(4, 1, 4) == 0
  assert pierwiastki(1, 4, 4) == -2
  assert pierwiastki(1, 4, 3) == (-3 , -1)
