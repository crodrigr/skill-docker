# 1) Imagen base: Python ya instalado
FROM python:3.12-slim

# 2) Carpeta de trabajo dentro de la imagen
WORKDIR /app

# 3) Primero las dependencias: si no cambian, Docker reutiliza esta capa (caché)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Después el código, que cambia más seguido
COPY app.py .

# 5) Documenta el puerto y define qué se ejecuta al arrancar
EXPOSE 5000
CMD ["python", "app.py"]
