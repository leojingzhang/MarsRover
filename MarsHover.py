#Leo Zhang @4-Aug-2021

#accept input
edge_input = input("please input upper-right coordinates (e.g. 5 5):  ")
start_input_1 = input("please give the first rover's current position (e.g. 1 2 N):  ")
command_input_1 = input("please give the command to the first rover (e.g. LMLMLMLMM):  ")
start_input_2 = input("please give the second rover's current position (e.g. 3 3 E):  ")
command_input_2 = input("please give the command to the second rover (e.g. MMRMMRMRRM):  ")

#prep the input variables
edge_x = int(edge_input.split()[0])
edge_y = int(edge_input.split()[1])

class Rover():
   def __init__(self, initial_location, full_commands):
      #parse the initial location input into x,y and heading direction
      start_location = initial_location.strip().split()
      self.x = int(start_location[0])
      self.y = int(start_location[1])
      self.d = str(start_location[2]).upper()

      #print(self.x)
      #print(self.y)
      #print(self.d)

      #error handling
      if self.x > edge_x or self.y > edge_y or self.x < 0 or self.y < 0:
         print('your starting point is out of the plateau!')
         return
      if self.d not in ['E','N','W','S']:
         print('Your input direction is incorrect!')
         return

      #parse the input commands and run step by step
      list_commands = list(full_commands)
      for command in list_commands:
         if str(command).upper() == 'L':
            self.turn_left()
         elif str(command).upper() == 'R':
            self.turn_right()
         elif str(command).upper() == 'M':
            self.advance()

   #function to handle turning left
   def turn_left(self):
      if self.d == 'E':
         self.d = 'N'
      elif self.d == 'N':
         self.d = 'W'
      elif self.d == 'W':
         self.d = 'S'
      elif self.d == 'S':
         self.d = 'E'

   # function to handle turning right
   def turn_right(self):
      if self.d == 'E':
         self.d = 'S'
      elif self.d == 'N':
         self.d = 'E'
      elif self.d == 'W':
         self.d = 'N'
      elif self.d == 'S':
         self.d = 'W'

   # function to handle moving forward one step
   def advance(self):
      if self.d == 'E':
         self.x += 1
      elif self.d == 'S':
         self.y -= 1
      elif self.d == 'W':
         self.x -= 1
      elif self.d == 'N':
         self.y += 1

      if self.x > edge_x or self.y > edge_y or self.x < 0 or self.y < 0:
         print('you now fell out of the plateau!')
         return

rover_1 = Rover(start_input_1, command_input_1)
print('Last location of the first rover is at:', rover_1.x, rover_1.y, rover_1.d)

rover_2 = Rover(start_input_2, command_input_2)
print('Last location of the second rover is at:', rover_2.x, rover_2.y, rover_2.d)