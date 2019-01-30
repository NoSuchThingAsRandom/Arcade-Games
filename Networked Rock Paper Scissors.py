import threading
import socket
import time

def start_host():
    sock=socket.socket()
    host=socket.gethostname()
    print("Host is: "+str(host))
    port=5000
    sock.bind((host,port))
    sock.listen(1)
    conn,addr=sock.accept()
    print("Client connected from: "+str(addr))
    if input("Do you wish to connect? (yes)").lower()!="yes":
        conn.send("Declined".encode("utf-8"))
        conn.close()
        start_host()
    else:
        conn.send("Accepted".encode("utf-8"))
    loop=True
    while loop:
        print("\n"*3)
        if conn.recv(1024).decode("utf-8")!="play":
            conn.close()
            print("They do not wish to play again")
            start()
        host_choice=get_choice()
        client_choice=conn.recv(1024).decode("utf-8")
        result=decide(host_choice,client_choice)
        conn.send(host_choice.encode("utf-8"))
        conn.send(result[1].encode("utf-8"))
        print("You chose: "+host_choice)
        print("They chose: "+client_choice)
        print("Therefore you have "+result[0])
        if input("Do you wish to play again? ").lower()!="yes":
            loop=False
            conn.send("exit".encode("utf-8"))
        else:
            conn.send("play".encode("utf-8"))
    conn.close()

def start_client():
    host=input("Enter the address given by the other player: ")
    sock=socket.socket()
    port=5000
    sock.connect((host,port))
    if sock.recv(1024).decode("utf-8")=="Declined":
        print("You have been declined!")
        start_client()
    loop=True
    while loop:
        print("\n"*3)
        sock.send("play".encode("utf-8"))
        player_choice=get_choice()
        sock.send(player_choice.encode("utf-8"))
        host_choice=sock.recv(1024).decode("utf-8")
        result=sock.recv(1024).decode("utf-8")

        print("You chose: "+player_choice)
        print("They chose: "+host_choice)
        print("Therefore you have "+result)
        if sock.recv(1024).decode("utf-8")=="exit":
            loop=False
            sock.close()
            print("They do not wish to play again")
            start()
        if input("Do you wish to play again? ").lower()!="yes":
            loop=False
            sock.send("exit".encode("utf-8"))
            sock.close()

def get_choice():
    print("Your choices are rock,paper or scissors")
    choice=input("Enter your choice: ").lower()
    if choice=="rock" or choice=="paper" or choice=="scissors":
        return choice
    return get_choice()

def decide(one,two):
    if one==two:
        return ("Drawn","Drawn")
    if one=="rock"and two=="scissors":
        return ("Won","Lost")
    elif one=="paper"and two=="rock":
        return ("Won","Lost")
    elif one =="scissors" and two=="paper":
        return ("Won","Lost")
    return ("Lost","Won")


def start():
    choice=input("Do you wish to host, join or exit?").lower()
    if choice=="host":
        start_host()
    elif choice="join:
        start_client()
    else:
        exit(0)

start()