from common import *
from shoes_management import get_predefined_shoe_list
import menu

option = '0'

# sleep(1)
clear()
# shoe_list = get_shoe_list()
shoe_list = get_predefined_shoe_list()

while option != '5':
  menu.display_menu()
  option = menu.execute_option(shoe_list, menu.get_option())
