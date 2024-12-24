class ExceededMaximumPLugsError(Exception):
    def __init__(self, plugs, message = "Enigma can utilize a maximum of 10 plugs"):
        self.plugs = plugs
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Exceeded maximum plugs: {self.plugs}"
    
class PlugAlreadyUsedError(Exception):
    def __init__(self, letter, message = "A plug already exists for the letter"):
        self.letter = letter
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Tried to insert a plug into a occupied location: {self.letter}"

class InvalidPlugError(Exception):
    def __init__(self, message = "No plug for that letter combination"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Tried to remove a plug that doesn't exist"