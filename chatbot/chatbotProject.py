# Define your functions
def coffee_bot():

  print("Welcome to the cafe!")
  name = input("Can I get your name please? ")

  size = get_size()
  drink_type = get_drink_type()

  print("Alright, that's a {} {}!".format(size, drink_type))
  print("Thanks {}! Your drink will be ready shortly. /n".format(name))

  extra_order()

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \nPlease enter the corresponding letter for your response. \n")
  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else: 
    print_message()
    return get_size()


def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n Please enter the corresponding letter for your response. \n")
  if res == 'a':
    return "Brewed"
  elif res == 'b':
    return "Mocha"
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()


def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n Please enter the corresponding letter for your response. \n")
  if res == "a":
    return "Latte with 2% milk"
  elif res == "b":
    return "Latte with Non-fat milk"
  elif res == "c":
    return "Latte with Soy milk"
  else:
    print_message()
    return order_latte()


def extra_order():
  res = input("Do you need another cup of coffee? \n[a] Yes \n[b] No \nPlease enter the corresponding letter for your response.\n")
  if res == "a":
    return get_size(), get_drink_type(), extra_order()
  elif res == "b":
    print("That's great, I wish you a great day!")
  else:
    print_message()
    return extra_order()

# Call coffee_bot()!
coffee_bot()