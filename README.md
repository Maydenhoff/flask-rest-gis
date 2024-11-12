# Weather API

#### Requisitos:
- Python3 
- Entorno virtual de Python
- Docker y Docker Compose

#### Instalacion del entorno
1. Crea un entorno virtual e instala las dependencias:
``` bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
2. Inicializar la base de datos
```bash
docker-compose up
```
3. Crear archivo .env
```env
DB_USER='user'
DB_PASSWORD='pasword'
DB_HOST=localhost
DB_PORT='1234'
DB_NAME='db-name'
DB_TRACK_MODIFICATIONS=False
```
4. Ejecutar la app
```bash
python3 run.py
```

## API routes

####  `POST /weather_stations`

Crea una nueva *Weather Station*.

- **Body:**
    ```json
    {
        "name": "Test",
        "latitude": 3.342,
        "longitude": 5.423423
    }
    ```
- **Respuestas:**
  - **201 Created**: Si la Weather Station es creada correctamente.
    ```json
    {
      "message": "Weather Station creada exitosamente.",
      "id": 2
    }
    ```
  - **400 Bad Request**: Si alguno de los campos son invalidos
    ```json
    {   
      "error": "Esquema invalido.",
      "errorsValidation": {
          "latitude": [
              "Not a valid number."
          ],
          "longitude": [
              "Not a valid number."
          ],
          "name": [
              "Not a valid string."
          ]
        }
    }
    ```

  - **400 Bad Request**: Si la Weather Station con ese "name" ya existe
    ```json
    {
      "error": "Weather station ya existente con ese nombre."
    }
    ```
### 2. `GET /weather_stations/nearest/<lat>,<long>`
Obtiene la *Weather Station* mas cercana.

- **Parámetros de consulta**:
  - `lat` (requerido, flotante): Latitud
  - `long` (requerido, flotante): Longitud 

- **Respuestas:**
  - **200 OK**: 
    ```json
    {

    "weather_stations": {
        "id": 2,
        "latitude": 19.03304,
        "location": "0101000020e6100000bb0ed594648e58c0b875374f75083340",
        "longitude": -98.224889,
        "name": "Estación 2",
        "weather_data": [
            {
                "humidity": 0.5,
                "id": 3,
                "pressure": 1015.2,
                "station_id": 2,
                "temperature": 22.8,
                "timestamp": "2023-03-19T10:00:00"
            }
        ]
      }
    }
    ```
  - **400 Bad Request**: Si los campos son invalidos
    ```json
    {
      "error": "Parametros invalidos.",
      "errors_validation": {
        "latitude": [
            "Latitude must be between -90 and 90."
        ],
        "longitude": [
            "Longitude must be between -180 and 180."
        ]
      }
    }
    ```
  - **404 Not Found**: Si no se encuentra Weather Station
    ```json
      {
        "error": "No se encontraron weather stations" 
      }
    ```

### 3. `PUT /weather_stations`

Actualiza una Weather Station existente.

- **Body**: Requiere el siguiente cuerpo en formato JSON.
    ```json
    { 
      "id": 23,
      "latitude": 3.12,
      "longitude": 20.234
    }
    ```
- **Respuestas**:
  - **200 OK**: Si la estación meteorológica es actualizada correctamente.
    ```json
    {
      "id": 2,
      "message": "Estacion metereologica actualizada con exito."
    } 
    ```
  - **404 Not Found**: Si no se encuentra la estación meteorológica con el `id` proporcionado.
    ```json
    {
    "error": "Weather station con id 33 no encontrada."
    }
    ```
  - **400 Bad Request**: Si los campos son invalidos
    ```json
    {
      "error": "Parametros invalidos.",
      "errors_validation": {
        "latitude": [
            "Latitude must be between -90 and 90."
        ],
        "longitude": [
            "Longitude must be between -180 and 180."
        ]
      }
    }
    ```

### 4. `DELETE /weather_stations/<id>`

Elimina una weather station específica.

- **Parámetros**:
  - `id`: (requerido, entero).
- **Respuestas**:
  - **200 OK**: Si la Weather Station es eliminada correctamente.
    ```json
    {
      "message": "Weather station con id 3 eliminada con exito"
    }
    ```
  - **404 Not Found**: Si no se encuentra la Weather Station con el `id` proporcionado.
    ```json
    {
      "error": "Weather station con id 3 no encontrada."
    } 
    ```