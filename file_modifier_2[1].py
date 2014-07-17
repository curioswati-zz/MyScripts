import os

for each_file in os.listdir(r'./'):
    #opening the file for reading
    old_file = open(each_file,"r")
    
    is_first_occurence = True

    lines_in_file = old_file.readlines()                        #lines in the file as a list of strings; where each string is a line
    old_file.close()

    #opening the file for writing the modified version
    old_file = open(each_file,"w")

    #iterating over the lines_in the file as strings.
    for line in lines_in_file:
        new_line=line
        if is_first_occurence:                                  #for the first occurence of the word 
            location_of_var = line.find("require once")
            is_first_occurence = False
        else:
            location_of_var = line.find("require once",location_of_var+1)
        if location_of_var != -1:                               #text found
            length_of_word = len("require once")
            add_the_text_at = location_of_var + length_of_word
            new_line = line[:add_the_text_at+1]+"text"+line[add_the_text_at:]
        old_file.write(new_line)                                #writing the modified line to the file     
      
    old_file.close()
                                        
