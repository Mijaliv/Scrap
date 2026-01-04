# README

## Análisis de Mercado Laboral

Bienvenido al repositorio del proyecto **Análisis de Mercado Laboral**, donde podrás explorar una lista de trabajos obtenida a través de técnicas de web scraping. Este proyecto utiliza la librería **Beautiful Soup** en Python para extraer información de ofertas de empleo de la página de CompuTrabajo, y realiza un pequeño análisis de datos sobre el mercado laboral.

### ¿Cómo Funciona?

El script de Python, llamado `ScrapCompuTrab.py`, navega por el sitio de CompuTrabajo, analiza su contenido HTML y extrae detalles de cada oferta de trabajo, incluyendo:

- Título
- Ubicación
- Empresa
- Salario

Una vez extraídos, los datos se guardan en un archivo estático llamado `computrabajo_jobs.json`. Ten en cuenta que la información mostrada en esta página no se actualiza en tiempo real; es una "foto" de los datos en el momento en que se ejecutó el script por última vez.

### Análisis de Datos

Los análisis generados dinámicamente a partir de los datos extraídos ofrecen una visión general del mercado laboral para vendedores, incluyendo:

1. **¿Dónde hay más demanda?** (Distribución Geográfica)
2. **¿Cuánto se puede ganar?** (Análisis Salarial)
3. **¿Quiénes están contratando más?** (Empresas Activas)
4. **¿Qué tipo de vendedores se buscan?** (Tipos de Roles)
5. **¿Qué tan recientes son las ofertas?** (Dinamismo del Mercado)

### Acerca de este Proyecto

Este proyecto fue desarrollado como parte de la materia de **Interfaz de Usuarios** en la carrera de **Desarrollo de Software**. 

### ¿Quieres Probarlo en Tu Propia Máquina?

¡Claro que puedes! Sigue estos pasos para ejecutar el script de scraping y generar una lista actualizada de trabajos:

1. **Prepara tu entorno:** Asegúrate de tener Python instalado. Luego, abre una terminal y crea un entorno virtual para mantener las dependencias aisladas:
   ```bash
   python -m venv .venv
   ```

2. **Activa el entorno virtual:**
   - En **Windows:** 
     ```bash
     .venv\Scripts\activate
     ```
   - En **macOS y Linux:** 
     ```bash
     source .venv/bin/activate
     ```

3. **Instala las librerías necesarias:** Todas las dependencias están listadas en el archivo `requirements.txt`. Instálalas con pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta el script:** Ahora, simplemente ejecuta el script de scraping:
   ```bash
   python ScrapCompuTrab.py
   ```

5. **¡Listo!** Después de unos segundos, verás un archivo `computrabajo_jobs.json` recién creado (o actualizado) en la carpeta del proyecto.

Esta es una excelente manera de practicar tus habilidades de programación y entender cómo funciona el web scraping en el mundo real.

### Acceso a la Página

Puedes acceder a la página aquí: [Análisis de Mercado Laboral](https://mijaliv.github.io/Scrap/)

© 2026 Mijal Nuñez. Todos los derechos reservados.
