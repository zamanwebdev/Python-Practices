filename = input("Enter file name (with extension): ")

with open(filename, "w") as file:
    file.write("File created successfully!")

print("✅ File created!")
