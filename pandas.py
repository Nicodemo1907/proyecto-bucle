from readchar import readkey, key

while True:
   k = readkey()
   print(f'Has presionado: {k}')
   if k == key.UP:
       print('Has presionado la tecla ↑. Saliendo del programa...')
       break