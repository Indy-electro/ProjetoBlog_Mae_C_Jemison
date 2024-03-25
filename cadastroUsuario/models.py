from django.db import models

class Cadastro(models.Model):
    Sexo_Choice = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outros'),
    )

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=Sexo_Choice)
    usuario = models.CharField(max_length=15)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data_nascimento = models.DateField(help_text='aaaa/dd/mm')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.usuario} [{self.email}]'

    class Meta:
        verbose_name = 'Formulário de Cadastro'
        verbose_name_plural = 'Formulários de Cadastros'
        ordering = ['-data_cadastro']


