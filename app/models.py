from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
import cloudinary
from cloudinary.models import CloudinaryField


# Modelo para Regiões
class Regiao(models.Model):
    regiao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.regiao

    class Meta:
        ordering = ['-pk']  
        verbose_name_plural = "Regioes"  

class Provincia(models.Model):
    regiao=models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name='provincias')
    provincia = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.provincia

class Distrito(models.Model):
    distrito = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='distritos')

    def __str__(self):
        return self.distrito

class Localidade(models.Model):
    localidade = models.CharField(max_length=100)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, related_name='localidades')

    def __str__(self):
        return self.localidade


def renomear_uploaded_file(instance, filename):
    ext = filename.split('.')[-1]  # Obtém a extensão do arquivo
    filename_slug = slugify(instance.nome_empresa)  # Converte o título para um formato URL-friendly
    new_filename = f"{filename_slug}.{ext}"  # Gera o novo nome do arquivo
    return os.path.join('linkagro_produtor/', new_filename)  # Define o caminho final


class Produtor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='produtor')
    logotipo = CloudinaryField('linkagro_produtor', null=True, blank=True)
    nome_empresa = models.CharField(max_length=100, null=True, blank=True)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    telefone = PhoneNumberField(null=True, blank=True)
    telefone_2 = PhoneNumberField(null=True, blank=True)
    provincia = models.ForeignKey('Provincia', on_delete=models.SET_NULL, null=True, blank=True, related_name='produtor_provincia')
    distrito = models.ForeignKey('Distrito', on_delete=models.SET_NULL, null=True, blank=True, related_name='produtor_distrito')
    localidade = models.ForeignKey('Localidade', on_delete=models.SET_NULL, null=True, blank=True, related_name='produtor_localidade')
    descricao = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    tipo_produtor = models.CharField(
        choices=[
            ('individual', 'Individual'),
            ('entidade', 'Entidade'),
            ('grupo', 'Grupo'),
            ('anual', 'Anual')
        ], 
        max_length=255, 
        default='individual'
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.tipo_produtor == "individual":
            return self.user.get_full_name()
        return self.nome_empresa or "Produtor Sem Nome"

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


def renomear_uploaded_categoria(instance, filename):
    ext = filename.split('.')[-1]  # Obtém a extensão do arquivo
    filename_slug = slugify(instance.nome_categoria)  # Converte o título para um formato URL-friendly
    new_filename = f"{filename_slug}.{ext}"  # Gera o novo nome do arquivo
    return os.path.join('linkagro_categorias/', new_filename)  # Define o caminho final

def renomear_uploaded_categoria_banner(instance, filename):
    ext = filename.split('.')[-1]  # Obtém a extensão do arquivo
    filename_slug = slugify(f'banner-{instance.nome_categoria}')  # Converte o título para um formato URL-friendly
    new_filename = f"{filename_slug}.{ext}"  # Gera o novo nome do arquivo
    return os.path.join('linkagro_categorias_banner/', new_filename)  # Define o caminho final



# Modelo para Categorias de Produtos
class Categoria(models.Model):
    imagem_categoria = CloudinaryField('linkagro_categorias')
    banner_categoria = CloudinaryField('linkagro_categorias/banner')
    nome_categoria = models.CharField(max_length=255, unique=True)
    slug_categoria = models.SlugField(max_length=120, unique=True, blank=True)
    descricao_categoria = models.TextField(blank=True, null=True)
    activo= models.BooleanField(default=True)

    class Meta:
        ordering = ['nome_categoria']  # Ordena as categorias em ordem alfabética
        verbose_name_plural = "Categorias"  # Nome plural no Django Admin


    def save(self, *args, **kwargs):
        if not self.slug_categoria:
            self.slug_categoria = slugify(self.nome_categoria)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_categoria


def renomear_uploaded_produto(instance, filename):
    ext = filename.split('.')[-1]  # Obtém a extensão do arquivo
    filename_slug = slugify(f'banner-{instance.nome_produto}')  # Converte o título para um formato URL-friendly
    new_filename = f"{filename_slug}.{ext}"  # Gera o novo nome do arquivo
    return os.path.join('linkagro_categorias/produtos/', new_filename)  # Define o caminho final


# Modelo para Produtos Agrários
class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    imagem_produto = CloudinaryField('linkagro_categorias/produtos/')
    categoria_produto = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_produtos')
    descricao_produto = models.TextField(blank=True, null=True)
    slug_produto = models.SlugField(max_length=120, unique=True, blank=True)
    activo= models.BooleanField(default=True)
    variedades_activas = models.PositiveIntegerField(default=0)
    proximas_colhetas = models.PositiveIntegerField(default=0)
    numero_variedades = models.PositiveIntegerField(default=0)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-variedades_activas']  # Ordena os produtos por nome
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def save(self, *args, **kwargs):
        if not self.slug_produto:
            self.slug_produto = slugify(self.nome_produto)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_produto}"



EP0CAS_DE_COLHEITA_CHOICES = [
    ('primavera', 'Primavera'),
    ('verao', 'Verão'),
    ('outono', 'Outono'),
    ('inverno', 'Inverno'),
    ('anual', 'Anual'),  
]



class Variedade(models.Model):
    produto_variedade = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='produto_variedades')
    produtor_variedade = models.ForeignKey(Produtor, on_delete=models.CASCADE, related_name='produtor_variedades')
    nome_variedade = models.CharField(max_length=100)
    slug_variedade = models.SlugField(max_length=120, unique=True, blank=True)
    descricao_variedade = models.TextField(blank=True, null=True)
    preco_por_unidade = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_variedade = models.PositiveIntegerField(default=0)
    quantidade_variedade = models.PositiveIntegerField(default=0)
    provincia = models.ForeignKey('Provincia', on_delete=models.SET_NULL, null=True, blank=True, related_name='producao_provincia')
    distrito = models.ForeignKey('Distrito', on_delete=models.SET_NULL, null=True, blank=True, related_name='producao_distrito')
    localidade = models.ForeignKey('Localidade', on_delete=models.SET_NULL, null=True, blank=True, related_name='producao_localidade')
    unidade_variedade = models.CharField(
        max_length=5,
        choices=UNIDADES_CHOICES,
        default='kg',
        help_text="Escolha a unidade de medida (ex: kg, litro, saca)"
    )
    qualidade = models.CharField(
        max_length=20,
        choices=[('Alta', 'Alta'), ('Média', 'Média'), ('Baixa', 'Baixa')],
        default='Média'
    )
    
    # umidade_variedade = models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=2, help_text="Umidade do produto (%)")
    # temperatura_ideal = models.DecimalField(max_digits=5, blank=True, null=True, decimal_places=2, help_text="Temperatura ideal de armazenamento (°C)")
    epoca_de_colheita = models.CharField(
        max_length=10,
        choices=EP0CAS_DE_COLHEITA_CHOICES,
        default='anual',  # Definindo o valor padrão
    )

    data_inicio_colheita=models.DateField()
    data_fim_colheita=models.DateField()
    activo= models.BooleanField(default=True)

    def imagem_variedade(self):
        imagem=None
        for galeria in self.variedade_galerias.all():
            imagem= galeria.imagem_variedade if galeria.default==True else None
            if imagem != None:
                return imagem
        return imagem


    class Meta:
        ordering = ['-data_inicio_colheita', 'nome_variedade']  # Ordena pela data de colheita mais recente e depois pelo nome
        constraints = [
            models.UniqueConstraint(fields=['produto_variedade', 'nome_variedade', 'produtor_variedade']
            , name="unique_variedade_produto")
        ]
        verbose_name = "Variedade"
        verbose_name_plural = "Variedades"

    def save(self, *args, **kwargs):
        if not self.slug_variedade :
            self.slug_variedade  = slugify(f"{self.nome_variedade}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto_variedade} - {self.nome_variedade} @{self.produtor_variedade} "



def renomear_uploaded_variedade(instance, filename):
    ext = filename.split('.')[-1]  # Obtém a extensão do arquivo
    filename_slug = slugify(f'banner-{instance.variedade_galeria.nome_variedade}')  # Converte o título para um formato URL-friendly
    new_filename = f"{filename_slug}.{ext}"  # Gera o novo nome do arquivo
    return os.path.join('linkagro_categorias/produtos/variedade_galeria/', new_filename)  # Define o caminho final


class GaleriaVariedade(models.Model):
    variedade_galeria = models.ForeignKey(Variedade, on_delete=models.CASCADE, related_name='variedade_galerias')
    imagem_variedade = CloudinaryField('linkagro_categorias/produtos/variedade_galeria/')
    default = models.BooleanField(default=False)  # Inicialmente, definimos como False
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-default']  # Garantir que a imagem padrão venha primeiro

    def save(self, *args, **kwargs):
        # Se a imagem for a primeira, definimos como padrão (caso contrário, vamos manter o comportamento).
        if not self.default:
            if not GaleriaVariedade.objects.filter(variedade_galeria=self.variedade_galeria, default=True).exists():
                # Se ainda não houver imagem com `default=True`, esta será a padrão
                self.default = True
        else:
            # Caso o usuário marque esta imagem como padrão, garantimos que as outras não tenham default=True
            GaleriaVariedade.objects.filter(variedade_galeria=self.variedade_galeria).exclude(id=self.id).update(default=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.variedade_galeria.nome_variedade



# Actualizar dados de produtos

# Signal para atualizar os campos após salvar o produto
@receiver(post_save, sender=Variedade)
def atualizar_produto(sender, instance, created, **kwargs):
    produto = instance.produto_variedade

    # Contagem de variedades ativas
    variedades_activas = Variedade.objects.filter(produto_variedade=produto, activo=True,
                                                  data_inicio_colheita__lte=timezone.now(),
                                                  data_fim_colheita__gte=timezone.now()).count()

    # Contagem de próximas colheitas
    proximas_colhetas = Variedade.objects.filter(produto_variedade=produto,
                                                 data_inicio_colheita__gte=timezone.now() + timedelta(days=1)).count()

    # Contagem total de variedades cadastradas
    numero_variedades = Variedade.objects.filter(produto_variedade=produto).count()

    produto.variedades_activas = variedades_activas
    produto.proximas_colhetas = proximas_colhetas
    produto.numero_variedades = numero_variedades
    produto.save()