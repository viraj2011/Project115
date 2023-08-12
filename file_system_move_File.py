import os

# Specify the directory and file name

source = "main.txt"
dest = "newfile.txt"

# Create the source file path by joining the directory and file name
source_file_path = os.path.join(dest , source)

# Print the source file path
print("Source File Path:", source_file_path)
os.rename(source, dest)


