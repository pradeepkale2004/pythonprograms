def banner_text(text):
    screen_width=80
    if len(text) > screen_width-4:
        raise ValueError(f'{text} is larger than specified width of {screen_width}')

    if text == '*':
        print('*' * screen_width )
    else:
        centered_text=text.center(screen_width-4)
        output_string = f'**{centered_text}**'
        print(output_string)

banner_text('*')
banner_text('Always look on the bright side of life..')
banner_text('if lif seems jolly rotten')
banner_text("There's something you've forgotten! ")
banner_text(' ')
banner_text('WHen you are feeling in the dumps,')
banner_text("Don't be silly chums")
banner_text('*')