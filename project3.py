'''
Considering the maximum allowed speed of 80 km/h on a particular street, create a program that takes a value from the user representing the speed and based on that speed, determine whether they received a light, serious, or very serious fine. If the person is below the maximum speed, the program should display "no fine." If the speed is up to 10 km/h above the limit, it should display: "received a light fine." If the speed is between 11 to 20 km/h above the maximum speed, display: "received a serious fine." If the speed is more than 20 km/h above the maximum speed, display: "received a very serious fine".

Critically analyze the problem and find out:
(Try explaining this problem to yourself out loud and ask for more information/investigate further until you fully understand the problem.)

1. What are the required input data?
User's input representing the speed.
2. What should I do with this data?
- Compare the input speed with the maximum allowed speed and determine the appropriate fine category.
3. What are the constraints of this problem?
- The maximum allowed speed is 80 km/h.
4. What is the expected output?
- The expected output is to display the appropriate message based on the user's input speed.
5. What is the sequence of steps to be taken to achieve the expected result?
Input speed
max_speed = 80
if speed <= max_speed:
  print('no fine')
if speed > max_speed and speed <= max_speed + 10:
  print('received a light fine.')
if speed > max_speed +11 and speed <= max_speed + 20:
  print('received a serious fine.')
if speed > max_speed +20:
print('received a very serious fine')
 '''

speed = int(input('Type your speed'))
max_speed = 80
if speed <= max_speed:
  print('No fine')
elif speed > max_speed and speed <= max_speed + 10:
  print('Received a light fine.')
elif speed >= max_speed +11 and speed <= max_speed + 20: 
  print('Received a serious fine.')
elif speed > max_speed + 20:
  print('Received a very serious fine')