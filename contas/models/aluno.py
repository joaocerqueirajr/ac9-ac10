from django.db import models

class Aluno(models.Model):
    
    nome = models.CharField("Nome Completo", max_length=155)
    email = models.EmailField("E-mail")
    celular = models.CharField("Celular", max_length=11)
    ra = models.IntegerField("RA", unique=True)
    usuario = models.ForeignKey('contas.Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nome)
        
    class Meta:
        db_table = 'ALUNO'