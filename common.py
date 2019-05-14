from os import system, name
from time import sleep

def clear():
  """Despeja la pantalla del terminal según el sistema operativo."""
  # Para Windows
  if name == 'nt':
    _ = system('cls')

  # Para Mac y Linux (aquí, os.name es 'posix')
  else:
    _ = system('clear')
