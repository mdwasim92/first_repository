import time

def countdown(t):

    while t:
        mins,sces = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,sces)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1

    print("Your Time is Finished: ")
     
t = input("Enter the time in seconds: ")

countdown(int(t))