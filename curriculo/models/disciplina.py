from django.db import models

STATUS = (
    ('ABERTO','Aberta'),
    ('FECHADO', 'Fechada')
)

class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=30, unique=True)
    identificador = models.CharField('Identificador', max_length=30, unique=True)
    data = models.DateField("Data de Início", auto_now_add=True)
    status = models.CharField("Status", max_length=10, choices=STATUS)
    carga_horaria = models.SmallIntegerField("Carga Horária")
    percentual_pratico = models.SmallIntegerField("Percentual Prático")
    percentual_teorico = models.SmallIntegerField("Percentual Teórico")
    plano_de_ensino = models.TextField("Plano de Ensino", blank=True)
    competencias = models.TextField("Competências", blank=True)
    habilidades = models.TextField("Habilidades", blank=True)
    ementa = models.TextField("Ementa", blank=True)
    conteudo_programatico = models.TextField("Conteúdo Programático", blank=True)
    bibliografia_basica = models.TextField("Bibliografia Básica", blank=True)
    bibliografia_complementar = models.TextField("Bibliografia Complementar", blank=True)

    def __str__(self):
        return f'{self.nome} - {self.carga_horaria} horas'

    class Meta:
        db_table = 'DISCIPLINA'

class SolicitacaoMatricula(models.Model):
    nome = models.CharField('Nome', max_length=30, unique=True)
    identificador = models.CharField('Identificador', max_length=30, unique=True)
    data = models.DateField('Data de Início', auto_now_add=True)
    status = models.CharField('Status', max_length=10, choices=STATUS)
    carga_horaria = models.SmallIntegerField('Carga Horária')
    percentual_pratico = models.SmallIntegerField('Percentual Prático')
    percentual_teorico = models.SmallIntegerField('Percentual Teórico')
    plano_de_ensino = models.TextField('Plano de Ensino', blank=True)
    competencias = models.TextField("Competências", blank=True)
    habilidades = models.TextField("Habilidades", blank=True)
    ementa = models.TextField("Ementa", blank=True)
    conteudo_programatico = models.TextField("Conteúdo Programático", blank=True)
    bibliografia_basica = models.TextField("Bibliografia Básica", blank=True)
    bibliografia_complementar = models.TextField("Bibliografia Complementar", blank=True)

    class Meta:
        db_table = 'SOLICITACAO_MATRICULA'

class DisciplinaOfertada(models.Model):
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.CharField(max_length=1)
    metodologia = models.TextField(max_length=255)
    recursos = models.TextField(max_length=255)
    criterio_avaliacao = models.TextField(max_length=1000)
    plano_aula = models.TextField(max_length=1000)
    disciplina = models.ForeignKey("curriculo.Disciplina", on_delete=models.PROTECT)
    professor = models.ForeignKey("contas.Professor", on_delete=models.PROTECT)
    coordenador = models.ForeignKey("contas.Coordenador", on_delete=models.PROTECT)
    curso = models.ForeignKey("curriculo.Curso", on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.disciplina}'

    class Meta:
        unique_together = ('curso', 'disciplina', 'turma', 'ano', 'semestre')
        db_table = 'DISCIPLINA_OFERTADA'