from shoes_management import *

def show_shoe(shoe_list):
  print_shoe_info(find_shoe(shoe_list, get_shoe_code()))

def verify_existence_of_shoe(shoe_list, shoe):
  try:
    shoe_index = shoe_list.index(shoe)
    return True
  except ValueError:
    print('El modelo no existe en la lista.')
    return False