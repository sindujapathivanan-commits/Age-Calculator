#get the currect year and month
current_year = int(input("Enter the current year: "))
current_month = int(input("Enter the current month: "))

#Get the user birthyear and month
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))

#Calculate the Age
age = current_year - birth_year


#Check the user birthday has passed or not
if current_month < birth_month:

    #Birthday has not passed yet, so we add 1 to the age
    age = age - 1 

    #Display the age
print("Your age is: ", age)