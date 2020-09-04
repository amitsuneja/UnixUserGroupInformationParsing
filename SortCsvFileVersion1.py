import os
import csv
from csv import writer

# Define 3 Global Variables , without this code will not work.
My_Dir = "E:\\UsersList"
Master_Password_File = My_Dir + str("\\Master_Password_File.csv")
Master_Group_File = My_Dir + str("\\Master_Group_File.csv")

def RmFileIfPresent(FileName):
    """:argument FileName , Type: String
    This function will check and remove file if it exist.
    """
    if os.path.exists(FileName):
        os.remove(FileName)

def ParseUnixGroupFile(FileName):
    """:argument Filename, Type: String
    This function will read the Group File and append it to Master Group File
    """
    with open(FileName, 'r') as MyCsvToRead:
        reader = csv.reader(MyCsvToRead)
        for row in reader:
            if row[0] != "HOSTNAME":
                with open(Master_Group_File, 'a+', newline='') as write_obj:
                    csv_writer = csv.writer(write_obj)
                    csv_writer.writerow(row)

def ParseUnixPasswordFile(FileName):
    """:argument Filename, Type: String
        This function will read the Password File and append it to Master Password File
    """
    with open(FileName, 'r') as MyCsvToRead:
        reader = csv.reader(MyCsvToRead)
        for row in reader:
            print(row)
            if row[0] != "HOSTNAME":
                with open(Master_Password_File, 'a+', newline='') as write_obj:
                    csv_writer = writer(write_obj)
                    csv_writer.writerow(row)


if "name==__main__":
    RmFileIfPresent(Master_Password_File)
    RmFileIfPresent(Master_Group_File)
    os.chdir(My_Dir)
    Files_List = os.listdir(My_Dir)
    for file in Files_List:
        if (file[-9:] == "group.csv"): # check last 9 character of filename
            ParseUnixGroupFile(file)
        if (file[-14:] == "passwdfile.csv"): # check last 14 characters of filename
            ParseUnixPasswordFile(file)