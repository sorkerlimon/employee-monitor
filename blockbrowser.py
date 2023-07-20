# import subprocess

# batch_script = r'''
# @echo off
# set "ChromeDir=%LOCALAPPDATA%\Google\Chrome\User Data\Default"
# echo ^{^"password_manager_enabled^": false^}>"%ChromeDir%\Preferences"
# '''

# # Run the batch script
# subprocess.call(batch_script, shell=True)

# import json

# file_path = r"C:\Users\21100002\AppData\Local\Google\Chrome\User Data\Default\Preferences"

# with open(file_path, 'r', encoding='utf-8') as file:
#     data = json.load(file)

# autosignin = data['credentials_enable_autosignin']
# service = data['credentials_enable_service']

# print("credentials_enable_autosignin:", autosignin)
# print("credentials_enable_service:", service)



import json

file_path = r"C:\Users\21100002\AppData\Local\Google\Chrome\User Data\Default\Preferences"

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

    
autosignin = data['credentials_enable_autosignin']
service = data['credentials_enable_service']

print("credentials_enable_autosignin:", autosignin)
print("credentials_enable_service:", service)


# data['credentials_enable_autosignin'] = "false"
# data['credentials_enable_service'] = "false"

# with open(file_path, 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4)
