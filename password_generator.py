from nis import match
import random

spec_chars = ['!', '@', '#', '$', '%', '&', '(', ')', '=', '*']
generated_password = ""
length = 0 
can_duplicate = False 
can_spec_chars = False
chars_types_count = 3


# returns random char
def get_char(): 
    rand_char_type = random.randint(1, chars_types_count)
    new_char = ''
    if (rand_char_type == 1):
        new_char = chr(random.randint(97, 122)) # lowercase letters
    elif (rand_char_type == 2):
        new_char = chr(random.randint(65, 90)) # uppercase letters
    elif (rand_char_type == 3):
        new_char = str(random.randint(0, 9)) # numbers
    elif (rand_char_type == 4):
        new_char = str(spec_chars[random.randint(0, len(spec_chars)-1)]) # special char
    
    return new_char


# get password length
while length == 0:
    try:
        length = int(input("\ninsert password length (type '0' for random): "))
        # set random length if the input is 0 (for random)
        if (length == 0):
            length = random.randint(8,12)
            print("\tlength will be " + str(length))
    except:
        print('try again..')


# ask and set if characters can be repeated
ans = ""
while (ans != 'N' and ans != 'n' and ans != 'Y' and ans != 'y'):
    ans = input('\ncan characters be repeated? [Y/N]: ')
can_duplicate = ans == 'Y' or ans == 'y'


# ask to use special chars
ans = ""
while (ans != 'N' and ans != 'n' and ans != 'Y' and ans != 'y'):
    ans = input('\ncan contain spacial characters? [Y/N]: ')
    if (ans == 'Y' or ans == 'y'):
        chars_types_count = 4 # the 4th is the special chars, effects the random char type choose


# gererate the new password
for i in range(length):
    new_char = get_char()
    if (can_duplicate == False):
        while (generated_password.find(new_char) != -1):
            new_char = get_char()
    generated_password += new_char


print("\nYour new password is: " + generated_password + '\n')


