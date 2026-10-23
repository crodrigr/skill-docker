# 🐳 Ejemplo 03 — Publicar una imagen en Docker Hub

> 📌 **Requisitos:** una cuenta gratuita en [hub.docker.com](https://hub.docker.com) y la
> imagen `contador:1.0` del [ejemplo 02](02-dockerfile.md).

Reemplazá `TU_USUARIO` por tu usuario de Docker Hub.

## 💻 Comandos

```bash
# 1) Iniciar sesión (pide usuario y contraseña o token de acceso)
docker login

# 2) Ponerle a la imagen el nombre completo: usuario/repositorio:etiqueta
docker tag contador:1.0 TU_USUARIO/contador:1.0

# 3) Subirla
docker push TU_USUARIO/contador:1.0

# 4) Comprobar que cualquiera puede bajarla (probalo borrando la local primero)
docker rmi TU_USUARIO/contador:1.0
docker pull TU_USUARIO/contador:1.0
```

## 🔍 Explicación paso a paso

| Paso | Por qué |
|---|---|
| `docker tag` | Docker Hub exige el formato `usuario/nombre`. `tag` no copia la imagen: solo agrega **otro nombre** a la misma. |
| `docker push` | Sube solo las capas que el repositorio todavía no tiene. |
| `docker pull` | Descarga la imagen en cualquier equipo con Docker. |

> 💡 Usá un **token de acceso** (Docker Hub → Account Settings → Security) en vez de tu
> contraseña, sobre todo en scripts o servidores.

## ✅ Resultado esperado

En `hub.docker.com/r/TU_USUARIO/contador` aparece la imagen con la etiqueta `1.0`.
