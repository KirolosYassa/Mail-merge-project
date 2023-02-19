# import regex as re

# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt", mode="r") as starting_file:
    letter = starting_file.read()
content = ""
# for line in letter:


with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

for name in names:
    new_name = name.strip()
    new_letter = letter.replace("[name]", new_name)
    # print(s.replace(' ', '-'))
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as file:
        file.write(new_letter)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
