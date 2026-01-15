def is_palindrome(string):
    rev=string[::-1]
    if rev==string:
        print('Is palindrome')
    else:
        print('Not palindrome')

is_palindrome('ABA')