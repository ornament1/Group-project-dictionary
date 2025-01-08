from tkinter import *
import tkinter.messagebox as messagebox

# Dictionary of languages and their translations
languages = {
    "Spanish": {
        "hello": "hola",
    "goodbye": "adiós",
    "please": "por favor",
    "thank you": "gracias",
    "yes": "sí",
    "no": "no",
    "cat": "gato",
    "dog": "perro",
    "house": "casa",
    "food": "comida",
    "water": "agua",
    "friend": "amigo",
    "family": "familia",
    "love": "amor",
    "school": "escuela",
    "book": "libro",
    "car": "coche",
    "city": "ciudad",
    "happy": "feliz",
    "sad": "triste",     
    },
"Portugese": {
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
    "beautiful": "bonito",
   },
"Hausa": {
    "Kaya": "Goods",
    "Gida": "House",
    "Lafiya": "Health",
    "Kuɗi": "Money",
    "Abinci": "Food",
    "Tafiya": "Journey",
    "Mutum": "Person",
    "Hannu": "Hand",
    "Ruwa": "Water",
    "Zuciya": "Heart",
    "Duniya": "World",
    "Shekara": "Year",
    "Idanu": "Eyes",
    "Yaro": "Boy",
    "Mace": "Woman",
    "Namiji": "Man",
    "Farin Ciki": "Happiness",
    "Tarihi": "History",
    "Ilimi": "Knowledge",
    "Gaskiya": "Truth",
},
"German": {
    "hello": "hallo",
    "goodbye": "tschüss",
    "please": "bitte",
    "thank you": "danke",
    "yes": "ja",
    "no": "nein",
    "good morning": "guten Morgen",
    "good evening": "guten Abend",
    "good night": "gute Nacht",
    "friend": "freund",
    "family": "familie",
    "house": "haus",
    "food": "essen",
    "water": "wasser",
    "book": "buch",
    "school": "schule",
    "work": "arbeit",
    "car": "auto",
    "dog": "hund",
    "cat": "katze",
    "love": "liebe",
},
"Zulu": {
     "hello": "sawubona",
    "goodbye": "hamba kahle",
    "please": "ngiyacela",
    "thank you": "ngiyabonga",
    "yes": "yebo",
    "no": "cha",
    "friend": "umngane",
    "family": "umndeni",
    "house": "indlu",
    "food": "ukudla",
    "water": "amanzi",
    "book": "incwadi",
    "school": "isikole",
    "work": "umsebenzi",
    "car": "imoto",
    "dog": "inja",
    "cat": "ikati",
    "love": "uthando",
    "city": "idolobha",
    "life": "impilo",
},
"deutsch" = { 
    "hallo":"hello",                               
    "danke":"thanks",                              
    "auf wiedersehen":"goodbye",                   
    "ja":"yes",                                    
    "nein":"no",                                   
    "haus":"house",                                
    "familie":"family",                            
    "essen":"food",                               
    "wasser":"water",                               
    "currywurst":"curry sausage",                  
    "vorwarts":"forward",                          
    "schwarz":"black",                             
    "flughafen":"airport",                         
    "kaufhaus":"department store",                 
    "schnitzel":"breaded and fried meat",          
    "u-bahn":"subway",                             
    "hilfe":"help",                                
    "auto":"car",                                  
    "trauer":"sorrow",                             
    "schokolade":"chocolate"                       
}                                               
}

def translate():
    selected_language = languages_var.get()
    word = word_entry.get().strip().lower()

    if selected_language in languages and word in languages[selected_language]:
        translation = languages[selected_language][word]
        messagebox.showinfo("Translation", f"{word} in {selected_language}: {translation}")
    else:
        messagebox.showwarning("Warning", "Word not found or language not supported.")

# Create the main window
root = Tk()
root.title("Multi-Language Translator")

# Create and pack widgets
Label(root, text="Enter an English word:").pack(pady=10)
word_entry = Entry(root, width=30)
word_entry.pack(pady=10)

# Dropdown for language selection
languages_var = StringVar(value="Select Language")
OptionMenu(root, languages_var, *languages.keys()).pack(pady=10)

# Button to trigger translation
Button(root, text="Translate", command=translate).pack(pady=20)

# Run the application
root.mainloop()

   
       
