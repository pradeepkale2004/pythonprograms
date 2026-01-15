def banner_text(text):
    screen_Width=80
    if len(text) > screen_Width-4:
        print('EEK!!')
        print('The text is too long to fir in the specified width')

    if text == '*':
        print('*' * screen_Width )
    else:
        centered_text=text.center(screen_Width-4)
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