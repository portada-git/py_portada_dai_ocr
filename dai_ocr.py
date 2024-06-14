import os
import json
import glob
from google.api_core.client_options import ClientOptions
from google.cloud import documentai
from google.protobuf.json_format import MessageToDict

# Configuración
FOLD_IN = "ruta_a_las_imagenes"
FOLD_OUT = "ruta_a_los_jsons"
EXTENSIONES = ['jpg', 'png', 'jpeg']
LOCATION, PROJECT_ID, PROCESSOR_ID, PROCESSOR_VERSION = 'us', 'mystic-primacy-xxxxxx', 'cxxxxxxxxxx0', "rc"
MIME_TYPE = "image/jpeg"

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'api_dai.json'

process_options = documentai.ProcessOptions(
    ocr_config=documentai.OcrConfig(
        enable_native_pdf_parsing=True,
        enable_image_quality_scores=True,
        enable_symbol=True,
    ),
)

def process_document(file_path: str) -> documentai.Document:
    client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
    )
    name = client.processor_version_path(PROJECT_ID, LOCATION, PROCESSOR_ID, PROCESSOR_VERSION)
    with open(file_path, "rb") as image_file:
        image_content = image_file.read()
    
    request = documentai.ProcessRequest(
        name=name,
        raw_document=documentai.RawDocument(content=image_content, mime_type=MIME_TYPE),
        process_options=process_options,
    )
    return client.process_document(request=request).document

def ocr(file_path, document):
    base_name = os.path.basename(file_path).split('.')[0]
    json_name = f"{base_name}_documentai.json"
    # Guardar el response en JSON
    with open(os.path.join(FOLD_OUT, json_name), "w") as f:
        f.write(json.dumps(MessageToDict(document._pb), indent=2))

def main():
    archivos = [file for ext in EXTENSIONES for file in glob.glob(f"{FOLD_IN}/*.{ext}")]
    for i, file_path in enumerate(archivos, start=1):
        print(f"Procesando {file_path}, {i} de {len(archivos)}")
        try:
            document = process_document(file_path)
            ocr(file_path, document)
        except Exception as e:
            print(f"Error al procesar {file_path}: {e}")

    print('Proceso terminado')

if __name__ == "__main__":
    main()
