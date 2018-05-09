def is_isogram(word):
	lst =[a for a in word]
	clear = set(lst)
	if len(lst) == len(clear):
		return True
		return False

print(is_isogram('Lucy'))








class ShoppingCart(object):
  
  
  def __init__(self):
    self.total=0
    self.items={}
  
  def add_item(self, item_name, quantity, price):
    self.total = self.total+ (price*quantity)
    self.items[item_name]= quantity
  
  def remove_item(self, item_name, quantity, price):
    if quantity < self.items[item_name]:
      self.total=self.total-(price * quantity)
      self.items[item_name] = self.items[item_name]-quantity
    else:
      self.total=self.total-(self.items[item_name]*price)
      del self.items[item_name]
  
  def checkout(self, cash_paid):
    if cash_paid < self.total:
      return "Cash paid not enough"
    
    return  cash_paid- self.total
    
class Shop(ShoppingCart):
  def __init__(self):
    self.quantity=100
  def remove_item(self, *args):
    try:
      args[0]
    except:
      self.quantity-= 1
    
    
    def remove_duplicates(word):
  lst= set(word)
  strt_list = sorted(lst) 
  joined_list = "".join(strt_list)
  no_duplicates = len(word) - len(joined_list)
  return (joined_list, no_duplicates)
    def my_sort(numbers):
  odd_numbers= []
  even_numbers =[]
  for num in numbers:
    if num % 2 == 0:
      even_numbers.append(num)
    else:
      odd_numbers.append(num)
  sort_odd =sorted(odd_numbers)
  sort_even =sorted(even_numbers)
  return sort_odd + sort_even

  def power(a,b):
  return a**b



  def longest(longest_word):
  b = longest_word.split(' ')
  return max(b, key=len)