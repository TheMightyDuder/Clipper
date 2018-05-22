unformatted_text = input("Enter the text you wish to format: ")
special_character = input("Enter the character you would like to format by: ")

formatted_text = ""

for character in unformatted_text:
    if(character != special_character):
        formatted_text += character

print("Here is the formatted text: " + formatted_text)