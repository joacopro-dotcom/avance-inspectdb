# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Usuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=50)
    region = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'USUARIOS'


class Juegos(models.Model):
    id_juego = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    popularidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'juegos'


class UsuarioJuegos(models.Model):
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_juego = models.ForeignKey(Juegos, models.DO_NOTHING, db_column='id_juego', blank=True, null=True)
    horas_jugadas = models.IntegerField(blank=True, null=True)
    consola = models.CharField(max_length=50)
    idioma = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_juegos'
