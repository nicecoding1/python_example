import random

def password_make(length):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@$%^&*()."
    b = list(a)
    pw = ""
    
    random.shuffle(b)

    try:
        for i in range(length):
            pw += str(b.pop())
    
    except Exception as e:
        print(e)
    
    return pw


if __name__ == "__main__":
    pw = password_make(10)
    print(pw)
