# Procesamiento de Imágenes y Extracción de Información con Google Document AI

## Descripción del Código

Este script en Python utiliza Google Document AI para procesar imágenes y extraer información OCR, guardando los resultados en formato JSON. A continuación se detalla el proceso llevado a cabo por el script:

1. **Configuración y Librerías**:
   - Se configuran los directorios de entrada y salida.
   - Se especifican las extensiones de los archivos de imagen a procesar.
   - Se configura Google Document AI con las credenciales necesarias y los parámetros de procesamiento.

2. **Funciones Principales**:
   - **`process_document`**: Procesa una imagen utilizando Google Document AI, enviando la imagen y recibiendo un documento con la información OCR.
   - **`ocr`**: Guarda la respuesta de Document AI en un archivo JSON, manteniendo la estructura original del documento procesado.

3. **Función `main`**:
   - **Recopilación de Archivos**: Busca todas las imágenes en el directorio especificado con las extensiones dadas.
   - **Procesamiento de Imágenes**: Itera sobre cada imagen, procesándola con `process_document` y guardando el resultado con `ocr`.
   - **Gestión de Errores**: Maneja posibles errores durante el procesamiento y continúa con la siguiente imagen.

## Ejecución del Script

El script se ejecuta llamando a la función `main()`, que se encarga de procesar todas las imágenes en el directorio de entrada y guardar los resultados en el directorio de salida. Para ejecutar el script, asegúrate de tener configuradas las credenciales de Google Document AI y de tener las librerías necesarias instaladas.

```bash
python dai_ocr.py
```
