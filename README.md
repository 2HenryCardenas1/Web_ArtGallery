# Pagina web usando Django :snake:



En este proyecto se desarrollo una pagina web para una galreia de arte en la cual con un usuario administrador podras:
```
1)Crear, eliminar o actualizar una obra de arte

2)Crear, eliminar o actualizar a un artista

3)Crear, eliminar o actualizar una categoria de arte


```

Como usuario podras buscar obras de arte o categorias, ver la informacion de cada obra, poder comprar una obra ya que se simulo el proceso de pago con payu,entre otras opciones dentro de la pagina.


## Comenzando 🚀

### Pre-requisitos 📋

_Estas son las herramientas que debe de tener instaladas para el funcinamientocdel proyecto_

```

-Postgresql
-Python3
-Un editor de codigo(PyCharm,VisualStudio,etc..)

```

### Instalación 🔧

_Estos son los pasos para la instalacion del proyecto_

_1)Clonar repositorio_

```
git clone https://github.com/2HenryCardenas1/pageUniversesComics
```

_2)En **postgresql** crear una base de datos_

```
Puede ser por consola o dentro del la interfaz web que nos otorga posgresql que es pgadmin
```

_3)Dentro de nuestro editor de codigo instalamos el entorno virtual_

```
En una terminal instalamos y activamos el entorno virtual de la siguiente manera:
  -pip install virtualenv
  -python -m venv my_env
  -my_env\Scripts\activate.bat
```

_4)Instalamos Django_

```
pip install "Django==3.0.*"
```

_5)En el arcivo settings.py vamos a editarlo_

```
En la parte de DATABASES ponemos lo siguiente
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',  # env
        'NAME': '',  # env #poner dentro de las comillas el nombre de la bd que creamos en el paso dos
        'USER': 'postgres',  # env #si usamos otro usuario diferente a postgres lo ponemos dentro de las comillas
        'PASSWORD': '',  # env #poner la contraseña del usuario postgres
    }
}
```

_6)Generar las tablas desde django_

```
En una terminal pondremos :
  1) python manage.py makemigrations
  2) python manage.py migrate
```

_7)Llenamos con datos la  base de datos_

###### Importante
```
Debemos crear unas categorias primero antes de asignar una obra de arte a una categoria.
```

_8)Creamos un usuario admin para el login_

```
 En una terminal pondremos :
  1) python manage.py createsuperuser
  2) Ponemos los datos que nos pidan
 ```

_9)Corremos el proyecto_

```
En una terminal pondremos :
  python manage.py runserver  
```

__Una vez terminado,deberia de correr el proyecto__


## Construido con 🛠️

_Estas fueron las herramientas que se utilizazron en el proyecto_

* [Postgresql](https://www.postgresql.org/download/) - El software de base de datos usado 
* [Python3](https://www.python.org/downloads/) - El lenguaje de programacion 
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/#section=windows) - Editor de codigo


## Versionado 📌

Versiones disponibles, mira los [tags en este repositorio](https://github.com/2HenryCardenas1/WebSite_ArtGallery/tags).

## Autores ✒️

* **Henry Esteban Cardenas Aleman** - [2HenryCardenas1](https://github.com/2HenryCardenas1)
