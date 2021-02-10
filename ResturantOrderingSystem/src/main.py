class MenuItem:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost
  
total_cost = 0.0

sandwichs = [MenuItem("chicken", 5.25), MenuItem("beef", 6.25), MenuItem("tofu", 5.75)]
beverages = [MenuItem("small", 1.0), MenuItem("medium", 1.75), MenuItem("large", 2.25)]
fries = [MenuItem("small", 1.0), MenuItem("medium", 1.50), MenuItem("large", 2.0)]
ketchup_packet_cost = 0.25

orders = []

def cycle_menu_item(menu_item, input_name, command):
    for item in menu_item:
        if(item.name == input_name):
            print(command + item.name + " Cost: " + str(item.cost))
            return item.cost
    return -1.0

def ask_for_sandwitch(user_orders = list):
    sandwich_type = input("What sandwich would you like: (chicken $5.25, beef $6.25, tofu $5.75)")
    found = cycle_menu_item(sandwichs, sandwich_type, "Sandwich selected: ")
    if(found != -1.0):
        user_orders.append(MenuItem(sandwich_type, found))
        return found
    print("No sandwich selected!")
    return 0.0

def yes_or_no_question(command_to_ask):
    answer = input(command_to_ask)
    return (answer == "yes")

def ask_for_beverage(user_orders = list):
  want_beverage = yes_or_no_question("Would you like a beverage?")
  if(want_beverage):
    beverage_type = input("What beverage? ($small 1.0, $medium 1.75, large, $2.25)")
    found = cycle_menu_item(beverages, beverage_type, "Beverage selected: ")
    if(found != -1.0):
        user_orders.append(MenuItem(beverage_type, found))
        return found
    print("No beverage selected!")

  return 0.0
  
def ask_for_fries(user_orders = list):
  want_fries = yes_or_no_question("Would you like fries?")
  if(want_fries):
    fry_size = input("What fry size? (small $1.0, medium $1.50, large, $2.00")
    for fry in fries:
      if(fry_size == "small" and fry.name == "small"):
          mega = yes_or_no_question("Would you like to mega-size your fries?")
          if(mega):
            return return_fry_info(MenuItem("large", 2.0), user_orders)
          else:
            return return_fry_info(fry, user_orders)
      elif(fry_size == fry.name):
        return return_fry_info(fry, user_orders)
  return 0.0

def return_fry_info(menu_item : MenuItem, user_orders = list):
  print("Fry selected: " + menu_item.name + " Cost: " + str(menu_item.cost))
  user_orders.append(menu_item)
  return menu_item.cost

def ask_for_ketchup_packs(user_orders = list):
  num_of_packets = int(input("How many ketchup packs would you like? ($" +  str(ketchup_packet_cost) + " each)."))
  if(num_of_packets > 0):
    counter = 0
    while(counter < num_of_packets):
      user_orders.append(MenuItem("Ketchup Packets", ketchup_packet_cost))
      counter += 1
    return num_of_packets * ketchup_packet_cost
  return 0.0

discount = 0
discount_cost = 1.0

total_cost += ask_for_sandwitch(orders)
if(orders[-1].cost > 0):
  discount += 1

total_cost += ask_for_beverage(orders)
if(orders[-1].cost > 0):
  discount += 1

total_cost += ask_for_fries(orders)
if(orders[-1].cost > 0):
  discount += 1

total_cost += ask_for_ketchup_packs(orders)

if(discount == 3):
  total_cost -= discount_cost

print("Order List: ")

for order in orders:
  print("Order name: " + order.name + " Cost: $" + str(order.cost))

print("Total cost: $" + str(total_cost))
