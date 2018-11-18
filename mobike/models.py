from django.db import models

class Cliente(models.Model):
    MEDIO_PAGO = (
    ('Debito', 'debito'),
    ('Credito', 'credito'),
    ('TarjetaMunicipal', 'tarjetamunicipal'),
)
    ID_CLIENTE = models.AutoField(primary_key=True)
    RUT = models.CharField(max_length=200)
    NOMBRE_COMPLETO = models.CharField(max_length=200)
    EDAD  = models.IntegerField()
    MEDIO_PAGO = models.CharField(max_length=30, choices=MEDIO_PAGO)
    NUMERO_CELULAR = models.CharField(max_length=200)
    EMAIL = models.CharField(max_length=200)

    def __str__(self):
        return self.NOMBRE_COMPLETO

class Bicicleta(models.Model):
    ESTADO_CANDADO = (
    ('Bloqueado', 'bloqueado'),
    ('Libre', 'libre'),
)
    ID_MOBIKE = models.AutoField(primary_key=True)
    COORDENADAS = models.CharField(max_length=200)
    CODIGO_BICICLETA = models.CharField(max_length=140)
    ESTADO_CANDADO  = models.CharField(max_length=200, choices=ESTADO_CANDADO)

    def __str__(self):
        return self.CODIGO_BICICLETA

class Arriendo(models.Model):
    ID_ARRIENDO = models.AutoField(primary_key=True)
    CODIGO_ARRIENDO = models.CharField(max_length=140)
    HORA_REGISTRO = models.TimeField(null=True)
    ID_MOBIKE = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    ID_CLIENTE = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.CODIGO_ARRIENDO
