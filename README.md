Ejercicio

El equipo de Ciencia de Datos se ha acercado a ti ya que necesitan incorporar información sobre clima dentro de sus modelos predictivos. Para ello, han encontrado el siguiente servicio web: https://smn.conagua.gob.mx/es/web-service-api. Te piden que los apoyes en lo siguiente:

1)	Cada hora debes consumir el último registro devuelto por el servicio de pronóstico por municipio y por hora.

    - Antes de iniciar con la extracción de los datos, una conversación con los cientificos de datos para determinar la granuralidad, la disponibilidad de los datos que solicitan. Esto con la finalidad de determinar si esos datos ya los tenemos almacenados en otro lugar o verdaderamente es necesario realizar la gestión del api del smn. 

    - La información entregada por ese WebService posee dos características destacables a tomar en cuenta dentro de la aplicación que vayas a realizar.

        - El WebService regresa un JSON comprimido en GZip. 
        - La información se actualiza cada 1 hora. 

2)	A partir de los datos extraídos en el punto 1, generar una tabla a nivel municipio en la que cada registro contenga el promedio de temperatura y precipitación de las últimas dos horas.
3)	Hay una carpeta “data_municipios” que contiene datos a nivel municipio organizados por fecha, cada vez que tu proceso se ejecute debe generar una tabla en la cual se crucen los datos más recientes de esta carpeta con los datos generados en el punto 2.

    - Es importante realizar un casteo de las columnas key para el merge, debido a que en la llamada se encuentran como objetos y en los csvs están como int.

4)	Versiona todas tus tablas de acuerdo a la fecha y hora en la que se ejecutó el proceso, en el caso del entregable del punto 3, además, genera una versión “current” que siempre contenga una copia de los datos más recientes.

    - La llamada se puede programar con un cron para que se realice la llamada cada hora y posteriormente realizar el filtrado del 'historico' con los dos últimos registros y entonces exponer el resultado promedio que los cientificos de datos necesitan.

Preguntas adicionales

●	¿Qué mejoras propondrías a tu solución para siguientes versiones?
    - 
●	Tu solución le ha gustado al equipo y deciden incorporar otros procesos, habrá nuevas personas colaborando contigo, ¿Qué aspectos o herramientas considerarías para escalar, organizar y automatizar tu solución?
