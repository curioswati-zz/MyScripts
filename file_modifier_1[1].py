filename = raw_input("enter filename: ")
old_file = open(filename,"r")
    
is_first_occurence = True

lines_in_file = old_file.readlines()                        
old_file.close()
     
old_file = open(filename,"w")
        
for line in lines_in_file:
    new_line=line
    if is_first_occurence:
        location_of_var = line.find("require once")
        is_first_occurence = False
    else:
            location_of_var = line.find("require once",location_of_var+1)
    if location_of_var != -1:
        length_of_word = len("require once")
        add_the_text_at = location_of_var + length_of_word
        new_line = line[:add_the_text_at+1]+"text"+line[add_the_text_at:]
    old_file.write(new_line)                                     
      
old_file.close()
