"""String basic exercises."""


# 1. Sõne-tüüpi muutujate deklareerimine
first_name = "James"
last_name = "Bond"

# 2. Sõnede konkatenatsioon (liitmine)
full_name = first_name + " " + last_name
self_description_sentence = f"My name is {last_name}, {first_name} {last_name}."

# 3. Sõnede tükeldamine
original_string = "Programming is fun!"
backwards = original_string[::-1]
every_other = original_string[::2]
first_word_reversed = original_string[10::-1]

# 4. Mitmerealised sõned
cake = "toppingfillingbase"
print(f"{cake[:7]}\n{cake[7:14]}\n{cake[14:]}")
