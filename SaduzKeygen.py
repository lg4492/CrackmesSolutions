#My solution for saduz's visual c++ crackme (https://crackmes.one/crackme/5c1d6f5f33c5d41e58e005f5)

#the same loop is used for the computer username and the program username
def name_loop(name):
    number_from_username=0x00
    i=0
    #for each character, add its hex value + 0x186A0 to the generated number.
    while i<len(name):
        number_from_username+=int(hex(ord(name[i])),16)+0x186A0
        i+=1
    return number_from_username
yesorno="yes"
#the windows username
computer_username=input("Enter the username you use to log in to your computer \n")
while yesorno == "yes":
    #ask the user for the username they want to use for the program
    program_username=input("Enter the name you would like to use as the name for the crackme \n")
    print("Here is the key:")
    #add the number from both usernames and add 0x7A69. The output is the serial
    print(int(hex(name_loop(computer_username)+name_loop(program_username)), 16) + 0x7A69)
    yesorno=input ("Generate another key? Type yes if so.")

