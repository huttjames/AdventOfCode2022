from classes import *

root = Folder("root", ["root"], {}, 0)
cwd = root
file_sizes = {} # This is a flat list of folder sizes which is updated every time a new file is added. It stores each path as a key. 

# This function checks whether the line is an instruction (False) or file/folder (True)
def isfile(string):
    x = True
    if string[0] == "$":
        x = False
    return x

# Having worked out if its a file/folder we split folders & end files
def isfolder(string):
    if string[0:4] == "dir ":
        return True
    else:
       return False

# This function is called every time a file is created. It adds the file size to every folder above the file location in the tree. 
def add_size_to_folders(path, size, cwd):

    # At a minimum the path has 2 values. ["root", "string"] is a file in the root directory. This is treated as a unique case. 
    if path[-1] == "root":
        cwd.update_size(size)
        file_sizes.update({str(cwd.path): cwd.size})
    # Otherwise, the file is in a sub folder. The method is: Move to root and add the file size to the running total. Then step through 
    # Each folder in the file path updating the file size using the method inbuilt in the class. 
    else: 
        cwd = root
        cwd.update_size(size)
        # This line logs the new folder size to the dictionary. Path compressed to string. 
        file_sizes.update({str(cwd.path): cwd.size})

        # Having dealt with the root folder we then change the cwd in turn to each subfolder using the function change_to_directory
        for folder in path[1:]:
            cwd = change_to_directory(folder, cwd)
            cwd.update_size(size)
            file_sizes.update({str(cwd.path): cwd.size})

# This function simply creates a new folder in the specified working directory. It logs the path to the folder for later use. 
def createFolder(string, path, cwd):
    name = string[4:]
    new_path = path + [name]
    contents = {}

    if name in cwd.contents.keys():
        print("Folder already exists")
    else:
        newFolder = Folder(name, new_path, contents, 0)
        # Append the key value pair to the correct dictionary 
        cwd.contents.update({name : newFolder})
        
# This function creates a file. Steps are 1: pull the file information from the line, 2: check that the file hasn't been listed already
# 3: Add the file to the contents dictionary in the folder, 4:Update the folder sizes for all folders in the tree
def createFile(string, path, cwd):
    info = string.split()
    size = int(info[0])
    name = info[1]
    
    if name in cwd.contents.keys():
        print(cwd.name)
        print("File already exists")
    else:
        newFile = File(name, path, size)
        # Append the key value pair to the correct dictionary 
        cwd.contents.update({name : newFile})
        add_size_to_folders(cwd.path, size, cwd)

# This function moves down 1 level from the cwd to a folder with the specified name. 
def change_to_directory(new_dir, cwd):
      cwd = cwd.contents[new_dir]
      return cwd

def read_file(line, cwd):
    if isfile(line):
        if isfolder(line):
            # Check if the folder exists and otherwise create it
            createFolder(line, cwd.path, cwd) 
        else: 
            # Check if the file exists and otherwise create it
            createFile(line, path, cwd)
    else: 
        # check if instruction to cwd 
        if line[0:4] == "$ cd":
            # if it is then cwd. There are 2 spaces in the instruction so the new_dir is the 3rd element of the split string. 
            info = line.split()
            new_dir = info[2]

            # Moving up a level
            if new_dir == "..":
                if cwd.path[-2] == 'root':
                    cwd = root
                else:
                    # If we aren't moving to root then we are moving depth-2 hops from root, since depth-1 hops would get us to the current folder
                    depth = len(cwd.path)
                    starting_folder = cwd.path
                    cwd = root
                    for i in range(depth-2):
                        cwd = change_to_directory(starting_folder[i+1], cwd)

            # This code moves to root when explicitly told to 
            elif new_dir == "/":
                cwd = root

            # This code moves down a level when told to 
            elif isinstance(new_dir, str):
                cwd = change_to_directory(new_dir, cwd)
            # This catches if the line doesn't end with a string
            else: 
                print("james has messed up the logic")
    return cwd
    



# Opens the instructions and reads them line by line. Read_file carries out the appropriate actions. 
with open("input.txt") as file:
    path = ['root']
    for line in file: 
        line = line.strip()
        cwd = read_file(line, cwd)


# Answering part 1

#Find just the folders with sizes less than 100,000
small_files = [i for i in file_sizes.values() if i <= 100000]
print(sum(small_files))

#Part 2 

x = max(file_sizes.values())
space_already_free = 70000000-x
new_space_needed = 30000000 - space_already_free

big_enough = [i for i in file_sizes.values() if i > new_space_needed]
print(min(big_enough))
