from django.db import models


class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Pieza(models.Model):
    nombre_pieza = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.FloatField()
    small_descripcion = models.TextField()
    big_descripcion = models.TextField()
    imagen = models.CharField(max_length=255)
    imagen2 = models.CharField(max_length=255)
    imagen4 = models.ImageField(null=True)

    def __str__(self):
        return self.nombre_pieza,self.id


class Facturacion(models.Model):
    nombre_usuario = models.CharField(max_length=250)
    apellido_usuario = models.CharField(max_length=250)
    direccion = models.CharField(max_length=300)
    email = models.EmailField()
    ciudad = models.CharField(max_length=300)
    departamento = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=6)
    pieza_id_pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_usuario