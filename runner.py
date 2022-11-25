from devbot import devbot
from playbot import playbot
from mathbot import mathbot

def main():
  option = input("Which bot would you like to run? (devbot, playbot, mathbot): ")
  options = ["devbot", "playbot", "mathbot"]
  if option not in options:
    print("Invalid option.")
    main()
  else:
    if option.lower() == "devbot":
      devbot()
    elif option.lower() == "playbot":
      playbot()
    elif option.lower() == "mathbot":
      mathbot()

if __name__ == "__main__":
  main()