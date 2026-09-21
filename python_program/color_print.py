BLACK = '\u001b[30m'
RED ='\u001b[31m'
GREEN ='\u001b[32m'
YELLOW ='\u001b[33m'
BLUE = '\u001b[34m'

BOLD ='\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(BLACK,"This will be in black")
print(RED,BOLD, "This will be in reed")
print(YELLOW, "This will be in Yellow")
print(BLUE,"This will be in Blue")
print(GREEN,"This will bw in GREEN")

def color_print(text :str, effect: str) -> None:
    """
    print `text` using the ANSI sequence to change colour, etc

    :param text: The text to print
    :param effect: the effect we want. One of the constants
         defined at the start of the module.
    """
    output_string = "{0}{1}{2}".format(effect, text,RESET)
    print(output_string)

color_print("Hello, Red", RED)
print('This should be in the default terminal colour')