from django.db import models

class Atividade(models.Model):
    titulo = models.TextField(max_length=255, unique=True)
    descricao = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255)
    extras = models.TextField(max_length=255)
    professor = models.ForeignKey("contas.Professor", on_delete=models.PROTECT)

    class Meta():
        db_table="Atividade"

class AtividadeVinculada(models.Model):
    status = models.IntegerField()
    rotulo = models.TextField(max_length=255)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    professor = models.ForeignKey("contas.Professor", on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey("curriculo.DisciplinaOfertada", on_delete=models.PROTECT)
    
    class Meta():
        db_table="AtividadeVinculada"

class EntregaAtividade(models.Model):
    titulo = models.TextField(max_length=100)
    resposta = models.TextField(max_length=255)
    dt_entrega = models.DateField()
    status = models.IntegerField()
    nota = models.IntegerField()
    dt_avaliacao = models.DateField()
    obs = models.TextField(max_length=255)
    aluno = models.ForeignKey("contas.Aluno", on_delete=models.PROTECT)
    atividade_vinculada = models.ForeignKey("curriculo.AtividadeVinculada", on_delete=models.PROTECT)
    professor = models.ForeignKey("contas.Professor", on_delete=models.PROTECT)
    
    class Meta():
        db_table="EntregaAtividade"

class Mensagem(models.Model):
    assunto = models.TextField(max_length=255)
    referencia = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    status = models.IntegerField()
    dt_envio = models.DateField()
    dr_resposta = models.DateField()
    resposta = models.TextField(max_length=1000)
    aluno = models.ForeignKey("contas.Aluno", on_delete=models.PROTECT)
    professor = models.ForeignKey("contas.Professor", on_delete=models.PROTECT)
    
    class Meta():
        db_table="Mensagem"