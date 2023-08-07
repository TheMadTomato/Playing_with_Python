import zipfile

# Create object of zip to crack
zip_file = zipfile.ZipFile("ZipMe.zip") #fill the name of the file to be cracked here

# Open wordlist
with open("rockyou.txt","rb") as file:
    # Read each line
    for line in file:
        line = line.strip()
        # Try to extract the zip file with the password
        try:
            zip_file.extractall(pwd=line)

            # If passwd is valid, print it
            print("Password found: ",line)
            break
        except:
            continue