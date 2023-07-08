# Allow entry if student height if more than or equal to 30
# Deny entry f student height is less than 30

a=int(input("Enter the height of the student in cm: "))
if a>=30:
    print(f"Height is {a} more than 30. You are allowed.")
else:
    print(f"Height is {a} less than 30. You are not allowed.")

