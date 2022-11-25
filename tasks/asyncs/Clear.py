import os

async def cls():
  if os.name == "nt":
    os.system("cls")