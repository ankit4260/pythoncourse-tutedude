text=input("Enter text to write in file : ")
with open("output.txt","w") as f:
    f.write(text)
print("Data successfully written to output.txt")
adtext=input(" Enter additional data to append in output.txt :")

with open("output.txt","a") as f:
    f.write("\n"+adtext)
print("Data successfully appended to output.txt")
with open("output.txt") as f:
    print(f.read())