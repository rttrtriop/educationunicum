from Model import plus, minus, multiply, divide, square, volume
from View import display_menu, get_numbers, get_numbers_for_volume, show_result, show_message

def main():
    while True:
        choice = display_menu()

        if choice == "1":
            num1, num2 = get_numbers()
            plus(num1, num2, show_result)
        elif choice == "2":
            num1, num2 = get_numbers()
            minus(num1, num2, show_result)
        elif choice == "3":
            num1, num2 = get_numbers()
            multiply(num1, num2, show_result)
        elif choice == "4":
            num1, num2 = get_numbers()
            divide(num1, num2, show_result)
        elif choice == "5":
            num1, num2 = get_numbers()
            square(num1, num2, show_result)
        elif choice == "6":
            num1, num2, num3 = get_numbers_for_volume()
            volume(num1, num2, num3, show_result)
        elif choice == "0":
            break
        else:
            show_message("Неверный выбор, попробуй снова")

#if name == "main":
main()
