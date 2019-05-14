from shoes_management import *

def make_shoe(shoe_list):
  quantity = -1
  shoe = find_shoe(shoe_list, get_shoe_code())
  if shoe == False:
    return False
  print_shoe_info(shoe)

  if shoe != False:
    while quantity < 0:
      valid = False

      while valid == False:
        quantity = input('Indique la cantidad a fabricar: ')

        try:
          quantity = int(quantity)
          valid = True
        except ValueError:
          print('El valor ingresado no es un número, por favor intente nuevamente.')
          valid = False

      if quantity < 0:
        print('Debe ingresar un número mayor o igual que cero (0)')
      elif quantity == 0:
        print('Ha decidido no fabricar ningún zapato.')
      else:
        fabricate_shoes(shoe_list, shoe, quantity)
        print('Agregadas ' + str(quantity) + ' unidades del modelo ' + shoe['codigo'])
        shoe = find_shoe(shoe_list, shoe['codigo'])
        print('Existencia del modelo ' + shoe['codigo'] + ': ' + str(shoe['cantidad']))
        break
  else:
    print('No existe el modelo seleccionado, por favor intente nuevamente.')
