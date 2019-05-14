from shoes_management import *

def send_shoe(shoe_list):
  """Recibe la lista de zapatos para luego despachar el modelo seleccionado."""
  shoe = find_shoe(shoe_list, get_shoe_code())

  if shoe != False and shoe['cantidad'] > 0:
    quantity = -1

    while quantity > shoe['cantidad'] or quantity < 0:
      valid = False

      while valid == False:
        quantity = input('Indique la cantidad de zapatos a despachar: ')

        try:
          quantity = int(quantity)
          valid = True
        except ValueError:
          print('El valor ingresado no es un número, por favor intente nuevamente.')
          valid = False

      if quantity > shoe['cantidad']:
        print('Ha escogido una cantidad mayor a la existencia de este modelo. Intente nuevamente.')
        print('Cantidad existente de este modelo: ' + str(shoe['cantidad']))
      elif quantity == 0:
        print('Ha decidido no despachar ningún zapato.')
      elif quantity < 0:
        print('No puede despachar una cantidad negativa de zapatos. Intente nuevamente.')
        print('Cantidad existente de este modelo: ' + str(shoe['cantidad']))
      else:
        dispatch_shoes(shoe_list, shoe, quantity)
        print('Despachados ' + str(quantity) + ' unidades del modelo ' + shoe['codigo'])
        shoe = find_shoe(shoe_list, shoe['codigo'])
        print('Existencia del modelo ' + shoe['codigo'] + ': ' + str(shoe['cantidad']))
        break
  else:
    if shoe != False:
      print('No quedan más zapatos de este modelo, por favor fabrique más.')
