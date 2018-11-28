from django.contrib import admin

from .models import Curso, Disciplina, DisciplinaOfertada
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "tipo_curso", "tipo_graduacao", "matutino", "vespertino", "noturno")
    list_filter = ("tipo_curso", "tipo_graduacao", "vespertino", "noturno")
    search_fields = ("nome", "sigla")

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "identificador", "status", "carga_horaria")

class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ("disciplina", "curso", "ano", "semestre", "turma")
    list_filter = ("curso", "ano", "semestre")
    


admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(DisciplinaOfertada, DisciplinaOfertadaAdmin)