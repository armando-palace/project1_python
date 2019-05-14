from shutil import get_terminal_size
import delivery
import manufacture
import verify

def display_menu():
  columns, rows = get_terminal_size(fallback = (50, 50))

  print('¡Bienvenido a la Zapatienda!\n'.center(columns))

  print('Menú\n'.center(columns))

  print('1. Entregar')
  print('2. Fabricar')
  print('3. Verificar existencia de un modelo (ingresando el código)')
  print('4. Ver existencia total')
  print('5. Salir\n')

def get_option():
  print('Por favor, escoja una opción del menú: \n')
  return input('Opción: ')

def execute_option(shoe_list, option):
  if option == '1':
    delivery.send_shoe(shoe_list)
  elif option == '2':
    manufacture.make_shoe(shoe_list)
  elif option == '3':
    verify.show_shoe(shoe_list)
  elif option == '4':
    print('Implementación de la opción 4')
  elif option == '5':
    print('¡Gracias por usar nuestra aplicación!')
    return option
  else:
    print('- Opción no válida, intente de nuevo -')
