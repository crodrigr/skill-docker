# 🐳 Ejemplo 04 — Docker Compose: app + Redis

Archivo: [app/compose.yaml](app/compose.yaml). Levanta **dos contenedores** con un solo
comando: la app (se construye con el [Dockerfile](app/Dockerfile)) y Redis (imagen lista de
Docker Hub).

## 💻 Comandos

```bash
cd ejemplos/app

docker compose up -d --build     # construye si hace falta y arranca todo
curl localhost:5000              # "…se visitó 1 veces."
curl localhost:5000              # "…se visitó 2 veces."

docker compose ps                # estado de los servicios
docker compose logs web          # registros de un servicio

docker compose down              # detiene y borra contenedores y red (conserva el volumen)
docker compose up -d             # el contador CONTINÚA: los datos viven en el volumen
docker compose down -v           # borra también el volumen (contador de vuelta a cero)
```

## 🔍 Explicación paso a paso

| Línea de `compose.yaml` | Qué hace |
|---|---|
| `build: .` | Construye la imagen de `web` con el Dockerfile de esta carpeta |
| `ports: "5000:5000"` | Publica el puerto en tu equipo |
| `REDIS_HOST: redis` | La app encuentra a Redis por el **nombre del servicio**: Compose crea una red donde los servicios se resuelven por nombre |
| `depends_on` | Arranca `redis` antes que `web` |
| `volumes: datos-redis` | Guarda los datos de Redis fuera del contenedor |

## ✅ Resultado esperado

El contador sube con cada `curl`, y sigue subiendo después de `down` + `up -d`. Con
`down -v` vuelve a empezar en 1.
