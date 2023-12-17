max_number = None

while True:
        user_input = input("Въведете число или 'END' за край: ")

        if user_input == "END":
            break

        current_number = float(user_input)

        if max_number is None or current_number > max_number:
            max_number = current_number

if max_number is not None:
    print(f"Най-голямото число е: {max_number}")
else:
    print("Няма въведени числа.")