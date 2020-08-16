#this is suppose to be a contact list using a while function
print("would you like to enter a new contact?")
ans = input("Yes or No?")

#the following subfunction is designed for data entry
contact_data = []
while ans == "Yes" or "yes":
	print("Please enter their information.")
	nam = input("please input their name:")
	phone = input("please input their phone number:")
	email = input("please input their email address:")
	if len(phone) != 10:
	        phone = input("the phone number you provided is not the proper length. Re-enter:")
	contact = []+[nam]+[phone]+[email]
	contact_data.append(contact)
	ans = input("would you like to continue adding:")
	if ans == "no":
		break
	if ans == "yes" or "Yes":
	        print("Alright")
	        continue 

print(contact_data)