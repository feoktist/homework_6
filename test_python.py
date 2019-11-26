# -----------------------------------------
# тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot.
import math
# ------- test map --------------------------
items = [1, 2, 3, 4, 5]

def map_it(your_items):
  squared = list(map(lambda x: x ** 2, your_items))
  return squared

def test_map():
  assert map_it(items) == [1, 4, 9, 16, 25]

print(map_it(items))

# --------- test filter ---------------------
number_list = range(-5, 5)

def filter_it(your_items):
  less_than_zero = list(filter(lambda x: x < 0, your_items))
  return less_than_zero

def test_filter():
  assert filter_it(number_list) == [-5, -4, -3, -2, -1]

print(filter_it(number_list))

# ----------- test sorted ----------------------
nums = [2, 8, 1, 0, -4, -99, 100]

def sort_it(your_stuff):
  brush_it_up = sorted(your_stuff)
  return brush_it_up

def sort_it_reverse(your_stuff):
  reverse_it_up = sorted(your_stuff, reverse = True)
  return reverse_it_up

def test_sorted():
  assert sort_it(nums) == [-99,-4, 0, 1, 2, 8, 100]

def test_reverse_sorted():
  assert sort_it_reverse(nums) == [100, 8, 2, 1, 0, -4, -99]

print(sort_it(nums))
print(sort_it_reverse(nums))

# --------------- math: pi, sqrt, pow, hypot ------------------------
p = math.pi

def your_pi():
  pipi = math.pi
  return pipi

def test_pi():
  assert your_pi() == p

#  = = = = = = = = = = = = = = =
your_num = float(input('Enter your num: '))
your_power = int(input('Enter your pownum: '))

def your_sqrt(your_stuff):
  get_root = math.sqrt(your_stuff) * 1.0
  return get_root

def test_sqrt():
  assert your_sqrt(your_num) == math.sqrt(your_num)

# = = = = = = = = = = = = = = = =
def your_pow(your_stuff, powerof):
  get_pow = math.pow(your_stuff, powerof) * 1.0
  return get_pow

def test_pow():
  assert your_pow(your_num, your_power) == math.pow(your_num, your_power)

# = = = = = = = = = = = = = = = =
your_num1 = float(input('Enter your num1: '))
your_num2 = int(input('Enter your num2: '))
def your_hypot(num1, num2):
  get_hypot = math.hypot(num1, num2) * 1.0
  return get_hypot

def test_hypot():
  assert your_hypot(your_num1, your_num2) == math.sqrt(math.pow(your_num1, 2) + (math.pow(your_num2, 2)))


print(your_hypot(your_num, your_power))