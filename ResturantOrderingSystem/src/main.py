class MenuItem:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost
  
total_cost = 0.0

sandwichs = [MenuItem("chicken", 5.25), MenuItem("beef", 6.25), MenuItem("tofu", 5.75), MenuItem("none", 0.0)]
beverages = [MenuItem("small", 1.0), MenuItem("medium", 1.75), MenuItem("large", 2.25), MenuItem("none", 0.0)]
fries = [MenuItem("small", 1.0), MenuItem("medium", 1.50), MenuItem("large", 2.0), MenuItem("none", 0.0)]

def cycle_menu_item(menu_item, input_name, command):
    for item in menu_item:
        if(item.name == input_name):
            print(command + item.name + " Cost: " + str(item.cost))
            return item.cost
    return -1.0

def ask_for_sandwitch():
    sandwich_type = input("What sandwich would you like: (chicken $5.25, beef $6.25, tofu $5.75, none $0)")
    found = cycle_menu_item(sandwichs, sandwich_type, "Sandwich selected: ")
    if(found != -1.0):
        return found
    print("No sandwich selected!")

def yes_or_no_question(command_to_ask):
    answer = input(command_to_ask)
    return (answer == "yes")

def ask_for_beverage():
  want_beverage = yes_or_no_question("Would you like a beverage?")
  if(want_beverage):
    beverage_type = input("What beverage? (small 1.0, medium 1.75, large, 2.25")
    found = cycle_menu_item(beverages, beverage_type, "Beverage selected: ")
    if(found != -1.0):
        return found
    print("No beverage selected!")

  return 0.0
  
def ask_for_fries():
  want_fries = yes_or_no_question("Would you like fries?")
  if(want_fries):
    fry_size = input("What fry size? (small 1.0, medium 1.50, large, 2.00")
    for fry in fries:
      if(fry_size == "small" and fry.name == "small"):
          mega = yes_or_no_question("Would you like to mega-size your fries?")
          if(mega):
            print("Fry selected: " + "Large" + " Cost: 2.0")
            return 2.0
      elif(fry_size == fry.name):
        print("Fry selected: " + fry.name + " Cost: " + str(fry.cost))
        return fry.cost
  return 0.0

total_cost += ask_for_sandwitch()
total_cost += ask_for_beverage()
total_cost += ask_for_fries()
print("Total cost: " + str(total_cost))
