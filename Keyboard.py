class Keyboard():
    """Class repesenting the keyboard of the Enigma machine. The purpose to just to insure that only uppercase alpha characters are entered.

    """
    def keypress(self, key: str) -> str:
        """Method to check if the key pressed is a valid key. If it is, it returns the key in uppercase, otherwise it returns an empty string.

        Args:
            key (str): The key pressed by the user
        """
        key = key.upper()
        if key.isalpha():
            return key
        else:
            return ''

if __name__ == "__main__":
    print('Testing Keyboard')
    kb = Keyboard()
    foo = input('Enter a key: ')
    print(kb.keypress(foo))
