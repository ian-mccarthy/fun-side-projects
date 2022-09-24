import curses.ascii
from curses.ascii import isdigit, isupper
import datetime
from datetime import datetime
import secrets
import string



user_defined_length = int(input("Input a length for your new password! \n"))

alphanumeric_list = string.ascii_letters + string.digits

while True:
    new_password = ''.join(secrets.choice(alphanumeric_list)for i in range(user_defined_length))
    if (any(char.islower() for char in new_password)
        and any (char.isupper()for char in new_password)
        and any (char.isdigit()for char in new_password)):
            break

date_and_time = datetime.now()
dt_list = [date_and_time.day,'/',date_and_time.month,'/',date_and_time.year, ' ', date_and_time.hour,':',date_and_time.minute,':',date_and_time.second]

dt_ = ''.join(str(v) for v in dt_list)

print("Your new password is: \n", new_password, "\n Generated at: \n", dt_)
