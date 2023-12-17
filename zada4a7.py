smallest_number = None

while True:
        user_input = input("Въведете число или 'END' за край: ")

        if user_input == "END":
            break

        current_number = float(user_input)

        if smallest_number is None or current_number < smallest_number:
            smallest_number = current_number

if smallest_number is not None:
    print(f"Най-малкото число е: {smallest_number}")
else:
    print("Няма въведени числа.")