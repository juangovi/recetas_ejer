from os import system
from importlib.resources import path
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

def menu_dinamico(listadinamica):
  for recetas in range(len(listadinamica)):
    print(f'[{ recetas + 1}] - {listadinamica[recetas].name}')
  print(f'[{len(listadinamica)+1}] - volver')
  return(input("elige una opcion: "))

def leer(Lista_recetas,receta):
  Lista_recetas[int(receta)-1].read_text()


def leer_recetas_menu():
  categoria=0
  while int(categoria)not in range(1,len(lista)+1):
    categoria = menu_dinamico(lista)
  system("clear")
  return [x for x in lista[int(categoria)-1].iterdir() if not x.is_dir()]
  
#* codigo--

print("saludos invocador")
saludo()
opcion = 0
while opcion != "7":
  opcion=menu()
  if opcion == "1":
    lista_recetas=leer_recetas_menu()
    leer(lista_recetas,menu_dinamico(lista_recetas))
  elif opcion == "7":
    pass
  else:
    system("clear")
    print(":/")
else:
  print("adios :D")





