import numpy as np #to help with grouping data (using arrays)
import matplotlib.pyplot as plt #helps display the information created from the numpy arrays using graphs 

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# November 19, 2019                               |
# Kristoff Finley                                 |
# -------------------------------------------------
#This program reads data from a file consisting of Montana
#State University Departments and students enrolled in those
#departments, presenting the data as a matplotlib bar graph

def read_file(file_name): #reads the data from the file in 
    i = 0
    data = open(file_name, 'r')
    for line in data:
        sections = int(line[0])
        college_array = np.empty(sections, dtype = object) #creating an empty array for different departments 
        enrollment_array = np.zeros(sections) #creating an empty array for enrollment statistics 
        break

    #Comma splitting the data and then adding it to the seperate arrays using a for loop 
    for line in data:
        line = line.split(',') 
        line[1] = line[1][:-1]
        college_names = line[0]
        college_array[i] = college_names 
        enrollment_array[i] = line[1]
        i +=1
    return college_array, enrollment_array #returns a tuple of the college department and statistic array, respectively
            
# -------------------------------------------------

def main(file_name):
    i = 0
    read_file(file_name) #reads in the file 
    college_names, college_enrollments = read_file(file_name) #gets the results from the read_file method 
    print(college_names)
    print(college_enrollments)

    #uses components of the matplotlib library to costomize a graph and present the information in a readable manner
    plt.figure("Montana State University Fall 2019 Enrollments")
    plt.bar(college_names, college_enrollments, width = 0.8, color = ["blue", "gold"])
    plt.yticks(ticks = np.arange(0,4800, 400))
    plt.ylim(0,4400)

       
    plt.xlabel("College Name")
    plt.ylabel("College Enrollment")
    
    plt.show()#shows the graph to the user

# -------------------------------------------------

main("fall-2019.csv")
