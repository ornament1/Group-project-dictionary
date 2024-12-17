# Spanish to English dictionary
spanish_to_english = {
    "hola": "hello",
    "adiós": "goodbye",
    "por favor": "please",
    "gracias": "thank you",
    "sí": "yes",
    "no": "no",
    "buenos días": "good morning",
    "buenas tardes": "good afternoon",
    "buenas noches": "good night",
    "¿cómo estás?": "how are you?",
    "bien": "well",
}


def translate(spanish_word):
    return spanish_to_english.get(spanish_word, "Translation not found")


def main():
    print("Welcome to the Spanish to English translator!")
    print("Type 'exit' to quit the program.")

    while True:
        spanish_word = input("Enter a Spanish word: ").strip().lower()
        if spanish_word == 'exit':
            print("Goodbye!")
            break
        translation = translate(spanish_word)
        print(f"The English translation of '{spanish_word}' is: '{translation}'")


if __name__ == "__main__":
    main()