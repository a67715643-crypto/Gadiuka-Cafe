import colorama

while True:

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

 print('balance: ' + str(balance))
 print('coffee: ' + str(coffee))
 print('tea: ' + str(tea))
 print('cookies: ' + str(cookies))
 print('pie: ' + str(pie))

 c_i = input('Customer:')

 if c_i == 'coffee':
    balance = balance - coffee
    print('Balance: ' + str(balance))

    if balance < coffee:
        print('Sorry, but you do not have enough money!')

 else:

  if c_i == 'tea':
    balance = balance - tea
    print('Balance: ' + str(balance))

    if balance < tea:
        print('Sorry, but you do not have enough money!')

  else:

   if c_i == 'cookies':
    balance = balance - cookies
    print('Balance: ' + str(balance))

    if balance < cookies:
        print('Sorry, but you do not have enough money!')

   else:
    if c_i == 'pie':
      balance = balance - pie
      print('Balance: ' + str(balance))

      if balance < pie:
          print('Sorry, but you do not have enough money!')

      break