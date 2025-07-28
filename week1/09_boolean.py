def main(number=0):
    if is_even(number):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main(10)