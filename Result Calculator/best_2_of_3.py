"""
The script reads a CSV file containing data of internal result of students.
It creates a file which contains the sum of two best of three internal marks
for each student.
"""
"""Required modules"""
import csv

#-----------------------------------------------------------------------------------------------------
def collect_data(csv_file):
	"""
	(file) -> {dictionary_of_calculated_sum_of_two_best_of_three}
	It takes input as a CSV file and returns a dictionary which contains name of student and the sum
	of the best two out of three internal marks of them.
	"""
	marks_dict = {}
	try:
	    reader = csv.reader(open(csv_file))

	    #To mark the header row.
	    c=True
	    for row in reader:
	    	#If it is header row.
	        if c:
	            c=False
	        else:
	        	#Empty list for collecting marks.
		    	marks = []
		    	for i, col in enumerate(row):

		    		#The name of student.
		    	    if i == 0:
		    	    	marks_dict[col] = 0
		    	    	name = col

		    	    #Marks columns
		    	    else:
		    	    	marks.append(int(col))

		    	#Calculate sum
		        marks_dict[name] = calculate_sum(marks)

	except IOError as e:
		print e

	return marks_dict

#-----------------------------------------------------------------------------------------------------
def calculate_sum(marks):
	"""
	Takes a list of marks and returns the sum of best two.
	"""
	try:
		return sum(marks)-min(marks)
	except:
		print "The data is not appropriate."

#-----------------------------------------------------------------------------------------------------
def create_file(students):
	"""
	Creates a file with output data.
	"""
	with open('result.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')

		#The header row.
		writer.writerow(['Name', '	Marks'])

		#Rest of the rows with student name and their total.
		for name in students:
			writer.writerow([name,students[name]])

#-----------------------------------------------------------------------------------------------------
def main(csv_file):
	"""
	Main module.
	"""
	students = collect_data(csv_file)
	create_file(students)

#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	try:
		filename = raw_input("Enter the file name: ")
		main(filename)
	except:
		main("example.csv")