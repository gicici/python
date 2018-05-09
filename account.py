class Account(object):

	def __init__(self,holder,number,balance,credit_line = 1600):
		self.holder = holder
		self.number = number
		self.balance = balance
		self.credit_line = credit_line
	def deposit(self, amount):
		self.balance = amount
	def withdraw(self,amount):
		if(self.balance -amount < -self.credit_line):
			return False
		else:
			self.balance -=amount
			return True
	def balance(self):
		return self.balance
	def transfer(self,target,amount):
		if(self.balance -amount < -self.credit_line):
			return False
		else:
			self.balance -=amount
			self.target +=amount
			return True

k = Account('Lucy' ,345267,10009.78)
print(k)

		