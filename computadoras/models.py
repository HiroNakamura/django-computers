# coding: utf-8

from django.db import models
from django.utils import timezone

class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    
    def __str__(self):
        return "Departamento{id:"+str(self.id)+", area:"+self.area+", responsable:"+self.responsable+"}"


class Computadora(models.Model):
    id = models.AutoField(primary_key=True)
    bien = models.CharField(max_length=50,default='MXL4332-')
    arrendado = models.CharField(max_length=50,default='77')
    asignado = models.IntegerField(default=0)
    ip = models.GenericIPAddressField(default='148.215.24.1')
    dns = models.GenericIPAddressField(default='148.215.1.1')
    red = models.CharField(max_length=50)
    OPERATIVO_CHOICES = (
        ('Windows XP', 'Windows XP'),
        ('Windows 7', 'Windows 7'),
        ('Windows Vista', 'Windows Vista'),
        ('Windows 8', 'Windows 8'),
        ('Windows 10', 'Windows 10'),
        ('Linux OS', 'Linux OS'),
        ('Mac OS X','Mac OS X'),
        ('No especificado','No especificado'),
    )

    TIPO_CHOICES = (
        ('Escritorio', 'Escritorio'),
        ('Portatil', 'Portatil'),
        ('No especificado','No especificado'),
    )

    PISO_CHOICES = (
        ('PISO 1', 'PISO 1'),
        ('PISO 2', 'PISO 2'),
        ('PISO 3','PISO 3'),
        ('PISO 4','PISO 4'),
        ('PISO 0','PISO 0'),
    )

    AREAS_CHOICES = (
        ('Direccion general', 'Direccion general'),
        ('Sistemas de informacion','Sistemas de informacion'),
        ('Recursos humanos' ,'Recursos humanos'),
        ('Recursos humanos','Recursos humanos'),
        ('Evaluacion','Evaluacion'),
        ('Hemeroteca','Hemeroteca'),
        ('Diseño y comunicacion','Diseño y comunicacion'),
    )

    operativo = models.CharField(max_length=50,choices=OPERATIVO_CHOICES, default='Windows 8')
    tipo = models.CharField(max_length=50,choices=TIPO_CHOICES, default='Escritorio')
    maquina = models.CharField(max_length=50,default='PC77')
    dominio = models.CharField(max_length=50, default='PC77')
    modelo = models.CharField(max_length=50)
    administrador = models.CharField(max_length=50, default='SOPTEC REDALYC')
    ubicacion = models.CharField(max_length=50,choices=PISO_CHOICES, default='PISO 2')
    actualizada = models.BooleanField(default=False)
    departamento = models.CharField(max_length=50,choices=AREAS_CHOICES, default='Hemeroteca') #Departamento() #models.ForeignKey(Departamento)


    def __str__(self):
        actualizada = "Actualizada" if self.actualizada==True else "No actualizada"
        return "Computadora{id:"+str(self.id)+",bien:"+ self.bien +", asignado:"+str(self.asignado)+", Ip:"+self.ip +", Dns:"+self.dns+", red:"+self.red+", operativo:"+self.operativo+", tipo:"+self.tipo+", maquina:"+self.maquina+", dominio:"+self.dominio+", modelo:"+self.modelo+", admin:"+self.administrador+", ubicacion:"+self.ubicacion+", actualizada:" +actualizada+", departamento: "+str(self.departamento) +"}"
        
        
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):        
        return self.choice_text