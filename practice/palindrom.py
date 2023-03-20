word = input("Ingrese una palabra: ").replace(" ", "").lower()
reverse_word = word[::-1].replace(" ", "").lower()
palindrom = "No es palindromo"
if word == reverse_word:
  palindrom = "Es palindromo"
  
print(palindrom)