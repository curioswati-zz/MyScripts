import os

def in_dir(dir_):
    #for each subdir in input directory
    for each_file in os.listdir(dir_+"/"):

        #if the current item is not a dir
        if not os.path.isdir(each_file):
            if each_file[5:9] == '.txt':
                #opening the file for reading
                old_file = open(dir_+"/"+each_file,"r")                                     

                if not old_file:
                    print "couldn't open"
                    
                is_first_occurence = True
                
                #lines in the file as a list of strings; where each string is a line
                lines_in_file = old_file.readlines()                                         
                old_file.close()
                
                #opening the file for writing the modified version
                old_file = open(dir_+"/"+each_file,"w")                                      

                #iterating over the lines_in the file as strings.
                for line in lines_in_file:                                                     
                    new_line=line
                    #if the first occurence of the word
                    if is_first_occurence:                                                    
                        location_of_var = line.find("require once")
                        is_first_occurence = False
                    else:
                        location_of_var = line.find("require once",location_of_var+1)    
                    if location_of_var != -1:        #text found                                        
                        length_of_word = len("require once")
                        add_the_text_at = location_of_var + length_of_word
                        new_line = line[:add_the_text_at+1]+"text"+line[add_the_text_at:]
                    #writing the modified line to the file    
                    old_file.write(new_line)                                                      
                old_file.close()
        else:
            #recursively descending the directory structure
            in_dir(dir_+"/"+each_file)
in_dir(r'.')
