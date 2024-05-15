def get_numbers():
  while True:
    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
      return num1, num2
def add_numbers(num1, num2):
   return num1 + num2    
def multiply_numbers(num1, num2):
   return num1 * num2
def show_result(result):
  print(result)
def main():
  has_numbers = False
  result = None
  while True:
    print("\nMenu:")
    print("1. Enter numbers")
    print("2. Add numbers")
    print("3. Multiply numbers")
    print("4. Show output")
    print("5. Exit")
    choice = input("Enter your choice: ")
    #choice 2
    if choice == "1":
      num1, num2 = get_numbers()
      has_numbers = True
    #choice 2
    elif choice == "2":
      if not has_numbers:
        print("first enter numbers")
        continue
      result = add_numbers(num1, num2)
    #choice 3
    elif choice == "3":
      if not has_numbers:
        print("first enter numbers")
        continue
      result = multiply_numbers(num1, num2)
    #choice 4
    elif choice == "4":
     if has_numbers and result is not None:
        show_output(result)
      else:
        print("didnt do anything")
     #choice 5
    elif choice == "5":
      break
    else:
      print("Invalid choice")
