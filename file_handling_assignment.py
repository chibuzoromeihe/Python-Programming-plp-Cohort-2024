#Opening my_file.txt in write mode  writng three new lines
with open('my_file.txt', 'w') as file:
    file.write("Good morning Ben, how are you today?\n")
    file.write("How much is your price, $300,00 take $250,00 \n")
    file.write("Deal done, thank you\n")
    
    
 # file reading and display
try:
    with open('my_file.txt', 'r') as file:
         contents = file.read()
    print(contents)
    
except(FileNotFoundError, PermissionError) as e:
    print(f"Error occured while reading file : {e}")
    
    
    
#File appending; Opening my_file.txt in append mode to add addditonal three line of text
try:
    with open('my_file.txt', 'a') as file:
        file.write("I love your product. \n")
        file.write("May I have more delivered tomorow.\n")
        file.write("Sure! you will get your pay.\n")
    
except(FileNotFoundError, PermissionError):
    print(f"An error occured while appending file: {e}")
        
        


    
