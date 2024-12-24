ENTRY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ROTOR_I = ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
ROTOR_II = ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
ROTOR_III = ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
ROTOR_IV = ('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
ROTOR_V = ('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')

class Rotor:

    __rotor: str
    __entry: str

    __notch: str

    # TODO: figure out how to incorporate the ring
    __ring_setting: str


    def __init__(self, rotor: tuple, ring_setting: str, initial_position: str):
        
        # Set the rotor, the notch, and the entry (alphabet in order)
        self.__rotor = rotor[0]
        self.__notch = rotor[1]
        self.__entry = ENTRY #TODO Come up with a better name
        
        # Set the ring setting and the initial position of the rotor
        self.__ring_setting = ring_setting
 
        # Set the rotor based on the initial position
        self.__set_rotor(ENTRY.find(initial_position))

    def __set_rotor(self, index = 1) -> None:
        """Used for establishing the initial setting of the rotor at installation, as well as to rotate the rotor each step

        Args:
            index (int, optional): Rotates the rotor by the given amount. Defaults to 1.
        """

        self.__rotor = self.__rotor[index:] + self.__rotor[:index]
        self.__entry = self.__entry[index:] + self.__entry[:index]

    def right_to_left(self, letter: str) -> str: #TODO better name for the right to left function

        # The enigma machine rotates the rotor first when the button is clicked
        self.rotate()

        # Get the index of the letter coming in (ie A = 0, B = 2, etc)
        keyboard_index = ENTRY.find(letter)

        # Find the rotor letter 
        inner_letter = self.__rotor[keyboard_index]

        # Get the index of the rotor letter based on it's internal order
        rotor_index = self.__entry.find(inner_letter)

        # Return the letter that is at the index of the rotor letter in the actual alphabet
        return ENTRY[rotor_index]

    # TODO combine rotate function and set rotor functions
    def rotate(self):

        self.__set_rotor()


if __name__ == "__main__":
    r = Rotor(ROTOR_I, "A", "L")
    
    for _ in range(5):
        print(r.right_to_left("A"))


    

    