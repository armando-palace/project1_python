from shoes_management import *

def make_shoe(shoe_list):
  """Recibe la lista de zapatos para luego fabricar el modelo seleccionado."""
  quantity = -1
  # Busca el zapato según una lista de zapatos, solicitando el código al usuario.
  shoe = find_shoe(shoe_list, get_shoe_code())

  if shoe != False:
    # Imprime la información del zapato.
    print_shoe_info(shoe)
    while quantity < 0:
      valid = False

      while valid == False:
        quantity = input('Indique la cantidad a fabricar: ')

        # Se valida que el valor ingresado por el usuario es un número.
        try:
          quantity = int(quantity)
          valid = True
        except ValueError:
          print('El valor ingresado no es un número, por favor intente nuevamente.')
          valid = False

      # Se valida que la cantidad no sea negativa.
      if quantity < 0:
        print('Debe ingresar un número mayor o igual que cero (0)')
      # No se fabrica nada.
      elif quantity == 0:
        print('Ha decidido no fabricar ningún zapato.')
      # Se fabrica la cantidad que se indicó
      else:
        fabricate_shoes(shoe_list, shoe, quantity)
        print('Agregadas ' + str(quantity) + ' unidades del modelo ' + shoe['codigo'])
        shoe = find_shoe(shoe_list, shoe['codigo'])
        print('Existencia del modelo ' + shoe['codigo'] + ': ' + str(shoe['cantidad']))
        break
  else:
    print('No existe el modelo seleccionado, por favor intente nuevamente.')
    return False
