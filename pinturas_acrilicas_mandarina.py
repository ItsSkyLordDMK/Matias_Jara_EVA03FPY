from pathlib import Path
import json
import csv
import os

home = Path(__file__).parent

ruta_js = Path(home/'invepint.json')
ruta_cs = Path(home/'mandarina.csv')

def cargar_inventario():
    try:
        with open(ruta_js, 'r') as stream:
            inventario = json.load(stream)
    except FileNotFoundError:
        inventario = []
    return inventario

def guardar_inventario(invepint):
    with open(ruta_js, 'w') as stream:
        json.dump(invepint, stream, indent=4)

def ver_listado_de_pinturas(invepint):
    if not invepint:
        print('El archivo esta vacio.')
    else:
      for prod in invepint:
            print(f'Codigo: {prod['codigo']}. Nombre: {prod['nombre']}. '
                  f'Tipo: {prod['tipo']}. Valor: {prod['valor']}.'
                  f'Stock: {prod['stock']}')
    print()

def buscar_pintura(invepint, cod):
    for prod in invepint:
        os.system('cls')
        if prod['codigo'] == cod:
            print(f'Aqui esta el articulo de codigo: {prod['codigo']}\n')
            print(f'Nombre: {prod['nombre']}. Tipo: {prod['tipo']}. '
                  f'Valor: {prod['valor']}. Stock: {prod['stock']}.')
        else:
            print('El codigo de la pintura que busca es erroneo o no existe')
            
    print()

def agregar_pintura(invepint):
    if not ruta_js.exists():
        ruta_js.touch()
        print('Archivo inventario.json creado exitosamente.')

    if invepint:
        codigo_base = max(repuesto['codigo'] for repuesto in invepint)
    else:
        codigo_base = 380560

    nueva_pint = {
        'codigo': codigo_base + 1,
        'nombre': input('Ingrese el color de la pintura: '),
        'tipo': None,
        'valor': None,
        'stock': None
        }
    while True:
        tipo = input("Ingrese el tipo de pintura (Acrilico, Latex): ").strip().capitalize()
        if tipo in ['Acrilico', 'Latex']:
            nueva_pint['tipo'] = tipo
            break
        else:
            print('Tipo de pintura no valida. Ingrese solamente Acrilico o Latex')

    while True:
        valor = input('Ingrese el valor de la pintura: ')
        if valor.isnumeric():
            nueva_pint['valor'] = int(valor)
            break
        else:
            print('El valor ingresado no es valido. Por favor, ingrese un valor valido.')

    while True:
        try:
            stock = int(input('Ingrese el stock del repuesto: '))
            nueva_pint['stock'] = stock
            break
        except ValueError:
            print("El stock ingresado no es valido. Por favor, ingrese un numero viable para el stock.")

    invepint.append(nueva_pint)
    guardar_inventario(invepint)
    os.system('cls')
    print('Repuesto agregado exitosamente.\n')

def eliminar_pintura(invepint):
    cod = int(input('Ingrese el codigo de la pintura a eliminar: '))
    for prod in invepint:
        if prod['codigo'] == cod:
            invepint.remove(prod)
            guardar_inventario(invepint)
            os.system('cls')
            print('Pintura eliminada exitosamente.\n')
            break
    else:
        print('Pintura no encontrado.')

def exportar_pinturas(invepint):
    with open(ruta_cs, 'w', newline='', encoding='utf-8') as stream:
        write = csv.writer(stream)
        write.writerow(['codigo', 'nombre', 'marca', 'tipo', 'valor', 'stock'])
        for prod in invepint:
            write.writerow([prod['codigo'], prod['nombre'], 
                            prod['tipo'], prod['valor'], prod['stock']])
    print('Inventario exportado a mandarina.csv exitosamente.')
    print()

menup = ['Ver Listado de Pinturas',
         'Buscar Pintura',
         'Agregar Pintura',
         'Eliminar Pintura',
         'Exportar Pinturas']

def principal():
    invepint = cargar_inventario()

    while True:
        for ind, opt in enumerate(menup):
            print(f'{ind+1}. {opt}')
        ans = input('Seleccione una opcion: ')
        os.system('cls')

        if ans == '1':
            ver_listado_de_pinturas(invepint)
        elif ans == '2':
            codp = int(input('Ingrese el codigo de la pintura: '))
            buscar_pintura(invepint, codp)
        elif ans == '3':
            agregar_pintura(invepint)
        elif ans == '4':
            eliminar_pintura(invepint)
        elif ans == '5':
            exportar_pinturas(invepint)
        else:
            print('Error: nesecitas seleccionar una opcion valida')

if __name__ == '__main__':
    principal()