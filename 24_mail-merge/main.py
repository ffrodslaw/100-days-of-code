#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as n:
    names = n.readlines()

with open("Input/Letters/starting_letter.txt") as sl:
    starting_letter = sl.read()

for n in range(len(names)-1):
    # delete \n in names
    names[n] = names[n].replace("\n", "")
    # replace placeholder with name in every letter
    output = starting_letter.replace("[name]", names[n])
    # save every letter in separate txt
    with open(f"Output/ReadyToSend/{names[n]}.txt", mode="w") as o:
        o.write(output)
