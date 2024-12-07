# List of books
books = ['Python Basics', 'Advanced Python', 'Intermediate Python', 'Understanding SQL', 'Comprejensive Java', 'JavaScript for Beginners']

#Welcome the user
print('Welcome to Joseph"s Library')

act = True

def view_books():
  print(f'{books}')

def borrow_book():
  book_to_borrow = input('Please enter book to borrow: ')
  if (book_to_borrow not in books):
    print(f'\nWe don"t have {book_to_borrow} right now\n')
  else:
    books.remove(book_to_borrow)
    print('\nEnjoy your read and don"t forget to return \n')

def return_book():
  book_to_return = input('Which book do you want to return? ')
  books.append(book_to_return)
  print(f'\nYou have returned {book_to_return}')

while act:
  # Asks the user for the action they want to perform
  action = input('\nDo you want to view, borrow or return a book? Enter either "v" to view, "b" to borrow or "r" to return a book OR enter "q" to quit : ')
  if (action == 'v'):
    view_books()
  elif (action == 'b'):
    borrow_book()
  elif (action == 'r'):
    return_book()
  elif (action == 'q'):
    act = False
  else:
    print('Please enter a valid input')





