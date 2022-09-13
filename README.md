Para install los paquetes necesarios, ejecutar:

```
poetry install
```

Posteriormente ejecutar:

```
python data_processing.py
```

Este archivo generará las tablas necesarias, los merge y las llamadas al smn. 


###  Ejercicio
__A continuación describo el MVP y respondo a través del cuerpo del ejercicio:__

El equipo de Ciencia de Datos se ha acercado a ti ya que necesitan incorporar información sobre clima dentro de sus modelos predictivos. Para ello, han encontrado el siguiente servicio web: https://smn.conagua.gob.mx/es/web-service-api. Te piden que los apoyes en lo siguiente:

1)	Cada hora debes consumir el último registro devuelto por el servicio de pronóstico por municipio y por hora.

    - Antes de iniciar con la extracción de los datos, iniciaría una conversación con el equipo de ciencia de datos para determinar la granuralidad, la disponibilidad de los datos que solicitan y establer que sucedería si el servicio deja de responder.

    - Posteriormente, hay que tener en cuenta que la información entregada por ese WebService posee dos características a tomar en cuenta para la aplicación que queramos realizar.

        - El WebService regresa un JSON comprimido en GZip.
        - La información se actualiza cada 1 hora.

2)	A partir de los datos extraídos en el punto 1, generar una tabla a nivel municipio en la que cada registro contenga el promedio de temperatura y precipitación de las últimas dos horas.

    - Para este punto necesitamos determinar que variables son necesarias para cumplir con el requerimiento. Estas son "ides", "idmun", "temp", "prec".

    - Debemos determinar una tabla que vaya adjuntando el request y posteriormente buscar los ultimos dos registros en caso de que el equipo deseé conservar eventos historicos.

    - En este paso fue necesario normalizar el tipo de dato para el paso 3.

3)	Hay una carpeta “data_municipios” que contiene datos a nivel municipio organizados por fecha, cada vez que tu proceso se ejecute debe generar una tabla en la cual se crucen los datos más recientes de esta carpeta con los datos generados en el punto 2.

    - Es importante realizar un casteo de las columnas key para el merge, debido a que en la llamada se encuentran como objetos y en los csvs están como int.

4)	Versiona todas tus tablas de acuerdo a la fecha y hora en la que se ejecutó el proceso, en el caso del entregable del punto 3, además, genera una versión “current” que siempre contenga una copia de los datos más recientes.

    - La llamada se puede programar con un cron para que se realice cada hora y el script prosiga con el filtrado del 'historico' de los dos últimos registros y entonces exponer el resultado promedio que los cientificos de datos necesitan en la aplicación.

Preguntas adicionales

- ¿Qué mejoras propondrías a tu solución para siguientes versiones?

    - Propondía una mejora en la gestión de los datos, no es necesario guardar los datos en csv ya que se trata de datos procesados. Podríamos guardarlo en requistro por renglón con un identificador, una versión y el dato json en otro campo. 

    - Además el current podría presentar errores de procesamiento en el caso de que no esté disponible el servicio smn, propondría realizar varios intentos y validar su existencia antes de ejecutar el trigger que llamaría a la aplicación del equipo de CD. Así consumiría datos en caso de que existan errores de comunicación, trafico o disponibilidad.

- Tu solución le ha gustado al equipo y deciden incorporar otros procesos, habrá nuevas personas colaborando contigo, ¿Qué aspectos o herramientas considerarías para escalar, organizar y automatizar tu solución?

    - La solución se podría escalar dentro de un warehouse donde se depositen las versiones de los consumibles en una misma tabla y no es tablas separadas. Esto ayudaría en la organización, rendimiento y en el consumo.

    - Para automatizar y organizar, podríamos realizar una app que llame a un cron para determinar la disponibilidad de los datos, procesarlos y entonces si disponibilizar los resultados antes de reescribir los current y romper el pipeline del equipo de consumo de CDs. 
    