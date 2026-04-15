import colorama

colorama.init()

print(colorama.Fore.BLACK)
print(colorama.Back.GREEN)

print('🐍Gadiuka Cafe🐍')

print(colorama.Back.YELLOW)

balance = input('Input your balance: ')
balance = int(balance)
coffee = 40
tea = 20
cookies = 5
pie = 80
secret = 4000

print('balance: ' + str(balance))
print('coffee: ' + str(coffee))
print('tea: ' + str(tea))
print('cookies: ' + str(cookies))
print('pie: ' + str(pie))

cui = input('Customer:')

if cui == 'coffee':
 balance = balance - coffee
print('Balance: ' + str(balance))

if balance < coffee:
 print('Sorry, but you do not have enough money!')

elif cui == 'tea':
 balance = balance - tea
print('Balance: ' + str(balance))

if balance < tea:
 print('Sorry, but you do not have enough money!')

elif cui == 'cookies':
 balance = balance - cookies
print('Balance: ' + str(balance))

if balance < cookies:
 print('Sorry, but you do not have enough money!')

elif cui == 'pie':
 balance = balance - pie
print('Balance: ' + str(balance))

if balance < pie:
 print('Sorry, but you do not have enough money!')

elif cui == 'secret':
  balance = balance - secret
  print('Balance: ' + str(balance))

  print('Oh! You want to buy a python? Wait a minute...')
  print('HAHAHAHA! You made a very big mistake... This is a TRAP!')
  print(colorama.Back.LIGHTBLACK_EX)
  print("""------___------
  --___------
  ---------___--""")
  print(colorama.Back.RED)
  print('Welcome to the Underworld')
  print(colorama.Back.LIGHTBLACK_EX)
  print('paper(print take to take)')
  print(colorama.Back.LIGHTWHITE_EX)

  input()

  if input() == 'take':
      print('paper: python from Gadiuka Cafe is in the cage, but you if you want to save him you need to find the cage')
  print(colorama.Back.LIGHTBLACK_EX)
  print('instruction(print take to take)')
  print(colorama.Back.LIGHTWHITE_EX)
  input()

  if input() == 'take':
      print("""instruction:
      print take to take;
      print jump to jump;
      print go to go;
      print open to open;
      print fight to fight.""")
  print(colorama.Back.LIGHTBLACK_EX)
  print('cave')
  print('jump?')

  input()

  if input() == 'jump':
      print("""------___------
  --___------
  ---------___--""")

  print(colorama.Back.YELLOW)
  print('mineshaft')
  print('go?')

  input()

  if input() == 'go':
      print("""----------------------------------------------------------------
----------------------------------------------------------------""")
  print(colorama.Back.RED)
  print('The Final Boss')
  print('The Gadiuka Cafe admin')
  print('admin: I am here. You think you can save the python?! HAHAHA! First you need to path through me!')
  print('fight?')

  input()

  if input() == 'fight':
      print('What? What do you do? Why? Why you choose to fight? Ok. You won. Here is your key...')
      print('You won!')
      print(colorama.Back.LIGHTYELLOW_EX)
      print('key')
      print('take?')

      input()

      if input() == 'take':
          print('the key is your now. Find and open the cage! Hurry!')
  print(colorama.Back.LIGHTBLACK_EX)

  print(colorama.Back.YELLOW)
  print('mineshaft')
  print('go?')

  input()

  if input() == 'go':
      print("""----------------------------------------------------------------
  ----------------------------------------------------------------""")

  print(colorama.Back.LIGHTBLACK_EX)
  print('/🐍/(the cage)')
  print('Nice! You found it! Now use your key to open the cage.')
  print('open?')

  input()

  if input() == 'open':
      print('🐍')
      print('The python is free! Now get back to the Gadiuka Cafe.')
      print('go?')

      input()

      if input() == 'go':
          print(colorama.Fore.BLACK)
          print(colorama.Back.GREEN)

          print('🐍Gadiuka Cafe🐍')

          print(colorama.Back.YELLOW)
          print('🐍Wow! Now you are the new admin here! And... thank you. Bye. But wait. I want to tell you who am I. And I am Gadiuka. Now... Bye.')

  else:
   if balance < secret:
    print('Sorry, but you do not have enough money!')

  print(colorama.Fore.BLACK)
  print(colorama.Back.LIGHTWHITE_EX)
  print("""Thanks for playing!🐍
  Made on Python
  Powered by PyCharm
  Made by Gadiuka
  
  🐍Special thanks for Python and PyCharm""")