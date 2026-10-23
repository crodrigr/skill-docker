# 🐳 Ejemplo 02 — Construir una imagen con Dockerfile

La app es un contador de visitas en Flask. Los archivos están en [app/](app/):

- [app/app.py](app/app.py) — la aplicación
- [app/requirements.txt](app/requirements.txt) — sus dependencias
- [app/Dockerfile](app/Dockerfile) — la receta de la imagen
- [app/.dockerignore](app/.dockerignore) — lo que NO se copia a la imagen

> 💡 Esta app guarda el contador en Redis, así que **sola** arranca, pero responde con
> error 500 al recibir una visita (no encuentra Redis). Eso es intencional: en el [ejemplo 04](04-compose.md) se levanta junto
> a Redis con Compose. Aquí el objetivo es ver **cómo se construye la imagen**.

## 💻 Comandos

```bash
cd ejemplos/app

# Construir la imagen y ponerle nombre:etiqueta
docker build -t contador:1.0 .

# Verla en la lista de imágenes y ver sus capas
docker images contador
docker history contador:1.0
```

## 🔍 Explicación paso a paso

Cada instrucción del Dockerfile crea una **capa**. Docker guarda las capas en caché:

1. `FROM python:3.12-slim` — parte de una imagen base con Python.
2. `COPY requirements.txt .` + `RUN pip install ...` — las dependencias van **antes** que el
   código a propósito: si solo cambiás `app.py`, esas capas se reutilizan y el build es rápido.
3. `COPY app.py .` — el código, que es lo que más cambia.
4. `CMD [...]` — el comando que se ejecuta cuando arranca un contenedor de esta imagen.

## 🧪 Pruébalo: la caché en acción

Corré `docker build -t contador:1.0 .` otra vez: todas las capas dicen `CACHED`. Ahora
cambiá una línea de `app.py` y volvé a construir: solo se rehace desde `COPY app.py`.

## ✅ Resultado esperado

`docker images contador` muestra `contador   1.0` con un tamaño de unos 135 MB.
