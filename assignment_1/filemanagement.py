import os

filename = "sample_file.txt"

print("FILE MANAGEMENT DEMONSTRATION\n")

# 1. CREATE + WRITE FILE
print("1. Creating and writing to file...")
with open(filename, "w") as file:
    file.write("Operating System File Management\n")
    file.write("This file is created using Python.\n")
    file.write("It demonstrates create and write operations.\n")
print("File created and data written successfully.\n")

# 2. READ FILE
print("2. Reading file content:")
with open(filename, "r") as file:
    content = file.read()
    print(content)

# 3. APPEND DATA
print("3. Appending new data to file...")
with open(filename, "a") as file:
    file.write("This line is appended later.\n")
print("Data appended successfully.\n")

# 4. READ AGAIN
print("4. Reading updated file content:")
with open(filename, "r") as file:
    print(file.read())

# 5. DELETE FILE
print("5. Deleting the file...")
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted successfully.")
else:
    print("File does not exist.")
