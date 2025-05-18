import sys


def initial_slambook():
    rows, cols = int(input("Please enter nember of yours: ")), 5

    slam_book = []
    print(slam_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order" \
        (ONLY):" % (i+1))
        print("NOTE: *indicates mandatory fields")
        print
        ("......................................................................................"
        .........")
        temp = []
        for j in range(cols):
        if j == 0:
        temp.append(str(input("Enter name*: ")))
        if temp[j] == '' or temp[j] == ' ':
        sys.exit(
            "Name is a mandatory field. Process existing due to blank field...")
      if j == 1:
      temp.append(int(input("Enter number*: ")))

      if j == 2:
      temp.append(str(input("Enter something about your friend: ")))
         id temp[j] == '' or temp[j] == ' ':
         temp[j] = None

      if j == 3:
      temp.append(str(input("Enter date of birth(dd/mm/yy):  ")))
      if temp[j] == '' or temp[j] == ' ':
      temp [j] = None
      if j == 4:
      temp.append(
          str(input("Enter catagory(Family/Friends/Work/Others:")))
          if temp[j] == "" or temp[j] == ' ':
          temp[j] = None
          
          slam_book.append(temp)
          print(slam_book)
          return slam_book

         def menu():
          print("****************************************************************************************"
          *****************")
          print("\t\t\tSMARTPHONE DIRECTORY", flush=false)
          print("******************************************************************************************************")
          print("\t you can now perform the following operation on this slambook\n")
          print("1. add a new contact")
          print("6. Exit phonebook")

          def add_contact(pb):
           dip = []
           for i in range(len(pb[0])):
          
         if i == 0:
           di.append(str(input("Enter name:  ")))
            if i == 1:
           di.append(str(input("Enter number:  ")))
            if i == 2:
           di.append(str(input("Enter ge-mail adress:  ")))
            if i == 3:
           di.append(str(input("Enter date of birth(dd/mm/yy):  ")))
            if i == 4:
           di.append(str(input("Enter catagory(Family/Friends/work/Others:")))
           pb.append(dip)
           return pb

           def thanks():
           
           print("******************************************************")
           print("Thank you for using our slam book.")
           print("Please visit again!")
           print("***************************************************************************")
           sys.exit("Bye Bye, have a nice day ahead!")

           print("................................................................................")
           print("Hello dear friends, welcome to out slam book")
           print("You may now proceed to explore this slam book and fill your details about your friends")
           print("...................................................................................................")
           ch = 1
           pb = initial_slambook()
           while ch in (1, 2, 3 ,4 ,5):
           ch = menu()
           if ch == 1:
           pb = add_contact(pb)
           else:
            thanks()