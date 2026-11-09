class Client:
  def __init__(self, name, balance): #створюємо самого клієнта, його ім'я та баланс
    self.name = name
    self.balance = balance
  def get_name(self): #повертаємо ім'я клієнта
    return self.name
  def get_balance(self):  #повертає баланс клієнта
    return self.balance
  def money_paid(self, amount): #показуємо яку ксть грошей списали=заплатили з рахунку клієнта(оплачено = true, не оплачено = false)
    if amount > self.balance:
      return False
    self.balance -= amount
    return True
