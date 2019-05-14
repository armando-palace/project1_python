from shoes_management import *

def send_shoe(shoe_list):
  """Recibe la lista de zapatos para luego despachar el modelo seleccionado."""
  # Busca el zapato según una lista de zapatos, solicitando el código al usuario.
  shoe = find_shoe(shoe_list, get_shoe_code())

  if shoe != False and shoe['cantidad'] > 0:
    # Imprime la información del zapato.
    print_shoe_info(shoe)
    quantity = -1

    while quantity > shoe['cantidad'] or quantity < 0:
      valid = False

      while valid == False:
        quantity = input('Indique la cantidad de zapatos a despachar: ')

        # Se valida que el valor ingresado por el usuario es un número.
        try:
          quantity = int(quantity)
          valid = True
        except ValueError:
          print('El valor ingresado no es un número, por favor intente nuevamente.')
          valid = False
      # No se puede enviar una cantidad mayor que la existencia del producto.
      if quantity > shoe['cantidad']:
        print('Ha escogido una cantidad mayor a la existencia de este modelo. Intente nuevamente.')
        print('Cantidad existente de este modelo: ' + str(shoe['cantidad']))
      # No se envía ningún zapato.
      elif quantity == 0:
        print('Ha decidido no despachar ningún zapato.')
      # Se valida que la cantidad no sea negativa.
      elif quantity < 0:
        print('No puede despachar una cantidad negativa de zapatos. Intente nuevamente.')
        print('Cantidad existente de este modelo: ' + str(shoe['cantidad']))
      # Se despacha la cantidad que se indicó.
      else:
        dispatch_shoes(shoe_list, shoe, quantity)
        print('Despachadas ' + str(quantity) + ' unidades del modelo ' + shoe['codigo'])
        shoe = find_shoe(shoe_list, shoe['codigo'])
        print('Existencia del modelo ' + shoe['codigo'] + ': ' + str(shoe['cantidad']))
        break
  else:
    if shoe != False:
      print('No quedan más zapatos de este modelo, por favor fabrique más.')
