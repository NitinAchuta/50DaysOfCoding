#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#All names are in the names list
with open('Mail Merge Project Start/Input/Names/invited_names.txt') as names:
    all_names = names.readlines()
    names = []
    for line in all_names:
        name = line.strip()
        names.append(name)
        
#Write the new letter
with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_lines = letter.read()

for name in names:
    new_letter = letter_lines.replace('[name]', name)
    with open(f'Mail Merge Project Start/Output/ReadyToSend/{name}_letter.txt', 'w') as current_letter:
        current_letter.write(new_letter)

