# Ingeniería en Sistemas — Sitio Web Flask

Sitio web futurista sobre la carrera de Ingeniería en Sistemas, hecho para la Feria de los Sueños del colegio.

## Estructura del Proyecto

```
Feria_de_los_sueños/
├── app.py                   # Servidor Flask
├── requirements.txt
├── static/
│   ├── css/
│   │   └── style.css        # Estilos futuristas neon
│   ├── images/              # (opcional) imágenes — créala si la necesitas
│   └── videos/              # (opcional) videos/GIFs — créala si la necesitas
└── templates/
    ├── base.html            # Plantilla base (navbar, rain effect, footer)
    ├── index.html           # Página principal
    ├── ramas.html           # Ramas y especializaciones
    └── empleos.html         # Empleos y salidas laborales
```

## Instalación y Ejecución

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
python app.py
```

Luego abre: http://localhost:5000

## Para agregar media

- **Imágenes**: Colocar en `static/images/` y referenciar con:
  ```html
  <img src="{{ url_for('static', filename='images/tu-imagen.png') }}">
  ```
- **Videos**: Colocar en `static/videos/` y referenciar con:
  ```html
  <video src="{{ url_for('static', filename='videos/tu-video.mp4') }}"></video>
  ```
- **GIFs**: Colocar en `static/images/` igual que las imágenes.

## Páginas

| Ruta       | Descripción                           |
|------------|---------------------------------------|
| `/`        | Página principal — qué es la carrera  |
| `/ramas`   | Ramas y especializaciones             |
| `/empleos` | Empleos, salarios y trayectoria       |

## Uso de IA

Hice este proyecto con ayuda de **Claude** (Anthropic) como asistente de programación. Me ayudó a generar y revisar partes del código, los estilos y esta documentación. La idea, el contenido y la revisión final son míos.
