available_parts = { "1": "computer",
                    "2": "monitor",
                    "3": "keyboard",
                    "4": "mouse",
                    "5": "hdmi cable",
                    "6": "dvd drive",
                    }
current_choice = None
current_list = []
while current_choice != '0':
    if current_choice in available_parts:
        current_choice = available_parts[current_choice]
        print('adding',{current_choice})
        current_list.append(current_choice)
    else:
        print('Add product from the list from the list')
        for key, value in available_parts.items():
            print(key,': ',value)
        print('0 : to finish')
    current_choice = input('>')
print('Selected items are',end='')
print(current_list)