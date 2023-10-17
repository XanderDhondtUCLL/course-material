#!/usr/bin/env py

def main():
    def greet(name):
        return f"Hello, {name}!"
    
    def interactive_greet():
        naam = input("What is your name? ")
        print(greet(naam))

    interactive_greet()
    
if __name__ == '__main__':
    main()