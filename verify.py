from shoes_management import *

def show_shoe(shoe_list):
  """Busca en la lista de zapatos, un zapato según el código proporcionado por el usuario e imprime todos sus datos."""
  print_shoe_info(find_shoe(shoe_list, get_shoe_code()))

def verify_existence_of_shoe(shoe_list, shoe):
  """Verifica la existencia de un zapato en la lista dada. Retorna True si existe, o False de lo contrario."""
  try:
    shoe_index = shoe_list.index(shoe)
    return True
  except ValueError:
    print('El modelo no existe en la lista.')
    return False
