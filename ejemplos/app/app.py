import os

import redis
from flask import Flask

app = Flask(__name__)
# El host "redis" es el NOMBRE del servicio en compose.yaml: Docker lo resuelve solo.
cache = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)


@app.route("/")
def inicio():
    visitas = cache.incr("visitas")
    return f"¡Hola desde Docker! Esta página se visitó {visitas} veces.\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
