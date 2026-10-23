# 🐳 Ejemplo 01 — Primeros contenedores

> 📌 **Requisito:** Docker instalado (ver la [guía](../README.md#-4-instalación-y-configuración)).

## 💻 Comandos

```bash
# 1) El "hola mundo": descarga la imagen y ejecuta un contenedor que imprime un mensaje y termina
docker run hello-world

# 2) Un servidor web en segundo plano, accesible en http://localhost:8080
docker run -d --name mi-web -p 8080:80 nginx:alpine

# 3) Ver qué está corriendo y probarlo
docker ps
curl http://localhost:8080

# 4) Ver los registros (logs) y entrar al contenedor
docker logs mi-web
docker exec -it mi-web sh        # escribí `exit` para salir

# 5) Detener y borrar
docker stop mi-web
docker rm mi-web
```

## 🔍 Explicación paso a paso

| Comando | Qué pasa |
|---|---|
| `docker run hello-world` | Docker no encuentra la imagen en tu equipo → la descarga de Docker Hub → crea un contenedor → lo ejecuta → el contenedor termina |
| `-d` | *detached*: corre en segundo plano y te devuelve la terminal |
| `--name mi-web` | Le da un nombre fácil de recordar (si no, Docker inventa uno) |
| `-p 8080:80` | Conecta el puerto **8080 de tu equipo** con el puerto **80 del contenedor** |
| `docker exec -it mi-web sh` | Abre una terminal **dentro** del contenedor que ya está corriendo |

## ✅ Resultado esperado

- `docker ps` muestra `mi-web` con estado `Up`.
- `curl` devuelve el HTML de bienvenida de nginx.
- Tras `docker rm`, `docker ps -a` ya no lo lista.
