import sys
import random
from webbrowser import get

class Archery:
    """an archery game.
    
    Atttributes:
        self.name (str): name of the player
        
    """    
    def __init__(self, name = 'Player 1'):
        """prompts the player for a name.

        Args:
            name (str): player name. defaults to 'Player 1'.
            points (int): starting points value of 0.
        """        
        print('Welcome to the Archery game!')
        print(' ')
        self.name = input('Please enter your name: ')
        self.points = 0
    
    def wind_direction(self):
        """randomly generates a wind direction from a list of North,
        South, East, and West.
        
        Returns: 
            str: string represented wind direction.
        """        
        direction = ['N', 'S', 'E', 'W']
        print(' ')
        self.wind = random.choice(direction)
        
        if self.wind == 'N':
            self.wind = 'North'
        elif self.wind == 'S':
            self.wind = 'South'
        elif self.wind == 'E':
            self.wind = 'East'
        elif self.wind == 'W':
            self.wind = 'West'
    
    def round (self):
        """prints welcome message and wind direction to start a round. then, prompts
        the player for a coordinate given board restrictions.

        Returns:
            str: lowercase string representation of the users inputted coordinates in 
                an x,y format. where x is a letter and y is a number.
        """        
        # store wind attribute in a new variable
        wind = self.wind
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print(f'{self.name}, the current wind direction is {wind}')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print(' ')
        
        # possible inputs given wind direction
        N = ['a5', 'b5', 'c5', 'd5', 'e5']
        S = ['a1', 'b1', 'c1', 'd1', 'e1']
        E = ['e1', 'e2', 'e3', 'e4', 'e5']
        W = ['a1', 'a2', 'a3', 'a4', 'a5']
        
        if wind == 'North':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-4: ')
            while self.player_input.lower() in N:
                print(' ')
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-4: ')
        elif wind == 'South':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 2-5: ')
            while self.player_input.lower() in S:
                print(' ')
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 2-5: ')
        elif wind == 'East':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-D and y is a number from 1-5: ')
            while self.player_input.lower() in E:
                print(' ')
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-D and y is a number from 1-5: ')
        elif wind == 'West':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from B-E and y is a number from 1-5: ')
            while self.player_input.lower() in W:
                print(' ')
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from B-E and y is a number from 1-5: ')
        
        self.player_input = self.player_input.lower()
    
    def coordinate(self):
        """unpacks the user inputted coordinates and converts it to an int,
        then applies the random wind direction to the user input.

        Returns:
            int: the coordinate of the shot with the wind direction applied.
        """        
        # unpack inputted coordinates
        x,y = self.player_input
        self.final_coordinate = self.player_input
        # unpack x and y from player input
        # sets the player_input as an int
        if x == 'a':
            self.player_input = int(str('1') + str(y))
        elif x  == 'b':
            self.player_input = int(str('2') + str(y))
        elif x  == 'c':
            self.player_input = int(str('3') + str(y))
        elif x  == 'd':
            self.player_input = int(str('4') + str(y))
        elif x  == 'e':
            self.player_input = int(str('5') + str(y))
        
        # the final coordinate depends on the random wind direction
        if self.wind == 'North':
            self.final_coordinate = int(self.player_input) + 1
        elif self.wind == 'South':
            self.final_coordinate = int(self.player_input) - 1
        elif self.wind == 'East':
            self.final_coordinate = int(self.player_input) + 10
        elif self.wind == 'West':
            self.final_coordinate = int(self.player_input) - 10
    
    def validate_shot(self):
        """calculates points given a bullseye of C3. the bullseye is 10 points, 
        1 deviation off the bullseye is 5 points, 2 is 1 point. 

        Returns:
            int: points scored that round
        """ 
        f,l = str(self.final_coordinate)

        if f == '1':
            self.final_coordinate = (str('A') + str(l))
        elif f == '2':
            self.final_coordinate = (str('B') + str(l))
        elif f  == '3':
            self.final_coordinate = (str('C') + str(l))
        elif f == '4':
            self.final_coordinate = (str('D') + str(l))
        else:
            self.final_coordinate = (str('E') + str(l))
        
        five_points = ['B2','B3','B4','C2','C4','E2','E3','E4']
        bullseye = 'C3'
        
        print('final coordinate', self.final_coordinate)
        
        if self.final_coordinate == bullseye:
            self.points += 10
            print(' ')
            print(f'BULLSEYE!: {self.name} hit the bullseye of C3!')
            print(' ')
            print(f'You scored 10 points.')
            print(' ')
        elif self.final_coordinate in five_points:
            self.points += 5
            print(' ')
            print(f'Your arrow landed on {self.final_coordinate}!')
            print(' ')
            print(f'You scored 5 points.')
            print(' ')
        else:
            self.points += 1
            print(' ')
            print(f'Your arrow landed on {self.final_coordinate}!')
            print(' ')
            print(f'You scored 1 point...')
            print(' ')
            
    # def announce(self):
    #     """given how many points the player has scored. prints a message
    #     of where their arrow landed and how many points they scored for 
    #     that shot.
    #     """        
    #     if self.points == 10:
    #         print(' ')
    #         print(f'BULLSEYE!: {self.name} hit the bullseye of C3!')
    #     elif self.points == 5:
    #         print(' ')
    #         print(f'Your arrow landed on {self.final_coordinate}!')
    #         print(' ')
    #         print(f'You scored 5 points.')
    #     else:
    #         print(' ')
    #         print(f'Your arrow landed on {self.final_coordinate}!')
    #         print(' ')
    #         print(f'You scored 1 point...')
    #         print(' ')

def main():
    """_summary_
    """    
    test = Archery()
    round = 1
    while round != 4:
        test.wind_direction()
        test.round()
        test.coordinate()
        test.validate_shot()
        
        round += 1
    print('Game over ' + (test.name) + '! You scored a total of ' + str(test.points) + ' points. Thanks for playing Archery!')
    
    
if __name__ == "__main__":
    main()