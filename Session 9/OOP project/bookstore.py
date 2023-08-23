class User:
    def __init__(self, name, password, phone, address, ans1, ans2, ans3, id):
        self.userID = id
        self.userName = name
        self.userPassword = password
        self.userCart = []
        self.userPhone = phone
        self.userAddress = address
        self.secretAns1 = ans1
        self.secretAns2 = ans2
        self.secretAns3 = ans3


class Book:
    def __init__(self,name, author, amount, btype, price, id):
        self.bookID = id
        self.bookName = name
        self.bookAuthor = author
        self.amountAvailable = amount
        self.bookType = btype
        self.bookPrice = price


class BookStore(User, Book):
    def __init__(self):
        self.users = []
        self.books = []
        self.userCounter = 0
        self.bookCounter = 0

    def registerNewUser(self):
        print("Welcome!")
        name = ""
        password = ""
        confirm = " "
        available = False
        while not available:
            found = False
            name = input("Enter Username: ")
            for user in self.users:
                if user.userName == name:
                    found = True
                    print("username already in use, Try another one")
            if not found:
                available = True

        while password != confirm:
            password = input("Password: ")
            confirm = input("Confirm password: ")
            if password != confirm:
                print("Error: Password and Confirm password are not the same")

        phone = input("Phone number: ")
        address = input("Address: ")
        ans1 = input("What is your favorite color?: ")
        ans2 = input("What is your favorite Team?: ")
        ans3 = input("What is your dream car?: ")

        self.userCounter += 1

        newUser = User(name, password, phone, address, ans1, ans2, ans3, self.userCounter)
        self.users.append(newUser)

    def addBook(self):
        name = input("Enter book's name: ")
        name.capitalize()
        author = input("Enter author's name: ")
        author.capitalize()
        amount = int(input("Amount to be added: "))
        btype = input("Book's type: ")
        btype.capitalize()
        price = 0
        found = False
        for book in self.books:
            if book.bookName == name and book.bookAuthor == author:
                price = book.bookPrice
                amount = book.amountAvailabile + amount
                found = True
        if not found:
            price = input("Enter book's selling price: ")

        self.bookCounter += 1

        newBook = Book(name, author, amount, btype, price, self.bookCounter)
        self.books.append(newBook)

    def login(self):
        username = input("Enter username: ")
        password = input("Enter Password: ")
        login = False
        for user in self.users:
            if user.userName == username and user.userPassword == password:
                print("login successful!")
                login = True
                self.action(username)
        if not login:
            while True:
                print("1. Try again\n2. Forgot Password\n3. Exit")
                choice = input("Choice: ")
                if choice == '1':
                    self.login()
                elif choice == '2':
                    self.forgetPass()
                elif choice == '3':
                    exit(0)
                else:
                    print("Wrong Input")

    def forgetPass(self):
        name = input("Username: ")
        for user in self.users:
            if user.userName == name:
                ans1 = input("What is your favorite color?: ")
                ans2 = input("What is your favorite Team?: ")
                ans3 = input("What is your dream car?: ")
                if user.secretAns1 == ans1 and user.secretAns2 == ans2 and user.secretAns3 == ans3:
                    password = ""
                    confirm = " "
                    while password != confirm:
                        password = input("Password: ")
                        confirm = input("Confirm password: ")
                        if password != confirm:
                            print("Error: Password and Confirm password are not the same")
                        else:
                            user.userPassword = password

    def printBook(self, book):
        lst = []
        lst.append({"book's ID": book.bookID})
        lst.append({"Name": book.bookName})
        lst.append({"Author's Name": book.bookAuthor})
        lst.append({"Available amount": book.amountAvailable})
        lst.append({"Type": book.bookType})
        lst.append({"Price": book.bookPrice})
        print(lst)

    def viewBooks(self):
        if len(self.books) > 0:
            for book in self.books:
                self.printBook(book)
        else:
            print("No Books Are available")

    def viewCertainBook(self):
        name = input("Enter Book's name")
        name.capitalize()
        found = False
        for book in self.books:
            self.printBook(book)
            found = True
        if not found:
            print("Book is unavailable")

    def viewBookByType(self):
        btype = input("Enter Book's type: ")
        btype.capitalize()
        found = False
        for book in self.books:
            if book.bookType == btype:
                self.printBook(book)
                found = True
        if not found:
            print("Book is unavailable")

    def viewCertainAuthor(self):
        author = input("Enter Author's name")
        author.capitalize()
        found = False
        for book in self.books:
            if book.bookAuthor == author:
                self.printBook(book)
                found = True
        if not found:
            print("Book is unavailable")

    def addtoCart(self, name, book):
        for user in self.users:
            if name == user.userName:
                user.userCart.append(book)
                book.amountAvailable -= 1

    def viewCart(self, name):
        for user in self.users:
            if name == user.userName:
                if len(user.userCart) > 0:
                    print(user.userCart)
                    print("Order?(y/any other button)")
                    ans = input("Choice: ")
                    if ans == 'y':
                        print("Shipping Started!")
                        user.userCart.empty()
                    else:
                        pass
                else:
                    print("Cart is empty!")


    def action(self, name):
        while True:
            print("1. View All Books\n2. View Specific Type\n3. View Certain Book\n4. View Books by Author")
            print("5. Add Book\n6. View Cart\n7. Exit")
            choice = input("Choice: ")
            if choice == '1':
                self.viewBooks()
            elif choice == '2':
                self.viewBookByType()
            elif choice == '3':
                book = self.viewCertainBook()
                print("Add to Cart?(y/any other button)")
                ans = input("Choice: ")
                ans.lower()
                if ans == 'y':
                    self.addtoCart(name, book)
                else:
                    pass

            elif choice == '4':
                self.viewCertainAuthor()
            elif choice == '5':
                self.addBook()
            elif choice == '6':
                self.viewCart(name)
            elif choice == '7':
                exit(0)
            else:
                print("Wrong Input")

    def running(self):
        while True:
            print("1. Register New User\n2. Login\n3. Exit")
            choice = input("Choice: ")
            if choice == '1':
                self.registerNewUser()
            elif choice == '2':
                self.login()
            elif choice == '3':
                exit(0)
            else:
                print("Wrong Input")


bs = BookStore()
bs.userCounter += 1
u = User("amr", "amr123", 1234, "street", "Blue", "Barca", "Brabus", bs.userCounter)
bs.bookCounter += 1
b = Book("Got", "AmrG", 4, "fantasy", 3.15, bs.bookCounter)
bs.users.append(u)
bs.books.append(b)
bs.running()

