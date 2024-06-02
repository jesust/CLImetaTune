import music_tag
import argparse

def modificar_etiquetas(archivo, datos):
    # Cargar el archivo de audio
    audio = music_tag.load_file(archivo)
    
    # Verificar si hay cambios que realizar
    cambios = False
    if 'title' in datos and datos['title'] is not None:
        audio['title'] = datos['title']
        cambios = True
    if 'album' in datos and datos['album'] is not None:
        audio['album'] = datos['album']
        cambios = True
    if 'genre' in datos and datos['genre'] is not None:
        audio['genre'] = datos['genre']
        cambios = True
    if 'year' in datos and datos['year'] is not None:
        audio['year'] = datos['year']
        cambios = True
    
    # Guardar los cambios solo si se hicieron modificaciones
    if cambios:
        audio.save()
        print("Cambios guardados exitosamente.")
    else:
        print("No se realizaron cambios, no se proporcionaron etiquetas para modificar.")

def mostrar_etiquetas(archivo):
    # Cargar el archivo de audio
    audio = music_tag.load_file(archivo)
    
    # Obtener las etiquetas
    etiquetas = {
        'title': audio['title'],
        'album': audio['album'],
        'genre': audio['genre'],
        'year': audio['year']
    }
    
    # Mostrar las etiquetas que tienen valores
    print("Etiquetas actuales del archivo:")
    for key, value in etiquetas.items():
        if value:
            print(f"{key}: {value}")
        else:
            print(f"{key}: No disponible")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modificar etiquetas de archivos de audio.")
    parser.add_argument("archivo", help="Ruta del archivo de audio.")
    parser.add_argument("--title", help="Nuevo título de la canción.")
    parser.add_argument("--album", help="Nuevo álbum de la canción.")
    parser.add_argument("--genre", help="Nuevo género de la canción.")
    parser.add_argument("--year", help="Nuevo año de la canción.")

    args = parser.parse_args()
    datos = {
        'title': args.title,
        'album': args.album,
        'genre': args.genre,
        'year': args.year
    }

    # Verificar si no se proporcionaron etiquetas para modificar
    if all(value is None for value in datos.values()):
        mostrar_etiquetas(args.archivo)
    else:
        modificar_etiquetas(args.archivo, datos)
