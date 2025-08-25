# File Read & Write Challenge 🖋️

# Open input file in read mode
infile = open("input.txt", "r")
content = infile.read()
infile.close()

# Modify content (convert to uppercase)
modified_content = content.upper()

# Open output file in write mode
outfile = open("output.txt", "w")
outfile.write(modified_content)
outfile.close()

print("✅ File has been read and modified version saved to 'output.txt'.")
