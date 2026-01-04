available_parts=["Exit",
                "Computer",
                "CPU",
                "Keyboard",
                "Printer",
                "Mouse",
                "HDMI Cable"
                 "Exit"
                 ]
current_choice="-"
computer_parts = []
valid_choices=[]
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != '0':
    if current_choice in valid_choices:

        index =int(current_choice)
        chosen_part=available_parts[index]
        if chosen_part in computer_parts:
            print(f'Removing {current_choice}')
            computer_parts.remove(chosen_part)
        else:
            print(f'Adding {current_choice}')
            computer_parts.append(chosen_part)
        print(f'Your list contains {computer_parts}')
        # if current_choice == '1':
        #     computer_parts.append('Monitor')
        # elif current_choice == '2':
        #     computer_parts.append('CPU')
        # elif current_choice == '3':
        #     computer_parts.append('Keyboard')
        # elif current_choice == '4':
        #     computer_parts.append('printer')
        # elif current_choice == '5':
        #     computer_parts.append('Mouse')
        # elif current_choice == '6':
        #     computer_parts.append('HDMI Cable')
    else:
        print('Please add the options below')
        for index,part in enumerate(available_parts):
            print(f'{index} :', part)


    current_choice=input()
print(computer_parts)

