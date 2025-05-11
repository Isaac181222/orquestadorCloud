# Microservicio Orquestador - Proyecto Biblioteca

Este microservicio orquestador combina datos de usuarios, libros y préstamos para mostrar el historial de préstamos de cada usuario.
(esta llamando a los 3 microservicios)
## Endpoint principal

`GET /usuario/{id}/historial`

## Requisitos

- Python 3.10
- Docker
- FastAPI

## Ejecución

```bash
docker build -t orquestador .
docker run -p 8000:8000 orquestador
