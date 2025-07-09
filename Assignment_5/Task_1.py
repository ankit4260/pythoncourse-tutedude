studic={'Ankit':77 ,'Rakesh' : 84 , 'Alice' : 34}
name=input("Enter user's name :")
if name in studic:
    print(f"{name}'s marks is {studic[name]}")
else:
    print("Student not found .")