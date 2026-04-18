# Variable sin cadena para guardar las letras
word_without_vowels = "" 

# 1. Pedir al usuario que ingrese una palabra  "murcielago"
user_word = input("Ingresa una palabra: ")

# 2. Convertir la palabra a mayúsculas
user_word = user_word.upper()


for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter
    
print(word_without_vowels)
        
    
    
    