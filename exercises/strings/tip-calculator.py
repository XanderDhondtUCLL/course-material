#!/usr/bin/env py

def main():
    def tip_calculator():
        price = int(input("Enter total price: "))
        percent = input("Enter tip percentage (default=20): ")
        if len(percent) == 0:
            percent = 20
        else:
            percent = int(percent)
        total = round(price * (1 + percent / 100))
        print(f'You have to pay {total}')
    tip_calculator()

if __name__ == '__main__':
    main()