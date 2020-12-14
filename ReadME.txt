SantanderChallenge - Comentarios
# El archivo con la solución es Challenge.py
  - toma el archivo de la carpeta data y deposita el procesado en la carpeta output
  - la denominación de los archivos de entrada y de salida se puede cambiar en el archivo Challenge.py
# Las respuestas a las preguntas estan en el archivo: respuestas.txt
# La imagen 'Arquitectura.png" es un soporte a las respuesta 3

Respuestas:

1- 
Para la cola de mensajes (no tengo experiencia en este tipo de implementaciones) utilizaría JAVA (JMS) porque me siento cómodo utilizando el lenguaje.
Para la parte de solución de datos:
Lo implementaría en una solución donde tuviera que procesar grandes volúmenes de datos y evitar cuellos de botella en el procesamiento.
Por ejemplo. Una solución que procesa pedidos. En momentos de elevada concurrencia puede producir degradamiento en las infraestructuras y generar problemas de rendimiento en la aplicación.
Otro caso podría ser cuando consumimos información de una API con restricciones de solicitudes. Poniendo un robot que ejecute los “request” en determinado momento y poniendo en cola todas las respuestas que luego serán procesadas.
El lenguaje que utilizaría para este procesamiento sería Python porque: 
Es sencillo de implementar y existe mucha información de referencia.
Cuenta con un monton de librerias que estan preparados para el procesamiento y análisis de grandes volúmenes de datos
Se integra de manera sencilla con múltiples plataformas
Tiene mejor performance para el procesamiento que otros lenguajes (por ejemplo R)
	
2-
No tengo experiencia trabajando con Spark. Si lo he visto en capacitaciones que he hecho y entiendo a grandes rasgos cómo funciona.

3-Desarrollaría un API que contuviera métodos reutilizables para el procesamiento de datos. De esta manera fomentaría la reutilización del código y facilitaría el mantenimiento de los scripts. 
Estos métodos podrían:
	- Obtener información relevante de otras plataformas 
	- Realizar conversiones
	- Extracción de datos en servidores o servicios
	- Modificar valores en DBs de terceros
	- Obtener visualizaciones mediante parámetros de entrada
	- Publicación de datos

Ejemplo:
MÉTODO: OBTENER VIZ
TIPO:GET | ENDPOINT: https://<server>:<port>/apiData/viz=100 |

MÉTODO: OBTENER CONVERSIONES 
TIPO:POST | ENDPOINT: https://<server>:<port>/apiData/conversiones | BODY: JSON

MÉTODO: PUBLICAR DATOS | 
TIPO:POST | ENDPOINT: https://<server>:<port>/apiData/publicar | BODY: JSON

Adjunto imagen con posible arquitectura.


