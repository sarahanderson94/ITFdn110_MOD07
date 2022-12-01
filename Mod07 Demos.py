# ------------------------------------------------- #
# Title: Demos - Exception Handling and Pickling
# Description: program to demo exception handling and
#     pickling. Divides values entered by a user and saves
#     the data to a pickle file.
# ChangeLog: (Who, When, What)
# Sarah Anderson,11.27.2022,Created Script
# ------------------------------------------------- #

# ...... Data ......
strFile = ""
dataObject = []  # declare list
row = {}  # declare dictionary


# ------- Processing ------------
def divide():
    """
    Function takes two user inputted values and divides them.
    Returns number1, number2, and the quotient

    """
    num1 = float(input("Enter a first number: "))
    num2 = float(input("Enter a second number: "))
    quotient = num1 / num2
    return num1, num2, quotient


def importfile():
    """
    Imports a text file and loads data to a table.
    User enters the name of the text fil

    """
    try:
        strFile = input("Please enter a txt file name: ")
        if not strFile.endswith("txt"):
            raise Exception('Incorrect file name. Text file should end with .txt')
        f = open(strFile, "r")
        for row in f:
            # removes the comma between elements in the text file
            lstRow = row.split(",")
            # use strip function to remove the \n from printing out
            lstRow = {"number01": lstRow[0].strip(), "number02": lstRow[1].strip(), "quotient": lstRow[2].strip()}
            dataObject.append(lstRow)
        f.close()
    except IOError:
        print("File not found")
    return dataObject


# ------ Presentation ---------------

dataObject = importfile()
print("Data loaded from file:")
print(dataObject)
print("\n")
print("Division Demo: Enter two numbers to get the quotient\n")

try:
    num1, num2, quotient = divide()
    row = {"number01": num1, "number02": num2, "quotient": quotient}
    dataObject.append(row)
except ValueError:
    print("ERROR: Please enter a number")
except ZeroDivisionError:
    print("ERROR: Can't divide by zero. Second number should not be 0")
except Exception as e:
    print("ERROR: There was a non specific error!")
    print("Python Error Info: ")
    print(e, type(e), sep='\n')

print(dataObject, sep='\n')
print("\n")

# Pickle Data
print("Save Data to Pickle File\n")

import pickle
pickleFile = open("quotient.dat", "wb")
pickle.dump(dataObject, pickleFile)
pickleFile.close()

# Read data from the Pickle File
openPickle = open("quotient.dat", "rb")
data = pickle.load(openPickle)
openPickle.close()
print("Read data from pickle file: ")
print(data)


