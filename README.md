# Script 1
Basicamente este script actua sobre una zona delimitada que conseguimos gracias a la herramienta BoundingBox. recopila datos de Tweets de esta zona y los almacena en nuestra base de datos de CouchDB que en esta ocasion la he llamado "juegosolimpicos"
![Screenshot_65](https://user-images.githubusercontent.com/58042023/127719497-2390a8fa-37fe-4959-b934-e79f5ac36b73.png)

para seguir las indicaciones del examen este proceso se lo hace en 3 ciudades distintas:
#### Tokio
![Screenshot_63](https://user-images.githubusercontent.com/58042023/127719790-a23220ad-dd3d-4c4c-9219-635bb2eabfd9.png)
Captura de coordenadas de Tokio
#### Fukushima
![Screenshot_66](https://user-images.githubusercontent.com/58042023/127719835-5999d555-bd49-4f7c-b5ec-76a17485ff9c.png)
Captura de coordenadas de Fukushima
#### Mito
![Screenshot_67](https://user-images.githubusercontent.com/58042023/127719927-7c66428a-6c0a-46ef-bcc2-23c69853cf89.png)
Captura de Coordenadas de Mito

# Script 2
Para el segundo Script solo modificamos la forma de filtrar. para esto he ingresado palabras como "olimpicos", "juegos", "medallas"...
![Screenshot_68](https://user-images.githubusercontent.com/58042023/127720279-871ec382-e31c-4ead-bcd3-801e3e389a4f.png)

# Script 3
Creamos una base de datos dentro de MongoDB conectandonos a localhost llamada "JegosOlimpicosMongo" y una coleccion dentro de la misma llamada "elcomercio", esto para almacenar posteriormente los datos que obtengamos
![Screenshot_69](https://user-images.githubusercontent.com/58042023/127721972-0a55f31d-32aa-4df7-a835-9e30f89f104b.png)

El Script básicamente busca los patrones que le asignamos, en este caso un elemento con el tag "<p>", y limpia todo lo que no sea el texto.
Luego, nos conectamos a nuestra base de datos "JuegosOlimpicosMongo" para asignar lo extraido a la colleccion llamada "elcomercio"
Despues de ejecutar el codigo se guardaran todo lo que hemos extraido en formato json
![image](https://user-images.githubusercontent.com/58042023/127723339-e2708ed0-31c8-43cb-8b54-7841de881470.png)


# Script 4
Utilizamos la herramienta facebook-scraper para obtener publicaciones de una determinada pagina de Facebook, en este caso de "ELDEMENTEYT"
laherramienta almacena los likes, comentarios, reacciones de estas publicaciones y las almançena para posterior mente asiganors a nuestra base de datos "JuegosOlimpicosMongo" para asignar lo extraido a la colleccion llamada "elcomercio".
Cuando ejecutamos el codigo se recibe mensajes de que una publicacion se guardo correctamente:  
![image](https://user-images.githubusercontent.com/58042023/127724105-6d51b9dc-7207-4c5f-9199-1b9dff89920f.png)
 
Resultado de almacenar en MongoDB:  
 ![image](https://user-images.githubusercontent.com/58042023/127724061-c709906a-1094-4a04-8969-f27b4531a341.png)


# Script 5

# Script 6

# Script 7

# Script 8

# Script 9

# Script 10


