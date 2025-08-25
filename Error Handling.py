
# Error Handling Lab 🧪

filename = input("Enter the filename to read: ")

# Open file in read mode
file = open(filename, "r")
content = file.read()
file.close()

print("📄 File content:")
print(content)
