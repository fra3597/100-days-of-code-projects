
WORD_TO_MORSE_MODE = "1"
MORSE_TO_WORD_MODE = "2"
MORSE_CODE_COMPLETED = "q"

morse_code_dict = {
    "a":"._",
    "b":"_...",
    "c":"_._.",
    "d":"_..",
    "e":".",
    "f":".._.",
    "g":"__.",
    "h":"....",
    "i":"..",
    "j":".___",
    "k":"_._",
    "l":"._..",
    "m":"__",
    "n":"_.",
    "o":"___",
    "p":".__.",
    "q":"__._",
    "r":"._.",
    "s":"...",
    "t":"_",
    "u":".._",
    "v":"..._",
    "w":".__",
    "x":"_.._",
    "y":"_.__",
    "z":"__..",
    "1":".____",
    "2":"..___",
    "3":"...__",
    "4":"...._",
    "5":".....",
    "6":"_....",
    "7":"__...",
    "8":"___..",
    "9":"____.",
    "0":"_____"
}
reversed_code_dict = {value: key for key, value in morse_code_dict.items()}

def get_morse_code():
    converted_morse_code = []
    is_valid = False
    input_message = """Select one letter at the time. There are a few rules to follow:
    1 - Only characters allowed: '_' and '.'
    2 - The input must be less than or equal than 5 characters
    3 - Type 'q' when you are done with the Morse Code to be converted
    Type here your Morse Code: 
    """

    next_letter = (input(input_message)).lower()
    while True:
        if next_letter == MORSE_CODE_COMPLETED:
            is_valid = True
            return converted_morse_code, is_valid
        elif next_letter not in reversed_code_dict or len(next_letter) > 5 or next_letter == "":
            return converted_morse_code, is_valid
        else:
            converted_morse_code.append(reversed_code_dict[next_letter])
            next_letter = (input(input_message)).lower()




def game_on():
    selected_mode = input("Select the conversion mode, type '1' for Word to Morse Code or '2' for Morse Code to Word: ")
    
    if selected_mode == WORD_TO_MORSE_MODE:
        converted_word = []
        word_to_convert = input("Type the word you want to convert (The characters allowed are only the standard letters of the English alphabet and numbers): ")
        for char in word_to_convert:
            lower_char = char.lower()
            if lower_char in morse_code_dict:
                converted_word.append(morse_code_dict[char.lower()])
            else:
                print(f"Key '{lower_char}' not found. Try again!")
                game_on()
        print(f"The converted Word is: {converted_word}")

    elif selected_mode == MORSE_TO_WORD_MODE:
        final_word = ""
        converted_morse_code, is_valid = get_morse_code()

        if is_valid:
            for letter in converted_morse_code:
                final_word += letter
            print(f"The converted Morse Code is: {final_word}")
                
        else:
            print(f"Something was wrong with your input. Try again!")
            game_on()


if __name__ == "__main__":
    game_on()

