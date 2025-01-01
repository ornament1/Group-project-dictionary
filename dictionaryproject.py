# English to Portuguese translation dictionary
translations = {
    "hello": "olá",
    "goodbye": "adeus",
    "please": "por favor",
    "thank you": "obrigado",
    "yes": "sim",
    "no": "não",
    "cat": "gato",
    "dog": "cão",
    "friend": "amigo",
    "love": "amor",
    "food": "comida",
    "water": "água",
    "house": "casa",
    "car": "carro",
    "book": "livro",
    "school": "escola",
    "family": "família",
    "happy": "feliz",
    "sad": "triste",
    "beautiful": "bonito"
}

# Function to display all translations
def translate_all():
    print("English to Portuguese Translations:")
    for english, portuguese in translations.items():
        print(f"{english}: {portuguese}")

# Main execution
if __name__ == "__main__":
    translate_all()