from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from app.models import *
import cloudinary
from cloudinary.models import CloudinaryField

# Modelo para Anúncios
class Banner(models.Model):
    TIPO_ANUNCIO = [
        ('imagem', 'Imagem'),
        ('video', 'Vídeo')
    ]
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    # link_banner=models.URLField(blank=True, null=True, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPO_ANUNCIO, default="Imagem")
    arquivo = CloudinaryField('linkagro_banners/')
    activo=models.BooleanField(default=False)
    mostrar_texto=models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo



class Parceiros(models.Model):
    titulo = models.CharField(max_length=255)
    arquivo = CloudinaryField('linkagro_parceiros/')
    mostrar_texto=models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# Modelo para Usuários
class Armazenista(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='armazenista')
    empresa=models.CharField(blank=True, null=True,max_length=255)
    slogan=models.CharField( blank=True, null=True, max_length=255)
    foto_perfil = models.ImageField(upload_to='linkagro_armazenista/',null=True, blank=True)
    telefone = models.CharField(max_length=20)
    telefone_2 = models.CharField(max_length=20)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, blank=True, related_name='armazenista_provincia')
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null=True, blank=True, related_name='armazenista_distrito')
    localidade = models.ForeignKey(Localidade, on_delete=models.SET_NULL, null=True, blank=True, related_name='armazenista_localidade')
    descricao = models.TextField(blank=True, null=True)
    activo=models.BooleanField(default=True)
    slug=models.CharField(max_length=255, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_= f'@{self.user.first_name}{self.user.last_name}' if self.empresa else self.empresa
            self.slug = slugify(slug_)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']  
        verbose_name_plural = "Armazenista"  


# Choices para unidades de medida
UNIDADES_CHOICES = [
    ('kg', 'Quilograma (kg)'),
    ('g', 'Grama (g)'),
    ('t', 'Tonelada (t)'),
    ('l', 'Litro (l)'),
    ('ml', 'Mililitro (ml)'),
    ('cx', 'Caixa (cx)'),
    ('sc', 'Saca (sc)'),
    ('un', 'Unidade (un)'),
]


class Armazem(models.Model):
    armazenar_produto= models.ManyToManyField(Produto, related_name="produtos_armazenados")
    armazenista = models.ForeignKey(Armazenista, on_delete=models.CASCADE, related_name='armazem')
    nome_armazem = models.CharField(max_length=100)
    slug=models.CharField(max_length=255, unique=True)
    numero_local_armazem = models.CharField(max_length=255)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, blank=True, related_name='armazem_provincia')
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null=True, blank=True, related_name='armazem_distrito')
    activo=models.BooleanField(default=True)
    localidade = models.ForeignKey(Localidade, on_delete=models.SET_NULL, null=True, blank=True, related_name='armazem_localidade')
    unidade_armazenamento=models.CharField(
        max_length=5,
        choices=UNIDADES_CHOICES,
        default='kg',
        help_text="Escolha a unidade de medida (ex: kg, litro, saca)"
    )
    capacidade_maxima = models.PositiveIntegerField(help_text="Capacidade máxima de armazenagem (em unidades)")
    lotacao= models.PositiveIntegerField(help_text="Capacidade máxima de armazenagem (em unidades)")
    condicoes_armazenagem = models.TextField(help_text="Condições específicas para armazenagem de produtos")
    dimensao = models.CharField(max_length=100, help_text="Dimensão do armazém, por exemplo, 10x20m")
    data_criacao = models.DateField(auto_now_add=True)
    disponivel = models.BooleanField(default=True, help_text="Se o armazém está disponível para receber novos produtos")
    
    def __str__(self):
        return self.nome_armazem

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome_armazem)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['disponivel', '-pk']  
        verbose_name_plural = "Armazens"  



class GaleriaArmazem(models.Model):
    armazem_galeria= models.ForeignKey(Armazem, on_delete=models.CASCADE, related_name='armazem_galeria')
    imagem_armazem = models.ImageField(upload_to='linkagro_aramzem_galeria/')
    default=models.BooleanField(default=True)
    activo=models.BooleanField(default=True)

    def __str__(self):
        return self.imagem_armazem.url


class AvaliarArmazem(models.Model):
    avaliar_armazem=models.DecimalField(max_digits=3, blank=True, null=True, decimal_places=2, help_text="De 1-5")
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliacaoes')

    def __str__(self): 
        return self.avaliar_armazem