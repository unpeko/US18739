def statement_generator(statement, decoration) :

  sides = decoration 

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""
  
statement_generator("Tēnā koe!","+")
statement_generator("Welcome to Fraser's school canteen!","-")
name = input ("What is your name? ")
print()

if name.isalpha() == False:
  print("Sorry we really need to know your name to help us process this order.")
  name = input("What is your name? ")
  print()

if name.isalpha():
  welcoming = "Kia Ora {v}, welcome to the Fraser High School canteen! "
  print(welcoming.format(v=name))