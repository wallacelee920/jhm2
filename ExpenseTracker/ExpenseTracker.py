from matplotlib.dviread import Page


while True:
    print("""
    Personal Expense Tracker
      1. Add Transaction
      2. Edit Transaction
      3. Delete Transaction
      4. Age
      5. Save and Exit
     """)
    choice = input("enter your choice:")

    if choice == "1":
        input("enter the date(YYYY-MM-DD):")
        input("enter the category(e.g Food Transport):")
        input("enter the amount:")
        input("enter the type(expense/Income):")

    elif choice == "2":
        input("enter the date(YYYY-MM-DD)")
        input("enter the category(e.g Food Transport):")
        input("enter the amount:")
        input("enter the type(expense/Income):")

    elif choice == "3":
        input("enter the date(YYYY-MM-DD)")
        input("enter the category(e.g Food Transport):")
        input("enter the amount:")
        input("enter the type(expense/Income):")

    elif choice == "4":
        age = int(input("How old are you?"))
        if age < 18:
            print("未成年")  
        elif age == 18:
            print("剛好成年")  
        else: 
            print("成年") 

    elif choice == "5":
        print("Save And Exit")
    break