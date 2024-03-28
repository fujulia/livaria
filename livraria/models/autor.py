from django.db import models

class Autor (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
