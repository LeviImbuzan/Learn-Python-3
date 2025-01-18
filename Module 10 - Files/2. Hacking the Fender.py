import csv
import json

compromised_users=[]

# Read usernames from 'passwords.csv'
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    password_row = []
    for password in password_csv:
        compromised_users.append(password['Username'])
    #print(compromised_users) # Uncomment this line if you want to print the compromised usernames

# Write compromised usernames to 'compromised_users.txt'
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + '\n') # Add usernames with line breaks

# Read and print compromised usernames from 'compromised_users.txt'
with open('compromised_users.txt') as compromised_user_file:
    print(compromised_user_file.read())

# Create and write boss message JSON to 'boss_message.json'
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
    json.dump(boss_message_dict, boss_message)

# Read and print boss message JSON from 'boss_message.json'
with open('boss_message.json') as boss_message:
    print(boss_message.read())

# Write ASCII art to 'new_passwords.csv' (This does not follow CSV format)
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
 """
    new_passwords_obj.write(slash_null_sig)

# Read and print the ASCII art from 'new_passwords.csv'
with open('new_passwords.csv') as new_passwords_obj:
    print(new_passwords_obj.read())
