import random

def get_user_choice():
    while True:
        user_choice = input("Wybierz kamień (k), papier (p) lub nożyce (n): ").lower()
        if user_choice in ['k', 'p', 'n']:
            return user_choice
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def get_computer_choice():
    return random.choice(['k', 'p', 'n'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Remis!"
    elif (user_choice == 'k' and computer_choice == 'n') or \
         (user_choice == 'p' and computer_choice == 'k') or \
         (user_choice == 'n' and computer_choice == 'p'):
        return "Wygrałeś!"
    else:
        return "Przegrałeś."

def main():
    print("Witaj w grze Kamień, Papier, Nożyce!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Twój wybór: {user_choice}")
        print(f"Wybor komputera: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Czy chcesz zagrać ponownie? (tak/nie): ").lower()
        if play_again != 'tak':
            print("Dziękujemy za grę!")
            break

if name == "main":
    main()