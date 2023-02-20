"""
Final Project
Name: Zackery Spears
"""

# This dictionary stores everyone room, direction of the room and skill of the room
rooms = {
    'College Main Hall': {'North': 'Internship', 'East': 'CS-210', 'West': 'IT-140', 'South': 'IT-145', 'Skill': ''},
    'IT-145': {'North': 'College Main Hall', 'East': 'Computer Lab', 'Skill': 'Java'},
    'Computer Lab': {'West': 'IT-145', 'Skill': 'Leetcode'},
    'IT-140': {'East': 'College Main Hall', 'Skill': 'Python'},
    'Company': {'Wast': 'Internship', 'Skill': 'Job'},
    'Internship': {'South': 'College Main Hall', 'East': 'Company', 'Skill': 'Experience'},
    'CS-210': {'North': 'CS-260', 'West': 'College Main Hall', 'Skill': 'C++'},
    'CS-260': {'South': 'CS-210', 'Skill': 'Algorithms'}
    }

# This variable stores the current room the player in
current_room = 'College Main Hall'

# This variable stores user skills
skills = []

# This function is used for updating the room with the new room the user choices to go into
def find_new_room(current_room, direction):
    # Assigns the current_room to the new room
    new_room = current_room
    # Loop and if valid direction will the assign new room
    for i in rooms:
        if i == current_room:
            if direction in rooms[current_room]:
                new_room = rooms[current_room][direction]
    return new_room



# This a intro function that tell the user about the story's game
def intro():
    print('*' * 50)
    print('This is the story of a young college student\'s')
    print('adventure into becoming a software engineer')
    print('*' * 50)


# Calling the function intro
intro()

# Gets player name and uses the capitalize function to make the first letter of name capitalize
player_name = input('Please Enter your name? ').capitalize()


# Tell the player the instruction of the game
def instruction():
    print('Welcome', player_name)
    print('*' * 50)
    print('For this game, you must travel to each class')
    print('to gain all 6 skills before going')
    print('to the job interview.')
    print('To add skills please type "get the name of the skill" to update your skills')
    print('    Do you have what it takes?      ')
    print('    *Press enter to continue*  ')
    # This makes the user have to enter a key before moving on to the game
    title_screen = {'play': 'play'}
    title_screen['play'] = input()
    print('*' * 50)


# Calling the function instruction
instruction()


# This function stores the menu for the player
def player_menu():
    # Tells user what room they are in
    print('*' * 50)
    print('You are currently in the', current_room + '.')
    print('Current skills', skills)
    print('*' * 50)
    # Print each option to the user
    print('Enter a direction to move to a different room or select Exit to leave the game.')
    print('North, South, East, West')
    print('Exit')


# Loop over the game until the user selects Exit
while True:
    #Show the player what current skill is in the room
    if 'Skill' in rooms[current_room]:
        print('*' * 50)
        print('You can add ' + rooms[current_room]['Skill'] + ' to your skills')
        print('Type "get '+  rooms[current_room]['Skill'] + '" to update skills')
        # Game menu function
    player_menu()
    # Ask user what direction, removes white space with the strip function and lowers case the input
    direction = input().strip().lower()

    #Sets all the direction the user can go in a list
    directions = ['north', 'east', 'south', 'west']

    # If user type Exit the game ends
    if direction == 'Exit':
        print('Thanks for play' + player_name)
        break
    else:
        # Checks to see if user direction equals North, South, East or West
        if direction in directions:
            # Calls the function above to see if the direction the user input is in the Dictionary and capitalize the first letter
            new_room = find_new_room(current_room, direction.capitalize())
            # If the user can not move to this room print unable to move this direction
            if new_room == current_room:
                print('*' * 50)
                print('For some reason, somebody put a wall here? Try another direction.')
                print()
            # Updates the current room to the new room
            else:
                current_room = new_room
        #This allows the user to type "get skill" to add to the user skills
        elif direction.title() == str('Get ' + rooms[current_room]['Skill']):
            #Tells the user they have already gotten this item
            if rooms[current_room]['Skill'] in skills:
                print('You have already retrieved this item!! Pick another direction!')
            #Appends the new skill to the skills
            else:
                skills.append(rooms[current_room]['Skill'])
        #If the user types the direction wrong print to the user You did not enter a direction try again.
        else:
            print('*' * 50)
            print('You did not enter a direction try again.')

        #This if statement tells the user if they lose. By checking when they enter the final room and making sure if they do not have all the items.
        if len(skills) != 6 and current_room == 'Company':
            print('*' * 50)
            print('Sorry ' + player_name +',but you did not collect all the skills before attampting')
            print('the Job interview. Try again')
            print('*' * 50)
            break
        # This if statment tells the user if they win. By checking when they enter the final room and makes sure if they have all the skills.
        elif len(skills) == 6 and current_room == 'Company':
            print('*' * 50)
            print('You are at the '+current_room)
            print('Congratulations '+ player_name + ' you had all the skills needed to land software engineering job!')
            print('*' * 50)
            break