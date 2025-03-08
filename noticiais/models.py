from django.db import models
from django.db.models import *
import os
from django.utils.text import slugify
# Create your models here.


def renomear_uploaded_file(instance, filename):
    ext = filename.split('.')[-1]  # Obtém a extensão do arquivo
    filename_slug = slugify(instance.titulo)  # Converte o título para um formato URL-friendly
    new_filename = f"{filename_slug}.{ext}"  # Gera o novo nome do arquivo
    return os.path.join('linkagro_noticiais/', new_filename)  # Define o caminho final



class Blog(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=255, help_text="Digite uma breve descrição sobre a notícia...")
    capa= models.ImageField(upload_to= renomear_uploaded_file)
    slug_url = models.SlugField(max_length=255, unique=True, blank=True)
    corpo = models.TextField()
    data = models.DateField(db_index=True, auto_now_add=True)
 

    def __unicode__(self):
        return '%s' % self.titulo
    
    def save(self, *args, **kwargs):
        if not self.slug_url :
            self.slug_url  = slugify(self.slug_url)
        super().save(*args, **kwargs)

    # @permalink
    def get_url_absoluta(self):
        return ('ver_post_blog', None, { 'slug': self.slug_url })
    
    def __str__(self):
        return self.titulo




