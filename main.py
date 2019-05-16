from common import *
from shoes_management import get_predefined_shoe_list
import menu

option = '0'

# sleep(1)
# Limpia la pantalla
clear()
# Obtiene la lista predeterminada de zapatos.
# shoe_list = get_shoe_list()
shoe_list = get_predefined_shoe_list()

# print(get_predefined_shoe_list.__doc__)
# help(get_predefined_shoe_list)

# Mientras que la opción no sea "5", no se sale de la aplicación.
while option != '5':
  menu.display_menu()
  option = menu.execute_option(shoe_list, menu.get_option())
