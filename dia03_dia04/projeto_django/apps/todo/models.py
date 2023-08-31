from django.db import models

# Create your models here.
class Task(models.Model): #criar tabela do banco de dados
    name = models.CharField(max_length=200)

    description = models.TextField()

    date = models.DateField()

    def __str__(self): #modifica a forma que a classe aparece
        return self.name