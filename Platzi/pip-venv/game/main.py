#!/usr/bin/env python3
# Python3 rock paper, sisors game

import random

def choose_options():
  options = ('rock', 'paper', 'scissors')
  user_option = input('rock, paper or scissors => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('Invalid option')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('User option:', user_option)
  print('Computer option:', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Tie!')
  elif user_option == 'rock':
    if computer_option == 'scissors':
      print('Rock beats Scissors')
      print('User won!')
      user_wins += 1
    else:
      print('Paper beats Rock')
      print('Computer won!')
      computer_wins += 1
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('Paper beats Rock')
      print('User won!')
      user_wins += 1
    else:
      print('Scissors beats Paper')
      print('Computer won!')
      computer_wins += 1
  elif user_option == 'scissors':
    if computer_option == 'paper':
      print('Scissors wins Paper')
      print('User won!')
      user_wins += 1
    else:
      print('Stone beats Scissors')
      print('Computer won!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('Computer is the Winner!')
      break

    if user_wins == 2:
      print('User is the Winner!')
      break

run_game()