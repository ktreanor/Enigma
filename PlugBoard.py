from Enigma_Errors import *

MAX_PLUGS = 10

class PlugBoard():

    __plug_count: int
    __plug_board: dict

    def __init__(self):

        self.__plug_count = 0
        self.__plug_board = {}

    def Add_Plug(self, plug_left_end: str, plug_right_end: str) -> None:
        """Adds a plug to the plug board. Plugs perform simple letter substitution by swapping letters that are "plugged" together, so for example A->Z and Z->A

        Args:
            plug_left_end (str): Letter to connect the left side of the plug to
            plug_right_end (str): Letter to connect the right side of the plug to

        Raises:
            EnigmaMaximumPlugError: The plug board can have a maximum of 10 plugs
        """

        self.__plug_count += 1

        # Throw an error if more than 10 plugs are added
        if self.__plug_count > MAX_PLUGS:
            raise ExceededMaximumPLugsError(self.__plug_count)

        # TODO Check for plug already in use and throw error

        # The plugboard swaps letters so the dictionary has to have entries for both letters, A->Z and Z->A
        self.__plug_board[plug_left_end] = plug_right_end
        self.__plug_board[plug_right_end] = plug_left_end


    def Remove_Plug(self, plug_left_end: str, plug_right_end: str):

        if plug_left_end in self.__plug_board and plug_right_end in self.__plug_board:
            del self.__plug_board[plug_left_end]
            del self.__plug_board[plug_right_end]
        else:
            raise InvalidPlugError()

        self.__plug_count -= 1

    def into_plugboard(self, input: str) -> str:
        
        # Create a translation table from the dictionary
        plug_table = str.maketrans(self.__plug_board)

        # The translate function will swap letters in the dictionary
        return input.translate(plug_table)


if __name__ == "__main__":

    # Testing general functionality 

    plug = PlugBoard()
    plug.Add_Plug('A', 'Z')

    print('With plug A to Z')
    print(f'Z -> {plug.into_plugboard('Z')}')
    print(f'A -> {plug.into_plugboard('A')}')
    print(f'D -> {plug.into_plugboard('D')}')
    print()

    plug.Remove_Plug('A', 'Z')

    print('Removed plug A to Z')
    print(f'Z -> {plug.into_plugboard('Z')}')
    print(f'A -> {plug.into_plugboard('A')}')
    print(f'D -> {plug.into_plugboard('D')}')
    print()

    # Should throw an exception 
    try:
        plug.Remove_Plug('C', 'G')
    except InvalidPlugError as e:
        print(f'Error: {e}')




