#My solution to the Ice9 crackme, by tripletordo (https://crackmes.one/crackme/5ab77f6633c5d40ad448cbe2)

#The program first uses the given username to generate a number, which this function does
def username_to_number_loop (name):
    number_from_username=0x00
    i=0
    #The algorithm ignores the last letter, which is why the loop uses the length-1 
    while i<len(name)-1:
        #For each letter, a given value is added to the number.
        current_letter_value=int(hex(ord(name[i])), 16)
        #0x2C is added if the value of the letter is between 0x5A and 0x41, and adds the value of the letter otherwise
        if current_letter_value <= 0x5A and current_letter_value >= 0x41:
            current_letter_value+=0x2C
        number_from_username+=current_letter_value
        i=i+1
    return number_from_username

#The number is then modified through addition, subtraction, and multiplication by a series of constants.
def modify_username_number (usernamenumber):
    usernamenumber+=0x29A
    usernamenumber*=0x3039
    usernamenumber-=0x17
    usernamenumber*=0x9
    return usernamenumber

#The number is then divided by 0xA, and the remainders (plus a constant) are stored in a list.
def division_and_list_loop (usernamenumber):
    numberlist=[]
    while usernamenumber !=0:
        tempremainder=usernamenumber%0xA
        tempremainder+=0x30
        numberlist.append(tempremainder)
        usernamenumber=int(usernamenumber/0xA)
    return numberlist

#The list is reversed to make the serial number. The characters of the username (excluding the first 3 characters) are then added to the end.
def produce_serial_number (numberlist, name):
    serialstring=""
    for i in reversed(numberlist):
        serialstring+=chr(i)
    j=3
    while j<len(name):
        serialstring+=name[j]
        j+=1
    return serialstring
    
yesorno="yes"
while yesorno == "yes":
    username=input("Enter desired username:")
    username_number=username_to_number_loop(username)
    username_number=modify_username_number(username_number)
    number_list=division_and_list_loop(username_number)
    serial_string=produce_serial_number(number_list, username)
    print("Serial number:")
    print(serial_string)
    yesorno=input ("Generate another serial? Type yes if so.\n")

