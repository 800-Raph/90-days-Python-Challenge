# A PROGRAM TO CALCULATE THE AGE OF A USER FROM DATETIME IMPORT DATETIME
name=input("What is your name")
age=int(input("What is your age"))
current_year=int(input("Enter the current year"))
year_of_birth=current_year - age
print(f"Hello, {name}.You were born in {year_of_birth} ")
