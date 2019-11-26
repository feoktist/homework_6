import random

years = {'Alex':1968, 'Bob': 1978, 'Charlie': 1988}
months = {'Alex' : 4, 'Bob': 3, 'Charlie': 5}
days = {'Alex':22, 'Bob': 1, 'Charlie': 25}
yob = years.keys()

person = random.choice(list(yob))

# -----------------------------------------------------------
def guessworks(w_data, dude_name, say):
  while say != w_data[dude_name]:
    print('Wrong answer! Try again! ')
    say = int(input(f'Enter your answer: '))
    if say == w_data[dude_name]:
      print('Gotcha!')
      print(10 * '-')
# -----------------------------------------------------------
answer = int(input(f'Enter YoB for writer {person}: '))
print(40 * '-')
guessworks(years, person, answer)

answer = int(input(f'Now guess MoB for writer {person}: '))
print(40 * '-')
guessworks(months, person, answer)

answer = int(input(f'Now guess DoB for writer {person}: '))
print(40 * '-')
guessworks(days, person, answer)

print ('End of victorina')