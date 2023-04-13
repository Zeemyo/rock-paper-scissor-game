rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

game_image = [rock, paper, scissors]

player_choice = int(
    input("Pilih angka 0 untuk batu, 1 untuk kertas, 2 untuk gunting! \n"))

if player_choice >= 3 or player_choice < 0:
    print("Angka yang anda masukkan tidak sesuai!")
else:
    print(f"Kamu memilih: {player_choice}")
    print(game_image[player_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer memilih: {computer_choice}")

    print(game_image[computer_choice])

    if player_choice == computer_choice:
        print("Seri!")
    elif player_choice == 0 and computer_choice == 1:
        print("Computer Menang!")
    elif player_choice == 0 and computer_choice == 2:
        print("Player Menang!")
    elif player_choice == 1 and computer_choice == 0:
        print("Player Menang!")
    elif player_choice == computer_choice:
        print("Seri!")
    elif player_choice == 1 and computer_choice == 2:
        print("Computer Menang!")
    elif player_choice == 2 and computer_choice == 0:
        print("Computer Menang!")
    elif player_choice == 2 and computer_choice == 1:
        print("Player Menang!")
    elif player_choice == computer_choice:
        print("Seri!")
