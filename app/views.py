from django.shortcuts import render, get_object_or_404
from .models import *
from anuncios.models import *
from noticiais.models import *
from django.db.models import Q


# Create your views here.
class linkagro:

    def index(request):
        banner= Banner.objects.all().exclude(activo=False)
        categoria= Categoria.objects.all().exclude(activo=False)
        parceiros= Parceiros.objects.all()
        noticia= Blog.objects.all()

        return render(request, "index.html", context={
            "banner": banner,
            "categoria": categoria,
            "parceiros": parceiros,
            "noticias": noticia,
            "activo_home":"active",
        })

    
    def pagina_de_informe_de_locais_de_producao(request):
        return render(request, "linkagro/informar_regiao_prov_distrito.html")
    

    def pagina_de_produtos_da_categoria(request, categ):
        categoria=get_object_or_404(Categoria, slug_categoria=categ)
        produto=Produto.objects.filter(categoria_produto=categoria, activo=True, variedades_activas__gt=0)
        categorias= Categoria.objects.exclude(Q(pk=categoria.pk) | Q(activo=False))
        banner= Banner.objects.all().exclude(activo=False)
        return render(request, "linkagro/produtos_da_categoria.html", context={
            "categoria": categoria,
            "produtos": produto,
            "categorias": categorias,
            "banner": banner,
        })
    

    def pagina_de_variedades_de_produto(request, produto):
        produto=get_object_or_404(Produto, slug_produto=produto)
        categoria=Categoria.objects.exclude(Q(pk=produto.categoria_produto.pk) | Q(activo=False))
        produtos=Produto.objects.exclude(pk=produto.pk).filter(activo=True, variedades_activas__gt=0,categoria_produto=produto.categoria_produto)

        return render(request, "linkagro/variedades_de_produto.html", context={
            "produto": produto,
            "produtos": produtos,
            "categorias": categoria,
        })
    

    def panina_de_detalhes_da_variedade(request, varied):
        variedade=get_object_or_404(Variedade, slug_variedade=varied)
        
        return render(request, "linkagro/detalhes_da_variedade.html", context={
            "variedade": variedade,
        })


    def panina_de_pesquisa(request):
        # variedade=get_object_or_404(Variedade, slug_pesquisa=q)
        
        return render(request, "linkagro/pagina_pesquisa.html", context={
            "variedade": "",
        })


    def panina_de_anunciantes(request):
        # variedade=get_object_or_404(Variedade, slug_pesquisa=q)
        
        return render(request, "linkagro/pagina_pesquisa.html", context={
            "variedade": "",
        })


    def panina_como_funciona(request):
        # variedade=get_object_or_404(Variedade, slug_pesquisa=q)
        
        return render(request, "linkagro/pagina_pesquisa.html", context={
            "variedade": "",
        })
    

    def panina_de_termos_condicoes(request):
        # variedade=get_object_or_404(Variedade, slug_pesquisa=q)
        
        return render(request, "linkagro/pagina_pesquisa.html", context={
            "variedade": "",
        })
    

    def panina_de_politica_privacidade(request):
        # variedade=get_object_or_404(Variedade, slug_pesquisa=q)
        
        return render(request, "linkagro/pagina_pesquisa.html", context={
            "variedade": "",
        })
