import os
from colors import red, yellow, green, info, bad, end

def main():

    os.system('cls')
    print('%s--------------------------- PEER-TO-PEER CONNECTIVITY ---------------------------'%green)

    print('[1] CONNECT TO SERVER')
    print('[2] INITIATE SERVER')
    print('[3] TO QUIT')

    option = int(input("Select your Mode: "))


    if option == 1 :
        ip = input("Enter IP Address of Peer to Connect: ")
        print("Port No. is set to Default: 12345")
        cred = 'nc '+ip+' 12345'
        os.system('cls')
        print("Connection Successful: Just Enter Message and Press <- Enter.")
        os.system(cred)

    elif option == 2:
        os.system('cls')
        print("Port No. is set to Default: 12345")
        cred = 'nc -nvlp'+'12345'
        os.system(cred)

    elif option == 3:
        os.system('exit')

    else:
        os.system('cls')
        print("%sInvalid Selection :("%red)
        main()

main()