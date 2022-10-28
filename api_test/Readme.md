# Para el siguiente problema crear cliente rest que pueda consumir la api rest. Se debe
# listar todas las personas (imprimir todos los datos del objeto), 
# posteriormente buscar en el listado las persona con apellido paterno Lara (imprimir todos los datos del objeto).


# **********************************************************
# INSTALACIÓN LOCAL
# **********************************************************

# Instalar libreria para entorno virtual
pip install virtualenv

# Crear entorno virtual
virtualenv env

# Activar entorno virtual en linux
source env/bin/activate

# Activar entorno virtual en windows
. env/Scripts/activate

# Desplegar proyecto
python main.py

# **********************************************************
# CONTENEDOR
# **********************************************************
# Docker 
sudo docker build -t apipython:1.0.0 .
sudo docker run -d apipython:1.0.0
