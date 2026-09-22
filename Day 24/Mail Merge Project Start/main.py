#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = [name.strip("\n") for name in file.readlines()]

for name in names:
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as data:
        with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
            letter = file.readlines()

        # replace [name] with actual name
        letter[0] = letter[0].replace("[name]", name)
        new_letter = ' '.join(letter)

        # writing the updated letter with names
        data.write(new_letter)


