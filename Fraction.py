from Binary_Search_Tree import Binary_Search_Tree

class Fraction:

  def __init__(self, numerator, denominator):
    # use caution here... In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  #the __lt__ method runs in constant time as it uses the numerator and denominator attributes stored in each fraction node to cross multiplty and then compare the fractions to see if self is less than other 
  def __lt__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self is less than other and
    #False otherwise. Recall that floating-point
    #representation is imprecise. Use cross-
    #multiplication to remain in the integer domain.
    selfNumeratorCopy = self.__n
    otherNumeratorCopy = other.__n
    crossMultipleSNC = selfNumeratorCopy * other.__d
    crossMultipleONC = otherNumeratorCopy * self.__d
    if crossMultipleSNC < crossMultipleONC:
      return True
    else:
      return False

  #the __gt__ method runs in constant time as it uses the numerator and denominator attributes stored in each fraction node to cross multiply and then compare the fractions to see if self is greater than other 
  def __gt__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self is greater than other and
    #False otherwise. Recall that floating-point
    #representation is imprecise. Use cross-
    #multiplication to remain in the integer domain.
    selfNumeratorCopy = self.__n
    otherNumeratorCopy = other.__n
    crossMultipleSNC = selfNumeratorCopy * other.__d
    crossMultipleONC = otherNumeratorCopy * self.__d
    if crossMultipleSNC > crossMultipleONC:
      return True
    else:
      return False

  #the __eq__ method runs in contant times as it uses the numerator and enominator attirbutes stored in each fraction node to cross multiply and then compare the fractions to see if self is equivalent to other
  def __eq__(self, other):
    #TODO replace pass with your implementation,
    #returning True if self equal to other and
    #False otherwise. Note that fractions are
    #stored in reduced form. Recall that floating-point
    #representation is imprecise. Use cross-
    #multiplication to remain in the integer domain.
    selfNumeratorCopy = self.__n
    otherNumeratorCopy = other.__n
    crossMultipleSNC = selfNumeratorCopy * other.__d
    crossMultipleONC = otherNumeratorCopy * self.__d
    if crossMultipleSNC == crossMultipleONC:
      return True
    else:
      return False

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':
  #TODO create a bunch of fraction objects and store them in an array.
  #Then insert each item from the array into a balanced BST.
  #Then get the in-order array representation of the BST using
  #the new to_list() method, which you must implement.
  #print the original and in-order traversal arrays to show that
  #the fractions have been sorted.
  fracArr = []
  a = Fraction(4,5)
  b = Fraction(1,2)
  c = Fraction(9,13)
  d = Fraction(3,4)
  e = Fraction(5,6)
  f = Fraction(6,7)
  g = Fraction(7,8)
  h = Fraction(3,8)
  i = Fraction(5,8)
  j = Fraction(4,9)
  k = Fraction(2,9)
  l = Fraction(5,7)
  m = Fraction(1,8)
  n = Fraction(2,7)
  o = Fraction(3,5)
  p = Fraction(4,7)
  q = Fraction(8,9)
  r = Fraction(9,10)
  s = Fraction(7,11)
  t = Fraction(5,13)
  fracArr.append(a)
  fracArr.append(b)
  fracArr.append(c)
  fracArr.append(d)
  fracArr.append(e)
  fracArr.append(f)
  fracArr.append(g)
  fracArr.append(h)
  fracArr.append(i)
  fracArr.append(j)
  fracArr.append(k)
  fracArr.append(l)
  fracArr.append(m)
  fracArr.append(n)
  fracArr.append(o)
  fracArr.append(p)
  fracArr.append(q)
  fracArr.append(r)
  fracArr.append(s)
  fracArr.append(t)
  print(fracArr)
  leBST = Binary_Search_Tree() 
  for i in fracArr:
    leBST.insert_element(i)
  print(leBST.in_order())


