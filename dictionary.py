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
    # Create a dictionary of Mandarin words and their English translations
    mandarin_dictionary = {
        "你好": "Hello",
        "谢谢": "Thank you",
        "再见": "Goodbye",
        "是": "Yes / To be",
        "不是": "No / Not to be",
        "请": "Please",
        "对不起": "Sorry",
        "没关系": "It's okay / No problem",
        "我": "I / Me",
        "你": "You",
        "他": "He / Him",
        "她": "She / Her",
        "我们": "We / Us",
        "他们": "They / Them",
        "好": "Good",
        "坏": "Bad",
        "大": "Big",
        "小": "Small",
        "水": "Water",
        "食物": "Food"
    }

    # Print the dictionary
    for mandarin, english in mandarin_dictionary.items():
        print(f"{mandarin}: {english}")