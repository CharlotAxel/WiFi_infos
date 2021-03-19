import subprocess
import re

#Python allows us to run system commands with the "subprocess" module. 
#We specify we want to capture the output.
#This information is stored in bytes and need to be decoded before it can be put in a string.

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode("cp1252")

#Python allows the use of regular expression with the module "re"
#In order to find all the WiFi names in the groups 'All User Profile'
#We create a group of all characters until the return escape sequence (\r) appears.
#And we put it in a list where all usrnames & pwd will be saved.

profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = list()

#If we didn't find profile name, we didn't have any wifi connections,
#So we only run the part to checks the details of the wifi and wether we can get their passwords in this part.

if len(profile_names) != 0:
    for name in profile_names:        
        wifi_profile = dict()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode("cp1252")
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
        
        wifi_list.append(wifi_profile) 

else:
    print("No wifi profil found.")

for x in range(len(wifi_list)):
    print(wifi_profile[x])
