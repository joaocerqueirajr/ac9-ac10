from django.db import models

TIPOS_CURSO = (
    ('TEC', 'Técnico'),
    ('G', 'Graduação'),
    ('POS', 'Pós-Graduação'),
    ('MBA', 'Master of Business Administration'),
)

TIPOS_GRADUACAO = (
    ('B', 'Bacharelado'),
    ('T', 'Tecnólogo'),
)

class Curso(models.Model):
    nome = models.CharField('Nome', max_length=260)
    sigla = models.CharField('Sigla', max_length=5, unique=True)
    sobre = models.TextField('Sobre o curso', null=True)
    duracao = models.SmallIntegerField('Semestre')
    tipo_curso = models.CharField('Tipo de Curso', max_length=3, choices=TIPOS_CURSO)
    tipo_graduacao = models.CharField('Tipo de Graduação', max_length=1, choices=TIPOS_GRADUACAO)
    matutino = models.BooleanField('Matutino', null=False)
    vespertino = models.BooleanField('Vespertino', null=False)
    noturno = models.BooleanField('Noturno', null=False)

    def __str__(self):
        return f'{self.nome}, {self.tipo_curso}, {self.tipo_graduacao}'

    class Meta:
        db_table = 'CURSO'