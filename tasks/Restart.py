import os
import sys

def restart():
  if os.name == "nt":
    os.system("cls")
  os.execv(sys.executable, ["python"] + sys.argv)