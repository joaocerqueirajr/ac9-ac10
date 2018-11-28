from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Professor, Usuario, Coordenador, Aluno

class UsuarioCriacaoForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('username',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password('123@mudar')
        if commit:
            user.save()
        return user


class UsuarioAlteracaoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'data_expiracao')

class ProfessorInline(admin.StackedInline):
    model = Professor
    max_num = 1

class ProfessorAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (ProfessorInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )
    add_fieldsets = (
        (None, { 'fields': ('username',) } ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'P'
        super(ProfessorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(ProfessorAdmin, self).get_queryset(request)
        return resultado.filter(tipo='P')

class ProfessorUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'professor'
        verbose_name_plural = 'professores'

        
class CoordenadorInline(admin.StackedInline):
    model = Coordenador
    max_num = 1
    
class CoordenadorAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (CoordenadorInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )
    add_fieldsets = (
        (None, { 'fields': ('username',) } ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'C'
        super(CoordenadorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(CoordenadorAdmin, self).get_queryset(request)
        return resultado.filter(tipo='C')


class CoordenadorUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'coordenador'
        verbose_name_plural = 'coordenadores'

        
class AlunoInline(admin.StackedInline):
    model = Aluno
    max_num = 1
    
class AlunoAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (AlunoInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )
    add_fieldsets = (
        (None, { 'fields': ('username',) } ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'A'
        super(AlunoAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(AlunoAdmin, self).get_queryset(request)
        return resultado.filter(tipo='A')


class AlunoUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

admin.site.register(ProfessorUsuario, ProfessorAdmin)
admin.site.register(CoordenadorUsuario, CoordenadorAdmin)
admin.site.register(AlunoUsuario, AlunoAdmin)