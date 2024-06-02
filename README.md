
# CLImetaTune

CLImetaTune es una herramienta de línea de comandos (CLI) escrita en Python que te permite modificar las etiquetas de archivos de audio que contengan metadatos.

## Requisitos

- Python 3.x instalado
- Archivos de audio con metadatos (por ejemplo, MP3, M4A, FLAC, etc.)
- La biblioteca `music-tag`

## Instalación de dependencias

Instala la biblioteca `music-tag` utilizando pip:

```bash
pip install music-tag
```

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/CLImetaTune.git
   ```

2. Navega hasta el directorio del repositorio:

   ```bash
   cd CLImetaTune
   ```

## Uso

Para modificar las etiquetas de un archivo de audio, ejecuta el script `climetatune.py` con los siguientes argumentos:

```bash
python climetatune.py ruta/al/archivo.mp3 --title "Nuevo Título" --album "Nuevo Álbum" --genre "Nuevo Género" --year "2024"
```

Si no proporcionas ningún argumento adicional, se mostrarán las etiquetas actuales del archivo de audio:

```bash
python climetatune.py ruta/al/archivo.mp3
```

## Contribución

Las contribuciones son bienvenidas. Si tienes alguna sugerencia, problema o quieres contribuir al proyecto, por favor crea un issue o envía una pull request.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
