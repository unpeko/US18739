# Functions go here...


def statement_generator(statement, decoration):

  sides = decoration

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""


def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response

    elif response == "no" or response == "n":
      response = "no"
      return response

    else:
      print("Please answer yes / no")


# Main routine goes here...

# greeting

statement_generator("Tēnā koe!", "+")
statement_generator("Welcome to Fraser's school canteen!", "-")
name = input("What is your name? ")
print()

# name checker (secqunce 1)
if name.isalpha() == False:
  print(
    "Sorry, we really need to know your name to help us process this order.")
  name = input("What is your name? ")
  print()

if name.isalpha():
  welcoming = "Kia Ora {v}, welcome to the Fraser High School canteen! "
  print(welcoming.format(v=name))
  print()

# menu yes_no (sequnce 2)
greeting = ("{v}, would you like to see our menu? ")
userinput = yes_no(greeting.format(v=name))
print()

if userinput == "yes":
  print(
    " On the special menu today we have the Pie for $4.50 and the Burger for $7.89."
  )
  menu = (
    "{v} what would you like to order?   Please enter either a Pie or a Burger. "
  )
  print(menu.format(v=name))

elif userinput == "no":
  thankyou = ("Thank you {v} for visiting us at Fraser High School Canteen.")
  print(thankyou.format(v=name))