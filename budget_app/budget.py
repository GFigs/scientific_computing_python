class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    return sum(item["amount"] for item in self.ledger)

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    output = self.category.center(30, "*") + "\n"
    for item in self.ledger:
      description = item["description"][:23]
      amount = format(item["amount"], ".2f").rjust(30 - len(description))
      output += f"{description}{amount}\n"
    total = format(self.get_balance(), ".2f")
    output += f"Total: {total}"
    return output





def create_spend_chart(categories):
  spendings = [(category.category, sum(item["amount"] for item in         category.ledger if item["amount"] < 0)) for category in categories]
  total_spent = sum(amount for _, amount in spendings)
  percentages = [int(amount / total_spent * 100) for _, amount in spendings]
  #spendings = sorted(spendings, key = lambda spending : spending[1])
  chart = "Percentage spent by category\n"
  for i in range(100, -1, -10):
      chart += str(i).rjust(3) + "| "
      for percentage in percentages:
          if percentage >= i:
              chart += "o  "
          else:
              chart += "   "
      chart += "\n"

  chart += "    -" + "---" * len(categories)

  max_length = max(len(category) for category, _ in spendings)
  for i in range(max_length):
      chart += "\n"
      chart += "     "
      for category, _ in spendings:
          if i < len(category):
              chart += category[i] + "  "
          else:
              chart += "   "
      
    
  return chart