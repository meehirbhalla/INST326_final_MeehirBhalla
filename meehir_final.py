import sys
import random

class Archery:
    """a class for an archery game.
    
    Attributes:
        name (str): name of the player
        points (int): points scored by the player
        wind (str): cardinal direction of wind
        player_input (str): player inputted coordinates 
        final_coordinate (int): player inputted coordinates affected by wind
    
    Side effects: 
        greets and prompts the player for their name via a print statement to
        console.
    """    
    
    def __init__(self, name = 'Player 1'):
        """greets and prompts the player for a name.

        Args:
            name (str): player name. defaults to 'Player 1'.
            
        Side effects:
            name attribute is assigned user input.
            
            points attribute is set to a value of 0.
        """        
        print('Welcome to the Archery game! \n')
        self.name = input('Please enter your name: ')
        print(' ')
        self.points = 0
    
    def wind_direction(self):
        """randomly generates a wind direction from a list of North,
            South, East, and West.
        
        Side effects: 
            creates wind attribute and sets it to a random cardinal direction.
        """        
        # possible cardinal directions
        direction = ['North', 'South', 'East', 'West']
        
        # wind attribute is set to a random direction
        self.wind = random.choice(direction)
    
    def round (self):
        """prints welcome message and wind direction to start a round. then prompts
            the player for a coordinate given board restrictions according to wind
            direction.
        
        Side effects:
            prints current player's name and wind direction to console.
            
            assigns user input value to player_input attribute.
            
            converts player_input attribute to lowercase.
        """        
        # store wind attribute in a new variable
        wind = self.wind
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print(f'{self.name}, the current wind direction is {wind}')
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* \n')
        
        # possible inputs given wind direction
        N = ['a1', 'a2', 'a3', 'a4' 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4']
        S = ['a2', 'a3', 'a4', 'a5', 'b2', 'b3', 'b4', 'b5', 'c2', 'c3', 'c4', 'c5', 'd2', 'd3', 'd4', 'd5', 'e2', 'e3', 'e4', 'e5']
        E = ['a1', 'a2', 'a3', 'a4', 'a5' , 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5']
        W = ['b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5']
        
        # makes sure user is inputting value input
        if wind == 'North':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-4: ')
            while self.player_input.lower() not in N:
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 1-4: ')
        elif wind == 'South':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 2-5: ')
            while self.player_input.lower() not in S:
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-E and y is a number from 2-5: ')
        elif wind == 'East':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-D and y is a number from 1-5: ')
            while self.player_input.lower() not in E:
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from A-D and y is a number from 1-5: ')
        elif wind == 'West':
            self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from B-E and y is a number from 1-5: ')
            while self.player_input.lower() not in W:
                self.player_input = input(f'{self.name}, please enter a coordinate in the format (xy), where x is a letter from B-E and y is a number from 1-5: ')
        
        self.player_input = self.player_input.lower()
    
    def coordinate(self):
        """unpacks the user inputted coordinates and converts it to an int,
            then applies the random wind direction to the user input.

        Side effects:
            final_coordinate attribute is set to the value of player_input.
            
            player_input attribute is changed from string to int.
            
            final_coordinate attribute is changed from string to a 
                new int value after wind's effect.
        """        
        # unpack user inputted coordinates
        x,y = self.player_input
        self.final_coordinate = self.player_input
        
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
            1 deviation off the bullseye is 5 points, 2 deviations is 1 point. 

        Side effects:
            final_coordinate attribute is changed from an int to a string.
            
            points attribute is assigned either 10, 5, or 1 point(s).
            
            prints name and final_coordinate attributes in a message to console.
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
        
        if self.final_coordinate == bullseye:
            self.points += 10
            print(' ')
            print(f'BULLSEYE!: {self.name} hit the bullseye of C3! \n')
            print(f'You scored 10 points. \n')
        elif self.final_coordinate in five_points:
            self.points += 5
            print(' ')
            print(f'Your arrow landed on {self.final_coordinate}! \n')
            print(f'You scored 5 points. \n')
        else:
            self.points += 1
            print(' ')
            print(f'Your arrow landed on {self.final_coordinate}! \n')
            print(f'You scored 1 point... \n')


def main():
    """creates an instance of the Archery class and plays through each method 3 times
        via a while loop. 
    
    Attributes: 
        game (Archery): an instance of the Archery class.
    
    Side effects:
        prints current round.
        
        prints game over message with the name and points attribute
    """    
    # create an instance of the Archery class
    game = Archery()
    round = 1
    while round != 4:
        print(f'This is round {round} of Archery! \n')
        game.wind_direction()
        game.round()
        game.coordinate()
        game.validate_shot()
        
        round += 1
    print('Game over ' + (game.name) + '! You scored a total of -*-' + str(game.points) + ' points!-*- Thanks for playing Archery! \n')
    
    
if __name__ == "__main__":
    main()