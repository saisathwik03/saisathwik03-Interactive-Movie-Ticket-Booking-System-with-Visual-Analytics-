import matplotlib.pyplot as plt

def initialize_movies():
    movies = []
    num_movies = int(input("Enter number of movies: "))
    duration = '120 mins'
    for i in range(num_movies):
        dic = {}
        title = input("Enter title of the movie: ")
        dic['movie'] = title
        dic['duration'] = duration
        dic['available_seats'] = 100
        dic['seats'] = initialize_seats()
        movies.append(dic)
    return movies

def display_movies(movies):
    for movie in movies:
        print(movie)
        print()

def initialize_seats():
    board = []
    for _ in range(10):
        row = []
        for j in range(1, 11):
            row.append(j)
        board.append(row)
    return board

def display_seating(movies, index):
    print('Title: ', movies[index]['movie'], 'available seats: ', movies[index]['available_seats'])
    board = movies[index]['seats']
    for row in board:
        for seat in row:
            print(seat, end=' ')
        print()
    generate_pie_chart(movies[index])

def book_seat(movies):
    display_movies(movies)
    index = int(input("Enter the movie index to book tickets: "))
    board = movies[index]['seats']
    tickets = int(input("Enter number of tickets to book: "))
    booked = []
    i = 0
    while i < tickets:
        row = int(input("Enter the row: "))
        col = int(input("Enter the col: "))
        if board[row][col] != 'B':
            board[row][col] = 'B'
            movies[index]['available_seats'] -= 1
            booked.append((row, col))
            i += 1
        else:
            print('Seat already booked!!')
    generate_pie_chart(movies[index])
    return index, movies, booked

def view_bookings(index, movies, booked):
    print('Movie Name: ', movies[index]['movie'])
    for booking in booked:
        print("Booked seat at row:", booking[0], 'at col:', booking[1])
    board = movies[index]['seats']
    for row in board:
        for seat in row:
            print(seat, end=' ')
        print()



def display_menu():
    print('Welcome to Book My Show!!')
    movies = initialize_movies()
    booked = []
    while True:
        print('''Menu Loop:
          a. view movies
          b. check seat availability
          c. book a seat
          d. view bookings
          e. most booked movie
          f. exit
          ''')
    
        select = input('Enter a/b/c/d/e/f: ')
        if select == 'a':
            display_movies(movies)
        elif select == 'b':
            index = int(input("Enter the movie index to see the available seats: "))
            display_seating(movies, index)
        elif select == 'c':
            index, movies, booked = book_seat(movies)
        elif select == 'd':
            view_bookings(index, movies, booked)
        elif select == 'e':
            generate_bar_chart(movies)
        elif select == 'f':
            print('Exiting from Book My Show!! Thank you.')
            break
        else:
            print('Invalid selection.')

display_menu()
