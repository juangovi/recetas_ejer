from importlib.resources import path
import os
from pathlib import *

base = Path.cwd()
ruta_padre = Path(base,"Recetas")
lista = [x for x in ruta_padre.iterdir() if x.is_dir()]

#* funciones

def saludo():
  for item in lista:
    print(f"en {item.name} hay {len([x for x in item.iterdir() if not x.is_dir()])} recetas")

def menu():
  print("[1] - leer receta")
  print("[3] - crear receta")
  print("[4] - crear categoria")
  print("[5] - eliminar receta")
  print("[6] - eliminar categoria")
  print("[7] - fin")
  return(input("elige una opcion: "))

def menu_categorias():
  for cat in range(len(lista)):
    print(f'[{cat + 1}] - {lista[cat].name}')
  return(input("elige una categoria: "))

def leer_recetas():
  categoria = menu_categorias()
#* codigo--

print("saludos invocador")
saludo()
opcion = 0
while opcion != 6:
  opcion=menu()
  if opcion == 1:
    pass





