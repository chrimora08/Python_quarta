import funzioni1
import random

def main():
    voti = [random.randint(2, 10) for i in range(10)]
    print(voti)
    m, n = funzioni1.media(voti)
    print(m)

if __name__ == "__main__":
    main()