from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/usuario/{id}/historial")    #CAMBIAR LOS PUERTOS
def historial_usuario(id: int):
    usuario = requests.get(f"http://microservicio-usuarios:5000/usuarios/{id}").json() #cambiar
    prestamos = requests.get(f"http://microservicio-prestamos:3000/prestamos/usuario/{id}").json() #cambiar

    historial = []
    for p in prestamos:
        libro = requests.get(f"http://microservicio-libros:8080/libros/{p['id_libro']}").json() #cambiar
        historial.append({
            "libro": libro["titulo"],
            "fecha_prestamo": p["fecha_prestamo"],
            "estado": p["estado"]
        })

    return {
        "usuario": usuario,
        "prestamos": historial
    }
