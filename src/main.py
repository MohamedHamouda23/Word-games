from tkinter import *
import csv
import random

def check(username):
    # Check if the username field empty
    if username=="":
     print("username field empty")
     return False
    # Check if the username is too long
    elif len(username) > 11:
        print("Username is too long")
        return False
    # Check if the username is too short
    elif len(username) < 6:
        print("Username is too short")
        return False
    # Check if the username is weak (only digits or only letters)
    elif username.isdigit() or username.isalpha():
        print("Weak username")
        return False
    # Check if the username contains at least one digit, one lowercase letter, and one uppercase letter
    elif any(char.isdigit() for char in username) and any(char.islower() for char in username) and any(char.isupper() for char in username):
        print("Strong username")
        return True
    # If the username meets none of the above conditions, consider it medium
    else:
        print("Medium username")
        return True

def check2(password):
    # Check if the password field empty
    if password=="":
     print("password field empty")
     return False
    # Check if the password length is greater than 11
    elif len(password) > 11:
        print("Password is too long")
        return False
    # Check if the password length is less than 6
    elif len(password) < 6:
        print("Password is too short")
        return False
   # Check if the password is weak (only digits or only letters)
    elif password.isdigit() or password.isalpha():
        print("Weak password\n")
        return False
    # Check if the password contains at least one digit, one lowercase letter, and one uppercase letter
    elif any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password):
        print("Strong password\n")
        return True
    # If none of the above conditions are met, consider the password medium
    else:
        print("Medium password\n")
        return True

def open_signup_window():
    # hide the root window and open new window with Sign up title
    root.withdraw()
    signup_window = Toplevel()
    signup_window.title("\nSign Up")

    def signup():
      # Getting the username and passowrd from an entry field
        username = username_entry.get()
        password = password_entry.get()
        # store checking funtions in variables
        username_valid = check(username)
        password_valid = check2(password)

         # Check if the username and password are validby  using checking function that store in variables
        if username_valid and password_valid:
           # open the users_info.txt file in append and read mode  and read all lines
            with open("users_info.txt", "r+") as info:
                lines = info.readlines()
                # Iterate through each line in the lines
                for line in lines:
                  # Split the line into parts using '|' as separator
                  parts = line.strip().split('|')
                  # Check if parts more than or equal to 2
                  if len(parts) >= 2:
                      existing_username, existing_password = parts
                      # Check if the username or password already exists and send a message back if they do
                      if username == existing_username.strip() or password.lower() == existing_password.strip():
                          print("Username or password already exists") 
                          print("Sign up failed\n")
                          return
                # If the username and password are not already taken, add them to the file 
                info.write(f"{username:<17} | {password:^30}\n")
                # display message with hide sign up window and unminimize the root window
                print("Sign up successful\n")
                signup_window.withdraw()
                root.deiconify()
        else:
            # if username or password result not true , display a message
            print("Sign up failed\n")

    # call when user click back
    def go_back():
        # destroy the signup window and unminimize the root window
        signup_window.destroy()
        root.deiconify()
    # label refer to username enrty field
    Label(signup_window, text="Username:").pack()
    # username enrty field packed in sign up 
    username_entry = Entry(signup_window)
    username_entry.pack()

    # label refer to passord enrty field
    Label(signup_window, text="Password:").pack()
    # password enrty field packed in sign up window 
    password_entry = Entry(signup_window)
    password_entry.pack()

    # button named Sign Up packed in signup_window and call signup function when clicked it 
    Button(signup_window, text="Sign Up", command=signup).pack()
    # button named Back packed in signup_window and call go_back function when clicked it 
    Button(signup_window, text="Back", command=go_back).pack()

# call when user click Log in
def open_login_window():
   # hide the root window and open new window with Log In title
    root.withdraw()
    login_window = Toplevel(root)
    login_window.title("Log In")

    def login():
      # Getting the username and password from an entry field
        username = username_entry.get()
        password = password_entry.get()

        # open the users_info.txt file in read  and write mode 
        with open("users_info.txt", "r+") as info:
            # read all lines in the file with extract the first one and save in lines varaible
            lines = info.readlines()[1:]
        # Iterate through each line in the file by lines varaible
        for line in lines:
            # Remove additional spaces within lines and divide the lines using the | symbol
            parts = line.strip().split('|')
            # check if both username and password entries are exist in file
            if username == parts[0].strip() and password == parts[1].strip():
                # display message with destroy login window and dispaly welcome messgae have the username
                print("Login successful")
                login_window.destroy()
                print("\nWelcome", username)
                # call the open_menu_window function and declare the variables responsible for score
                open_menu_window(username)
                score = 0
                score2=0
                # open the users_score.txt file in append, read, and seek from the beginning in the file.
                with open("users_score.txt", "a+") as tracker:
                    tracker.seek(0)
                    # save the header in variable assigned to content
                    content = (f"{'username':<17} | {'guess score':^30} | {'match score':^30} \n")   
                    # write the content in the file if not exist
                    if not content in tracker:
                        tracker.write(f"{'username':<17} | {'guess score':^30} | {'match score':^30} \n")   
                    # store a check of username exist in first part of line
                    exists = any(username == line.split(" | ")[0].strip() for line in tracker)
                    # use the exists variable if it become true, end the loop
                    if not exists:
                        tracker.write(f"{username:<17} | {score:^30} | {score2 :^30} \n")   
                break

        else:
          # if username or password not exist in file, display a message
            print("Incorrect username or password")
    # called when user  click on  back button
    def go_back():
        # destroy the login window and unminimize the root window
        login_window.destroy()
        root.deiconify()
    # label refer to username enrty field in login_window
    Label(login_window, text="Username:").pack()
    # username enrty field in log in window with declares position and size of it
    username_entry = Entry(login_window)
    username_entry.pack()
     # label refer to passowrd enrty field in login_window
    Label(login_window, text="Password:").pack()
    # password enrty field packed in login_window with hide the password by *
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    # button named Log In packed in login_window and call login function when clicked it 
    Button(login_window, text="Log In", command=login).pack()
    # button named Back packed in login_window and call go_back function when clicked it 
    Button(login_window, text="Back", command=go_back).pack()

# called when log in successfully
def open_menu_window(username):
    # open  window with Menu title
    menu = Toplevel(root)
    menu.title("Menu")
    # refer to label packed in menu indow 
    Label(menu, text="Choose an option:").pack()

    # The menu has a words guessing" button. Clicking it runs a lambda function with the argument word_guessing(username, menu)
    Button(menu, text="words guessing", command=lambda: word_guessing(username,menu)).pack()
    # The menu has a definitions matching button. Clicking it runs a lambda function with the argument definitions_matching(username,menu)
    Button(menu, text="definitions matching", command=lambda: definitions_matching(username,menu)).pack()
     # The menu has a Log out button. Clicking it runs a lambda function with the argument log_out(menu)
    Button(menu, text="Log out", command=lambda: log_out(menu)).pack()

# called when user click on words guessing button
def games_rules(username, game):
    # Create the CSV file if it doesn't exist
    try:
        with open('CSWords.csv', 'r') as reader:
            pass
    except FileNotFoundError:
        # Create the file with some sample data
        sample_data = [
            ["Word", "Definition", "Topic", "Level"],
            ["Python", "A programming language", "Programming", "1"],
            ["Variable", "A container for storing data", "Programming", "1"],
            ["Function", "A block of reusable code", "Programming", "1"],
            ["Loop", "A structure that repeats instructions", "Programming", "2"],
            ["Algorithm", "A step-by-step procedure", "Programming", "2"],
            ["Database", "An organized collection of data", "Programming", "3"],
            ["API", "Application Programming Interface", "Programming", "3"],
            ["Machine Learning", "AI that learns from data", "Programming", "4"],
            ["Blockchain", "Decentralized digital ledger", "Programming", "4"]
        ]
        with open('CSWords.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(sample_data)

    # Now open the file for reading
    with open('CSWords.csv', 'r') as reader:
        # identify specif name field for each row that become dictionary and refered to reader variable 
        reader = csv.DictReader(reader, fieldnames=["Word", "Definition", "Topic", "Level"])
        # skipping the header of the file
        next(reader) 
        # open users_score.txt file in read mode as tracker
        with open('users_score.txt', 'r') as tracker:
            # Iterate through each line in tracker
            for line in tracker: 
                # Split the line into parts using '|' as separator and remove whitespace
                parts = line.strip().split('|')
                # Check if the username is in the first part of the line
                if parts[0].strip() == username:
                    # Check the game part in the line and remove whitespace
                    points = int(parts[game].strip())
                    # Check if the points is less than or equal 2
                    if points <= 2:
                        level = 1
                    # Check if the points is less than or equal 15
                    elif points <= 15:
                        level = 2
                    # Check if the points is less than or equal 30
                    elif points <= 30:
                        level = 3
                    # excute when all conditions false
                    else:
                        level = 4
        # Display the word depending on the row in reader if its level is equal to the level of the user
        words = [row for row in reader if int(row['Level']) == level]
        return words

# called when user click on words guessing button
def word_guessing(username, menu):
 # hide the the menu window with dipslay message
  menu.withdraw() 
  print("\nWelcome to guess game")

  while True:
      # call games_rules fuunctions in varable words 
      words = games_rules(username, 1)
     # Choose a random row from the words list
      random_row = random.choice(words)
      # Extract the random word from the selected row
      random_word = random_row["Word"]
      # Extract the random word topic from the selected row
      topic = random_row["Topic"]
      # display meesage include topic and the word length
      print("\nTopic:", topic,"     Word letters:", len(random_word))
      # set the number of guesses left to 6
      guesses_left = 6
      # set a set to store guessed letters
      guessed_letters = set()

      while True:
          # Get user input and convert it to lowercase
          user_input = input("Guess the word or a letter: ").lower().strip()
          # Check if the user input empty
          if user_input=="":
           print("Please fill the inputs\n")
           continue
          # Check if the user input length equal 1
          if len(user_input) == 1:
              # Check if the user input is a letter already guessed
              if user_input in guessed_letters:
                  print("You already guessed that letter\n")
                  continue
              # Add the user input to guessed_letters 
              guessed_letters.add(user_input)
              # Check if the user input matches any character in the randomly chosen word
              if user_input in random_word.lower().strip():
                  print("Correct letter!\n")
                # if not display message with decrement the guesses left
              else:
                  print("Incorrect guess\n")
                  guesses_left -= 1
          # excute when user input equal converted lowercase random_word 
          elif user_input == random_word.lower().strip():
              # dipslay message with call score_update() and dispaly the current score
              print("Correct!")
              guess_score, _ = score_update(username, 1, 0)
              print(f"\ncurrent guess score: {guess_score}")
              break
            # if user input not equal random_word
          else:
              print("Incorrect guess\n")
              guesses_left -= 1             # decrement the guesses left

        # Check if all the letters in the random word have been guessed, ignoring whitespace,
        # or if all letters in the random word along with possible spaces have been guessed.
          if set(random_word.lower().strip()) == guessed_letters or all(letter in guessed_letters or letter == ' ' for letter in random_word.lower().strip()):
              # dispaly message along with the randowm word and call score_update() in varaible
              print("You've guessed all the letters! The word is:", random_word)
              guess_score, _ = score_update(username, 1, 0)
              # dispaly the current score
              print(f"\ncurrent guess score: {guess_score}")
              break
            # if guesses left equal 0
          elif guesses_left == 0:
              #call score_update() in varaible and dispaly the current score
              guess_score, _ = score_update(username, -1, 0)
              print(f"\ncurrent guess score: {guess_score}")
              print("Game over")   # display end message
              break
          # display the current state of the guessed word with underscores for unguessed letters
          guessed_word = ''.join(letter if letter in guessed_letters or letter == ' ' else '_' for letter in random_word.lower().strip())
          # display the guessed letters of the word
          print("Guessed Letters:", guessed_word)

      # # Ask the user if they want to play again
      play_again = input("Do you want to play again? (yes/any button): ").lower().strip()
      # Check if the user input is not 'yes'
      if play_again != 'yes':
          # unminimize the menu window
          menu.deiconify()
          break

# called when user click on definitions matching button
def definitions_matching(username, menu):
  # hide the the menu window with dipslay messages
  menu.withdraw()
  print("\nWelcome to the definition matching game")
  print("Match the words with their definitions (A, B, C)\n")

  while True:
      guesses_left = 2  # Set the number of guesses left to 2
      # call games_rules fuunctions in varable words 
      words = games_rules(username, 2)
      # Selecting 3 random dictionaries from words
      random_rows = random.sample(words, 3)
    # Extracting "Word" values into random_word variables
      random_word, random_word2, random_word3 = random_rows[0]["Word"], random_rows[1]["Word"], random_rows[2]["Word"]
      # Extracting definitions for the randomly selected words into definitions list
      definitions = [random_rows[0]["Definition"], random_rows[1]["Definition"], random_rows[2]["Definition"]]
      # Shuffle the list of definitions randomly
      random.shuffle(definitions)
      # Create a dictionary where options A, B, and C are mapped to the shuffled definitions
      options = {'A': definitions[0], 'B': definitions[1], 'C': definitions[2]}
      # Print the randomly selected words
      print(f"\n{random_word}\n{random_word2}\n{random_word3}\n")
      # Print the shuffled definitions along with options A, B, and C
      print(f"A- {definitions[0]}\n\nB- {definitions[1]}\n\nC- {definitions[2]}\n\n")
      # excute when guesses_left still more than 0
      while guesses_left > 0:  
          # Get user inputs and convert it to uppercase
          answer = input(f"{random_word}: ").upper()
          answer2 = input(f"{random_word2}: ").upper()
          answer3 = input(f"{random_word3}: ").upper()
           # Check if all three answers corresponding with Definitions
          if options.get(answer) == random_rows[0]["Definition"] and \
             options.get(answer2) == random_rows[1]["Definition"] and \
             options.get(answer3) == random_rows[2]["Definition"]:
              # dispaly meesage with call score_update() in varaible to return matching_score
              print("Correct!\n\n")      
              _, matching_score = score_update(username, 0, 1)  
              # dispaly the current score
              print(f"Current matching score: {matching_score}")
              break
          # Check if all letters in the concatenated answers are 'A', 'B', or 'C', 
          # or if there are duplicates in the answers.
          elif not all(letter in 'ABC' for letter in (answer + answer2 + answer3)) or len(set(answer + answer2 + answer3)) != len(answer + answer2 + answer3):
              print("\nInputs must have (A, B, C)\n")
            # Check if any of the answers are empty strings.
          elif answer == "" or answer2 == "" or answer3 == "":
              print("Fill all the inputs\n\n")
            # excute when previous conditions false
          else:
              # display meesge with decrement the guesses left
              print("Incorrect answers\n\n")
              guesses_left -= 1
              # check if guesses_left become 0
              if guesses_left == 0:
                  # call score_update() in varaible to return matching_score
                  _, matching_score = score_update(username, 0, -1)  
                  # dispaly the current score and messgae
                  print(f"Current matching score: {matching_score}")
                  print("Game over")
                  break
      # Ask the user if they want to play again
      play_again = input("Do you want to play again? (yes/any button): ").lower().strip()
      # Check if the user input is not 'yes'
      if play_again != 'yes':
          # unminimize the menu window
          menu.deiconify()
          break

def score_update(username, point, point2):
  # set guess score to 0
  guess_score = 0
  # set matching score to 0
  matching_score = 0
  # create an empty list to store updated lines
  updated_lines = []
  # open users_score.txt file in read mode as tracker
  with open("users_score.txt", "r+") as tracker:
      # read all lines and store in lines variable
      lines = tracker.readlines()
      # iterate through each line in lines
      for line in lines:
          # split the line into parts using '|' as separator and remove whitespace
          parts = line.split('|')
          # check if the username is in the first part of the line
          if parts[0].strip() == username:
              # Calculate the guess_score, ensuring it's not negative
              guess_score = max(0, int(parts[1].strip()) + int(point))
              # Calculate the matching_score, ensuring it's not negative
              matching_score = max(0, int(parts[2].strip()) + int(point2))
              # set the updated line with username, guess score, and matching score
              updated_line = f"{username:<17} | {guess_score:^30} | {matching_score:^30}"
              # append the updated line to updated_lines
              updated_lines.append(updated_line)
          else:
              # if username not in line, append the line as it is to updated_lines
              updated_lines.append(line)
      # move the file pointer to the beginning
      tracker.seek(0)
      # overwrite the file with the updated lines
      tracker.writelines(updated_lines)
  # return guess_score and matching_score
  return guess_score, matching_score

# execute hen user click on Log out
def log_out(menu):
    # Hide the menu window
    menu.withdraw()  
    # Display a message
    print("Log out successfully ")
    # unminimize the root window
    root.deiconify()  

# open users_info.txt in appending and reading mode as info
with open("users_info.txt", "a+") as info:
     # move the file pointer to the beginning
    info.seek(0)
    # read all lines and store in contents
    contents = info.read()
    # check if the header is not in contents
    if not contents:
        info.write("username" + "|".center(24) + "password\n".center(10))

# Create the Tkinter root window
root = Tk()
# Set the title of the window
root.title("Edeo learning")

# Create a label widget to display a welcome message
label = Label(root, text="Welcome to Edeo Learning Program", font="Arial 10")
# Place the label widget in the root window and configure its position
label.grid(row=0, column=0, columnspan=2, pady=20)

# Create a button widget for signing up
button1 = Button(root, text="Sign Up", font="Arial 10", command=open_signup_window)
# Place the sign-up button in the root window and configure its position
button1.grid(row=1, column=0)

# Create a button widget for logging in
button2 = Button(root, text="Log In", font="Arial 10", command=open_login_window)
# Place the login button in the root window and configure its position
button2.grid(row=1, column=1)
# Start the Tkinter event loop
root.mainloop()