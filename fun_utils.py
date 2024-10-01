import os
#defining a function
def check_cpu(command):
    print(os.system(command))

def check_date(command):
    print(os.system(command))

def check_disk(command):     
    print(os.system(command))

def check_uptime(command):
    return os.system(command)

#calling a function
check_cpu("free -h")   #calling a function
check_date("date")
check_disk("df -h")
check_uptime("uptime")