from shutil import get_terminal_size

def show_table(shoe_list):
  """Muestra en pantalla una tabla con los datos de todos los zapatos."""
  # Se obtienen las columnas y filas que tiene el terminal donde se está ejecutando la aplicación.
  columns, rows = get_terminal_size(fallback = (50, 50))

  # Imprime el borde superior de la tabla.
  print('-' * columns)

  # Imprime la primera fila que son los títulos de cada columna.
  print(
    '|' + 'Código'.center(columns // 6 - 1) +
    '|' + 'Descripción'.center(columns // 6 * 2 - 1) +
    '|' + 'Talla'.center(columns // 6 - 1) +
    '|' + 'Precio'.center(columns // 6 - 1) +
    '|' + 'Cantidad'.center(columns // 6 - 1) + '|'
  )

  # Imprime el borde inferior de la primera fila.
  print('-' * columns)

  # Imprime los datos de cada zapato en sus respectivas columnas.
  # Cada zapato se imprime en una nueva fila.
  for i in range(0, len(shoe_list)):
    print(
      '|' + shoe_list[i]['codigo'].center(columns // 6 - 1) +
      '|' + shoe_list[i]['modelo'].center(columns // 6 * 2 - 1) +
      '|' + str(shoe_list[i]['talla']).center(columns // 6 - 1) +
      '|' + str(shoe_list[i]['precio']).center(columns // 6 - 1) +
      '|' + str(shoe_list[i]['cantidad']).center(columns // 6 - 1) + '|'
    )

  # Imprime el borde inferior de la tabla.
  print('-' * columns)