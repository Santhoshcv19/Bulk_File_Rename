import os

def rename_files(directory, ending, newname):
    files = os.listdir(directory)
    counter = 0
    for file in files:
        if file.endswith(ending):
            filetype = file.split('.')[-1]
            os.rename(directory + '/' + file, directory + '/' + newname + str(counter) + '.' + filetype)
            print("Renaming " + file + " to " + newname + str(counter) + "." + filetype)
            counter += 1
