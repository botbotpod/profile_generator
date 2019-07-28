import os
import random
import csv

'''
This function will create a csv file that will generate a dummy profile that contains
a first name, last name, street address, phone number and email
The default profiles being generated is set to 200
'''
def dummy_export(folder_dir,fname,lname,street,city,profile_size):
    try:
        os.chdir(folder_dir)
        with open(fname,'r') as first_name, open(lname,'r') as last_name, open(street,'r') as street, \
                open(city,'r') as city:

            #read files containing first names and last names
            read_first = first_name.read()
            list_first = read_first.split("\n")
            read_last = last_name.read()
            list_last = read_last.split("\n")


            #Most common email domain address list
            email_list = ['gmail.com','outlook.com','icloud.com','aol.com','yahoo.com','mail.com','hotmail.com','msn.com']

            #List of US Streets
            read_street = street.read()
            list_street = read_street.split('\n')

            #List of US Cities and States
            city_state = city.read()
            list_city_state = city_state.split("\n")

        #Creating CSV File
        with open('usa_profile.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(("First Name", "Last Name", "Address", "City", "State", "Zip Code", "Phone", "Email"))

            #Generating the Profile Data
            for num in range(profile_size):
                first = random.choice(list_first)
                last = random.choice(list_last)
                phone = f'{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000,9999)}'
                email = first.lower() + last.lower() + '@' + random.choice(email_list)

                #Generate Random Street Address
                street_num = random.randint(1,9999)
                street = random.choice(list_street)
                city_state = random.choice(list_city_state)
                zip_code = random.randint(10000,99950)

                address = f'{street_num} {street},{city_state},{zip_code}'

                format_str = f'{first},{last},{address},{phone},{email}'
                split_str = format_str.split(",")

                #Print out the profile for testing, please uncomment if you don't want to see the output
                print(split_str)

                #Export/write all the profile data into a csv file
                writer.writerow(split_str)
    except Exception as e:
        print(e)

#This will run the function and generate a csv file with dummy data
dummy_export('''Please enter your folder directory here''','us_first_names.txt','us_last_names.txt','us_streets.txt','us_cities&states.txt',200)