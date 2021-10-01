class Library:
    list_of_books = ["Harry Potter and the Socceror's stone",
                     "Harry Potter and the Chambers of secret",
                     "Harry Potter and the Prisoner of Azkaban",
                     "Harry Potter and the Goblet of Fire",
                     "Harry Potter and the Order of the Pheoix",
                     "Harry Potter and the Half Blood Prince",
                     "Harry Potter and The Deathly Hallows",
                     "Harry Potter and the Cursed Child",
                     "Rich Dad Poor Dad",
                     "Fault On Our Stars",
                     "Einstein's Biography"]

    name_of_library = 'Aarush International Library'

    def __init__(self, name, todo):
        self.name = name
        self.todo = todo

    def show_books(self):
        if len(self.list_of_books) != 0:
            print("Hi! {0}. The available books are: ".format(self.name))
            print()
            for no, book in enumerate(self.list_of_books):
                print('{0}.> {1}'.format(no + 1, book))

        else:
            print('Sorry the library has no book available')
            quit()

    def lend(self):
        self.show_books()
        print()

        yes = False
        book_to_lend = input('Which book would you like to take: ')
        for is_present in self.list_of_books:
            if book_to_lend == is_present:
                yes = True
                self.list_of_books.remove(book_to_lend)
                print()
                print('Here is your book "{}", Enjoy:)'.format(book_to_lend))
        if yes is False:
            print()
            print('Sorry! The book is you are looking for is not available :(')
            print()
            would_u = input('Would you like to take another book(y/n): ')
            if would_u == 'y':
                self.lend()
            elif would_u == 'n':
                print()
                print('Thanks {1} for visiting "{0}"'.format(self.name_of_library,
                    self.name))
                print()
                print('Visit Again :)')
                quit()
            else:
                print()
                print('Invalid Input :(')
                print()
                print('Try again')
                print()
                self.lend()

    def ret_urn(self):
        print('Hi! {}'.format(self.name))
        print()
        which = input('Which book do you want to return: ')
        self.list_of_books.append(str(which))

        def lend_another():
            print()
            again = input('Would you like to take another book(y/n): ')
            if again == 'y':
                print()
                self.lend()
            elif again == 'n':
                print()
                print('Thanks {1} for visiting "{0}"'.format(self.name_of_library,
                    self.name))
                print()
                print('Visit again :)')
                quit()
            else:
                print()
                print('Invalid input :(')
                print()
                print('Please try again')
                lend_another()

        lend_another()

    def add_book(self):
        print()
        print('Hi! {0}. Thanks for Donating books to "{1}" :)'.format(self.name,
            self.name_of_library))
        print()
        how_many = int(input('How many books would you like to donate: '))
        for book in range(how_many):
            print()
            book_name = input('Enter the name of the book {}: '.format(book + 1))
            self.list_of_books.append(str(book_name))
        print()
        print('Thanks for Donating the book :)')
        print()

        def lend_another():
            print()
            again = input('Would you like to take another book(y/n): ')
            if again == 'y':
                print()
                self.lend()
            elif again == 'n':
                print()
                print('Thanks {1} for visiting "{0}"'.format(self.name_of_library,
                    self.name))
                print()
                print('Visit again :)')
                quit()
            else:
                print()
                print('Invalid input :(')
                print()
                print('Please try again')
                lend_another()

        lend_another()


def main():
    first = 1

    while True:
        name = ''
        if first == 1:
            name = input('Please enter your name: ')
            first += 1

            print()

        if first == 2:
            first += 1
            rea_son = input('What would you like to do (q -> quit): ')

        else:

            rea_son = input('Would you like to do something else (q -> quit): ')

        visitor = Library(name, rea_son)
        print()
        if visitor.todo == 'See books':
            visitor.show_books()
            print()

            def should_we():
                want_to = input('Do you want to lend any book(y/n): ')
                if want_to == 'y':
                    print()
                    visitor.lend()
                elif want_to == 'n':
                    print()
                    print('Thanks {1} for visiting "{0}"'.format(visitor.name_of_library,
                        visitor.name))
                    print()
                    print('Visit again :)')
                    quit()
                else:
                    print()
                    print('Invalid input :(')
                    print()
                    print('Please try again')
                    print()

                    should_we()

            should_we()

        elif visitor.todo == 'Lend book':
            visitor.lend()

            print()

        elif visitor.todo == 'Return book':
            visitor.ret_urn()

            print()

        elif visitor.todo == 'Add book':
            visitor.add_book()

            print()

        elif visitor.todo == 'q':
            print()
            print('Thanks {1} for visiting "{0}"'.format(visitor.name_of_library,
                visitor.name))
            print()
            print('Visit again :)')
            quit()

        else:
            print()
            print('Invalid input :(')
            print()
            print('Please try again')
            print()


if __name__ == "__main__":
    print()
    main()
# code ends here
