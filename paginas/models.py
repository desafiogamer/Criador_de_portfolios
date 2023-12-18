from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.

class PortfolioOne(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    logo = models.CharField(max_length=10,null=True, blank=True)
    developer = {
        ("Developer Fullstack","Developer Fullstack"),
        ("Developer BackEnd","Developer BackEnd"),
        ("Developer FrontEnd","Developer FrontEnd"),
    }

    desenvolvedor = models.CharField(max_length=20, choices=developer, default="Developer Fullstack", null=True, blank=True)
    resumo_sobre = models.TextField(max_length=200, null=True, blank=True)
    linkdin = models.CharField(max_length=100, null=True, blank=True, default='#')
    github = models.CharField(max_length=100,null=True, blank=True, default='#')
    instagran = models.CharField(max_length=100,null=True, blank=True, default='#')
    curriculo = models.CharField(max_length=100,null=True, blank=True, default='#')
    backgroundInicio = models.ImageField(upload_to='midia', null=True, default='fundo-hacker.jpg', blank=True)
    backgroundColorInicio = ColorField(null=True, blank=True)

    texto = {
        ("left","Esquerda"),
        ("center","Meio"),
        ("right","Direita"),
    }

    alinharTexto = models.CharField(max_length=20, choices=texto, null=True, blank=True, default="left")
    
    #Sobre
    fotoSobre = models.ImageField(upload_to='midia', null=True, default='fundo-Projetos-hacker.png', blank=True)
    sobreVoce = models.TextField(max_length=2000,null=True, blank=True)
    backgroundSobre = models.ImageField(upload_to='midia', null=True, default='fundo-about.jpg', blank=True)
    backgroundColorSobre = ColorField(null=True, blank=True)

    #projetos
    tituloOne = models.CharField(max_length=10, null=True, blank=True,default='Em breve')
    imagemProjetoOne = models.ImageField(upload_to='midia', null=True, default='fundo-Projetos-hacker.png', blank=True)
    DescricaoProjetoOne = models.TextField(max_length=130,null=True, blank=True)
    LinkProjetoOne = models.CharField(max_length=200,null=True, blank=True, default='#')

    tituloTwo = models.CharField(max_length=10, null=True, blank=True,default='Em breve')
    imagemProjetoTwo = models.ImageField(upload_to='midia', null=True, default='fundo-Projetos-hacker.png', blank=True)
    DescricaoProjetoTwo = models.TextField(max_length=130,null=True, blank=True)
    LinkProjetoTwo = models.CharField(max_length=200,null=True, blank=True, default='#')

    tituloThre = models.CharField(max_length=10, null=True, blank=True,default='Em breve')
    imagemProjetoThre = models.ImageField(upload_to='midia', null=True, default='fundo-Projetos-hacker.png', blank=True)
    DescricaoProjetoThre = models.TextField(max_length=130,null=True, blank=True)
    LinkProjetoThre = models.CharField(max_length=200,null=True, blank=True, default='#')

    tituloFour = models.CharField(max_length=10, null=True, blank=True,default='Em breve')
    imagemProjetoFour = models.ImageField(upload_to='midia', null=True, default='fundo-Projetos-hacker.png', blank=True)
    DescricaoProjetoFour = models.TextField(max_length=130,null=True, blank=True)
    LinkProjetoFour = models.CharField(max_length=200,null=True, blank=True, default='#')

    backgroundProjetos = models.ImageField(upload_to='midia', null=True, default='fundo-port.jpg', blank=True)
    backgroundColorProjetos = ColorField(null=True, blank=True)

    nivel = {
        ("Experiente","Experiente"),
        ("Intermediario","Intermediario"),
        ("Básico","Básico"),
    }

    #habilidades
    linguagensProgramação1 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia1 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img1 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação2 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia2 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img2 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação3 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia3 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img3 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação4 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia4 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img4 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação5 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia5 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img5 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação6 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia6 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img6 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação7 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia7 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img7 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação8 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia8 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img8 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação9 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia9 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img9 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação10 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia10 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img10 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação11 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia11 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img11 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)
    linguagensProgramação12 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    nivelExperiencia12 = models.CharField(max_length=20, choices=nivel, default='', null=True, blank=True)
    img12 = models.ImageField(upload_to='midia', null=True, default='cpu.png', blank=True)

    backgroundHabilidades = models.ImageField(upload_to='midia', default='red.png', null=True, blank=True)
    backgroundColorHabilidades = ColorField(null=True, blank=True, default='#323946')

    #Contato
    gmail = models.CharField(max_length=100,null=True, blank=True)
    linkGmail = models.CharField(max_length=100, null=True, blank=True, default='#')
    numero = models.CharField(max_length=20,null=True, blank=True)
    linkWhatsap = models.CharField(max_length=100, null=True, blank=True, default='#') 

    backgroundContact = models.ImageField(upload_to='midia',default='red.png', null=True, blank=True)
    backgroundColorContact = ColorField(null=True, blank=True, default='#323946')

    corPrimaria = ColorField(default="#ededed")
    corSecundaria = ColorField(default="#00ff08")

    def __str__(self):
        return f'{self.usuario.username}-PortfolioTemplate1'

    
class PortfolioTwo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=20, null=True, blank=True)
    imagemPerfil = models.ImageField(null=True, blank=True, default='fundo-Projetos-hacker.png', upload_to='midia')
    developer = {
        ("Fullstack","Fullstack"),
        ("BackEnd","BackEnd"),
        ("FrontEnd","FrontEnd"),
    }
    desenvolvedor = models.CharField(max_length=20, choices=developer, default="Fullstack", null=True, blank=True)
    linkdin = models.CharField(max_length=100, null=True, blank=True, default='#')
    github = models.CharField(max_length=100,null=True, blank=True, default='#')
    instagran = models.CharField(max_length=100,null=True, blank=True, default='#')
    facebook = models.CharField(max_length=100,null=True, blank=True, default='#')
    gra ={
        ("Senior","Senior"),
        ("Pleno","Pleno"),
        ("Junior","Junior"),
    }
    imagemDeFundo = models.ImageField(null=True, blank=True, default='pexels-fundo.jpg', upload_to='midia')
    
    #sobre
    SobreVoce = models.TextField(max_length=2000, null=True, blank=True)
    nascimento = models.CharField(max_length=20, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    idade = models.CharField(max_length=10, null=True, blank=True)
    grau = models.CharField(max_length=20, choices=gra, default="Junior", null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)
    imagemSobre = models.ImageField(null=True, blank=True, default='fundo-hacker.jpg', upload_to='midia')
    CorDeFundo = ColorField(null=True, blank=True, default="#191D26")

    #skills
    SobreHabilidades = models.TextField(max_length=1000, null=True, blank=True)

    linguagen1 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento1 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen2 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento2 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen3 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento3 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen4 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento4 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen5 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento5 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen6 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento6 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    #resumo
    deli = {
        ("block","Visivél"),
        ("none","Remover"),
    }

    remover1 = models.CharField(max_length=20, choices=deli, default="Visivél", null=True, blank=True)
    remover2 = models.CharField(max_length=20, choices=deli, default="Visivél", null=True, blank=True)
    remover3 = models.CharField(max_length=20, choices=deli, default="Visivél", null=True, blank=True)

    resumoSobre = models.TextField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    curso1 = models.CharField(max_length=200, null=True, blank=True)
    nomeInstituição1 = models.CharField(max_length=300, null=True, blank=True)
    periodo1 = models.CharField(max_length=20, null=True, blank=True)
    sobreCurso1 = models.TextField(max_length=1000, null=True, blank=True)

    curso2 = models.CharField(max_length=200, null=True, blank=True)
    nomeInstituição2 = models.CharField(max_length=300, null=True, blank=True)
    periodo2 = models.CharField(max_length=20, null=True, blank=True)
    sobreCurso1 = models.TextField(max_length=1000, null=True, blank=True)

    função1 = models.CharField(max_length=100, null=True, blank=True)
    periodoSeviço1 = models.CharField(max_length=20, null=True, blank=True)
    local1 = models.CharField(max_length=100, null=True, blank=True)
    cargo1 = models.TextField(max_length=1000, null=True, blank=True)

    função2 = models.CharField(max_length=100, null=True, blank=True)
    periodoSeviço2 = models.CharField(max_length=20, null=True, blank=True)
    local2 = models.CharField(max_length=100, null=True, blank=True)
    cargo2 = models.TextField(max_length=1000, null=True, blank=True)

    #projetos
    SobreProjetos = models.TextField(max_length=100, null=True, blank=True)

    tituloProjeto1 = models.CharField(max_length=100, null=True, blank=True)
    sobreProjeto1 = models.TextField(max_length=2000, null=True, blank=True, default='Em breve')
    ProjetoLink1 = models.CharField(max_length=100, null=True, blank=True, default='#')
    projetoImagem1 = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')

    tituloProjeto2 = models.CharField(max_length=100, null=True, blank=True)
    sobreProjeto2 = models.TextField(max_length=2000, null=True, blank=True, default='Em breve')
    ProjetoLink2 = models.CharField(max_length=100, null=True, blank=True, default='#')
    projetoImagem2 = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')

    tituloProjeto3 = models.CharField(max_length=100, null=True, blank=True)
    sobreProjeto3 = models.TextField(max_length=2000, null=True, blank=True, default='Em breve')
    ProjetoLink3 = models.CharField(max_length=100, null=True, blank=True, default='#')
    projetoImagem3 = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')

    tituloProjeto4 = models.CharField(max_length=100, null=True, blank=True)
    sobreProjeto4 = models.TextField(max_length=2000, null=True, blank=True, default='Em breve')
    ProjetoLink4 = models.CharField(max_length=100, null=True, blank=True, default='#')
    projetoImagem4 = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')

    tituloProjeto5 = models.CharField(max_length=100, null=True, blank=True)
    sobreProjeto5 = models.TextField(max_length=2000, null=True, blank=True, default='Em breve')
    ProjetoLink5 = models.CharField(max_length=100, null=True, blank=True, default='#')
    projetoImagem5 = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')

    tituloProjeto6 = models.CharField(max_length=100, null=True, blank=True)
    sobreProjeto6 = models.TextField(max_length=2000, null=True, blank=True, default='Em breve')
    ProjetoLink6 = models.CharField(max_length=100, null=True, blank=True, default='#')
    projetoImagem6 = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')

    #contato
    SobreContato = models.TextField(max_length=2000, null=True, blank=True)

    localizacaoVoce = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    

    CorPrimaria = ColorField(null=True, blank=True, default="#FFFFFF")
    CorSecundaria = ColorField(null=True, blank=True, default="#02FFD0")

    def __str__(self):
        return f'{self.usuario.username}-PortfolioTemplate2'


class Portfolio3(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=20, null=True, blank=True)
    ImagemDePerfil = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')
    developer = {
        ("Fullstack","Fullstack"),
        ("BackEnd","BackEnd"),
        ("FrontEnd","FrontEnd"),
    }

    desenvolvedor = models.CharField(max_length=20, choices=developer, default="Fullstack", null=True, blank=True)
    linkdin = models.CharField(max_length=100, null=True, blank=True, default='#')
    github = models.CharField(max_length=100,null=True, blank=True, default='#')
    instagran = models.CharField(max_length=100,null=True, blank=True, default='#')
    telefone = models.CharField(max_length=100,null=True, blank=True, default='#')
    email = models.CharField(max_length=100,null=True, blank=True, default='#')
    logo = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')

    #sobre
    cidade = models.CharField(max_length=100,null=True, blank=True, default='#')
    SobreVoce = models.TextField(max_length=2000, null=True, blank=True)
    curriculo = models.CharField(max_length=100,null=True, blank=True, default='#')
    ImagemSobreVoce = models.ImageField(null=True, blank=True, default='fundo_preto.png', upload_to='midia')
    SobreDesigner = models.TextField(max_length=2000, null=True, blank=True)
    SobreSocial = models.TextField(max_length=2000, null=True, blank=True)
    SobreCreativo = models.TextField(max_length=2000, null=True, blank=True)
    linguagen1 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento1 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen2 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento2 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen3 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento3 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen4 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento4 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen5 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento5 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen6 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento6 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen7 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento7 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen8 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento8 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen9 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento9 = models.CharField(max_length=10, null=True, blank=True, default='0') 
    
    linguagen10 = models.CharField(max_length=100, null=True, blank=True, default='Em breve')
    porcento10 = models.CharField(max_length=10, null=True, blank=True, default='0')


    #projetos
    titulo1 = models.CharField(max_length=10, null=True, blank=True,default='Em breve')
    imagemProjeto1 = models.ImageField(upload_to='midia', null=True, default='fundo_preto.png', blank=True)
    DescricaoProjeto1 = models.TextField(max_length=130,null=True, blank=True)
    LinkProjeto1 = models.CharField(max_length=200,null=True, blank=True, default='#')

    titulo2 = models.CharField(max_length=10, null=True, blank=True,default='Em breve')
    imagemProjeto2 = models.ImageField(upload_to='midia', null=True, default='fundo_preto.png', blank=True)
    DescricaoProjeto2 = models.TextField(max_length=130,null=True, blank=True)
    LinkProjeto2 = models.CharField(max_length=200,null=True, blank=True, default='#')

    titulo3 = models.CharField(max_length=10, null=True, blank=True,default='Em breve')
    imagemProjeto3 = models.ImageField(upload_to='midia', null=True, default='fundo_preto.png', blank=True)
    DescricaoProjeto3 = models.TextField(max_length=130,null=True, blank=True)
    LinkProjeto3 = models.CharField(max_length=200,null=True, blank=True, default='#')

    titulo4 = models.CharField(max_length=10, null=True, blank=True,default='Em breve')
    imagemProjeto4 = models.ImageField(upload_to='midia', null=True, default='fundo_preto.png', blank=True)
    DescricaoProjeto4 = models.TextField(max_length=130,null=True, blank=True)
    LinkProjeto4 = models.CharField(max_length=200,null=True, blank=True, default='#')

    #contato
    localizacaoVoce = models.CharField(max_length=100, null=True, blank=True)

    CorPrimaria = ColorField(null=True, blank=True, default="#FFFFFF")
    CorSecundaria = ColorField(null=True, blank=True, default="#02FFD0")
    CorDoFundo = ColorField(null=True, blank=True, default="#02FFD0")

    def __str__(self):
        return f'{self.usuario.username}-PortfolioTemplate3'
 


    
    