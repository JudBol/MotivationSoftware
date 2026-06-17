from toyControl import *

def main():
    print("Application Started")
    print("""
========================================================
Welcome to the Motivation Software graphical interface!

    This is the interface for "motivation" in your 
    coding activities!
    
========================================================
""")

    input("Press enter to continue...")


    asyncio.run(customFunction())

if __name__ == "__main__":
    main()