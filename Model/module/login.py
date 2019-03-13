from time import sleep

def login(name):

    for c in name:
        print(c, end='', flush=True)
        sleep(0.1)

    result= input()
    return result


