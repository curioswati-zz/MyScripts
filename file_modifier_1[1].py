'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''This script will modify all the files in the current directory.
It works recursively on all subdirectories.
It will insert the input string on a required place as mentioned with respect to some text.''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''
'''Required Modules'''
''''''''''''''''''''''''''''''''''''''''''''
import os

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''Reads the input file, and returns a list of the lines in file.
Each line is a string.''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def read_file(input_file):
    try:
        inputFile = open(input_file,'r')                                  #opening the input_file for reading.
        return inputFile.readlines()
    except:
        print "There was some problem with file "+input_file+"."          #if any file not exist or fails to open, The program will not stop.
        
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''Writes the input lines in the out_file.
The out_file is the one that was read earlier in read_file().''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def write_file(out_file,lines):
    with open(out_file,'w') as outFile:
        for line in lines:
            outFile.write(line)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''Modifies a line by placing some text on a location after some text.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def modify_line(line,location):                                                            
    new_line=line
    location = line.find("require once",location)
    if location != -1:                                                    #text found
        length_of_word = len("require once")
        add_the_text_at = location + length_of_word
        new_line = line[:add_the_text_at+1]+"text"+line[add_the_text_at:] #new_line, assigned the old line with insertion of the text.
    return new_line,location+1                                            #returning the new_line with the location after, text was found.  


'''''''''''''''''
The main module
'''''''''''''''''
def main(dir_):              
    for each_file in os.listdir(dir_+"/"):                                #for each file in input dir_.       
        if not os.path.isdir(each_file):                                  #if the file is not a directory.  
            file_extension = each_file[5:9]

            if file_extension == '.txt':
                lines_in_file = read_file(dir_+"/"+each_file)             #reading file                                
                lines_to_write = []                                       #list to write new lines        
                location_of_text = 0 
                                               
                for line in lines_in_file:                                #iterating over the lines_in_file.
                    line, location_of_text = modify_line(line,location_of_text)
                    lines_to_write.append(line)                           #appending the line to list
                    
                write_file(dir_+"/"+each_file, lines_to_write)            #writing the new lines to file.
        else:
            main(dir_+"/"+each_file)                                      #Go through the subdirectory.
main(r'.')                                                                #calling the main() with current directory
