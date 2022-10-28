implementa una modificacion para dejar fuera los fuentes del contenedor para produccion

Generar Docker
> docker build -t test:1.0 .

Revisar Contenido contenedor
> docker run -it test:1.0 sh

Aplicacion funcionando:
> docker run test:1.0

Resultado obtenido ahora:
>/src # ls
>Dockerfile  Readme.md   main.go     main


Resultado esperado:
>/src # ls
> main

