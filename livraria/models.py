from django.db import models

class Categoria (models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Editora (models.Model):
    name = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Autor (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Livro (models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length= 32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco= models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name= "livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete = models.PROTECT, related_name="livros"
    )

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"

# Create your models here.
