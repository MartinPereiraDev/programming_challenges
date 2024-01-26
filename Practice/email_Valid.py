# use te regex for format email
# alt 94 ^,  alt 92 \
import re 

def IsValidEmail(email):
        regex = "^[A-Z0-9.%+-]+@[A-Z0-9]+\.[A-Z]{2,}$"
        if len(email) > 7:
                if re.match(regex, email, re.IGNORECASE) is not None:
                        return True
                
if IsValidEmail("martin900@hotmail.com"):
        print("This email is Valid")
else: 
        print("this email NOT is Valid")               
                
