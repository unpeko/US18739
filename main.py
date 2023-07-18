# Functions go here...


def statement_generator(statement, decoration):

  sides = decoration

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""


# Main routine goes here...

# greeting

statement_generator("Tēnā koe!", "+")
statement_generator("Welcome to Fraser's school canteen!", "-")

# name checker (secqunce 1)

name = input("What is your name? ")
print()
while name.isalpha() == False:
  print(
    "Sorry, we really need to know your name to help us process this order.")
  name = input("What is your name? ")
  print()

if name.isalpha():
  welcoming = "Kia Ora {v}, welcome to the Fraser High School canteen! "
  print(welcoming.format(v=name))
  print()

# menu yes_no (sequnce 2)

greeting = "{}, would you like to see our menu? "

while True:
    userinput = input(greeting.format(name))

    if userinput.lower() == "yes":
        menu = "{}, what would you like to order? ".format(name)
        print(menu)
        break  # Exit the loop if the user says "yes"
    elif userinput.lower() == "no":
        print('Thank you {} for visiting us at Fraser High School Canteen.'.format(name))
        exit()  # Exit the program if the user says "no"
    else:
        print("Please answer with 'yes' or 'no'.")
      
# sequence 3 menu selection

menuList = "On the special menu today the Pie is worth $4.50 and The Burger is worth $7.89, {v} what would you like to order, either a Pie or a Burger? "
print()
foodResponse = input(menuList.format(v=name))
while foodResponse.lower() != "pie" and foodResponse.lower() != "burger":
  print("Invalid input. Please choose either a Pie or a Burger.")
  foodResponse = input(menuList.format(v=name))

finalResponse = "Thank you {v} for ordering the delicious {meal}. We will just get this ready for you."
if foodResponse.lower() == "pie":
  print(finalResponse.format(v=name, meal="Pie"))
else:
  print(finalResponse.format(v=name, meal="Burger"))
