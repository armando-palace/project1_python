from random import randint

def get_shoe_types():
  shoe_types  = ['Botas', 'Botines', 'Tacones Bajos', 'Tacones Altos', 'Deportivos', 'Sandalias', 'Casuales', 'Mocasines', 'Zapatillas', 'Elegantes']
  shoe_colors = ['Blanco', 'Negro', 'Azul', 'Rojo', 'Amarillo', 'Verde', 'Marrón', 'Morado', 'Rosado', 'Anaranjado', 'Gris', 'Dorado', 'Plateado']
  shoe_sizes  = [23, 47]

  return shoe_types, shoe_colors, shoe_sizes

def get_shoe_list():
  shoe_types, shoe_colors, shoe_sizes = get_shoe_types()
  shoe_list = []

  for i in range(1, 10):
    shoe_size = randint(shoe_sizes[0], shoe_sizes[1])

    shoe_list.append({
      'codigo': 'zapTAM' + str(shoe_size),
      'modelo': shoe_types[randint(0, len(shoe_types) - 1)] + ' ' + shoe_colors[randint(0, len(shoe_colors) - 1)],
      'talla': shoe_size,
      'precio': randint(50000, 500000),
      'cantidad': randint(1, 100)
    })

  return shoe_list

def get_predefined_shoe_list():
  codes = [
    'zapTAN37', 'zapTAN38', 'zapTAN39',
    'zapTAM37', 'zapTAM38', 'zapTAM39',
    'zapTMN37', 'zapTMN38', 'zapTMN39',
    'zapTMM37', 'zapTMM38', 'zapTMM39'
  ]

  models = [
    'Tacón alto negro', 'Tacón alto negro', 'Tacón alto negro',
    'Tacón alto marrón', 'Tacón alto marrón', 'Tacón alto marrón',
    'Tacón medio negro', 'Tacón medio negro', 'Tacón medio negro',
    'Tacón medio marrón', 'Tacón medio marrón', 'Tacón medio marrón'
  ]

  sizes = [
    37, 38, 39,
    37, 38, 39,
    37, 38, 39,
    37, 38, 39
  ]

  prices = [
    95000, 95000, 95000,
    92500, 92500, 92500,
    85000, 85000, 85000,
    83500, 83500, 83500
  ]

  quantities = [
    10, 10, 10,
    7, 7, 7,
    12, 12, 12,
    8, 8, 8
  ]

  shoe_list = []

  for i in range(0, 12):
    shoe_list.append({
      'codigo': codes[i],
      'modelo': models[i],
      'talla': sizes[i],
      'precio': prices[i],
      'cantidad': quantities[i]
    })

  return shoe_list

def get_shoe_code():
  return input('Ingrese el código del zapato: ')

def find_shoe(shoe_list, code):
  for i in range(0, len(shoe_list)):
    if code == shoe_list[i]['codigo']:
      # print('El modelo seleccionado es:')
      # print('Modelo: ' + shoe_list[i]['modelo'])
      # print('Talla: ' + str(shoe_list[i]['talla']))
      # print('Precio: ' + str(shoe_list[i]['precio']))
      # print('Cantidad: ' + str(shoe_list[i]['cantidad']))

      return shoe_list[i]

  print('No se encontró el modelo especificado, intente nuevamente.')
  return False

def dispatch_shoes(shoe_list, shoe, quantity):
  shoe_index = shoe_list.index(shoe)
  shoe['cantidad'] -= quantity
  shoe_list[shoe_index] = shoe

def fabricate_shoes(shoe_list, shoe, quantity):
  shoe_index = shoe_list.index(shoe)
  shoe['cantidad'] += quantity
  shoe_list[shoe_index] = shoe

def print_shoe_info(shoe):
  # shoe = find_shoe(shoe_list, code)
  print('El modelo seleccionado es:')
  print('Modelo: ' + shoe['modelo'])
  print('Talla: ' + str(shoe['talla']))
  print('Precio: ' + str(shoe['precio']))
  print('Cantidad: ' + str(shoe['cantidad']))
