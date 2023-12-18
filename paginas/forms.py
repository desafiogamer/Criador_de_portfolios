from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PortfolioOne, PortfolioTwo, Portfolio3

class PortfolioForms(forms.ModelForm):
    class Meta:
        model = PortfolioOne
        fields = ["logo","desenvolvedor","resumo_sobre","linkdin","github","instagran","curriculo","backgroundInicio","backgroundColorInicio",
                  "fotoSobre","sobreVoce","backgroundColorSobre","backgroundSobre",
                  "tituloOne","imagemProjetoOne","DescricaoProjetoOne","LinkProjetoOne","tituloTwo","imagemProjetoTwo","DescricaoProjetoTwo","LinkProjetoTwo","tituloThre","imagemProjetoThre","DescricaoProjetoThre","LinkProjetoThre","tituloFour","imagemProjetoFour","DescricaoProjetoFour","LinkProjetoFour","backgroundProjetos","backgroundColorProjetos",
                  "gmail","linkGmail","numero","linkWhatsap","backgroundContact","backgroundColorContact",
                  "linguagensProgramação1","linguagensProgramação2","linguagensProgramação3","linguagensProgramação4","linguagensProgramação5","linguagensProgramação6","linguagensProgramação7","linguagensProgramação8","linguagensProgramação9","linguagensProgramação10","linguagensProgramação11","linguagensProgramação12",
                  "nivelExperiencia1","nivelExperiencia2","nivelExperiencia3","nivelExperiencia4","nivelExperiencia5","nivelExperiencia6","nivelExperiencia7","nivelExperiencia8","nivelExperiencia9","nivelExperiencia10","nivelExperiencia11","nivelExperiencia12","alinharTexto",
                  "img1","img2","img3","img4","img5","img6","img7","img8","img9","img10","img11","img12","backgroundHabilidades","backgroundColorHabilidades","corPrimaria","corSecundaria"]
        

class PortfolioFormsTwo(forms.ModelForm):
    class Meta:
        model = PortfolioTwo
        fields = ["nome","imagemPerfil","desenvolvedor","linkdin","github","instagran","facebook",
                  "SobreVoce","nascimento","telefone","cidade","idade","grau","email",
                  "linguagen1","porcento1","linguagen2","porcento2","linguagen3","porcento3","linguagen4","porcento4","linguagen5","porcento5","linguagen6","porcento6",
                  "resumoSobre","city","curso1","nomeInstituição1","periodo1","sobreCurso1","curso2","nomeInstituição2","periodo2","sobreCurso1","função1","periodoSeviço1","local1","cargo1","função2","periodoSeviço2","local2","cargo2",
                  "SobreProjetos","tituloProjeto1","sobreProjeto1","ProjetoLink1","projetoImagem1","tituloProjeto2","sobreProjeto2","ProjetoLink2","projetoImagem2","tituloProjeto3","sobreProjeto3","ProjetoLink3","projetoImagem3","tituloProjeto4","sobreProjeto4","ProjetoLink4","projetoImagem4","tituloProjeto5","sobreProjeto5","ProjetoLink5","projetoImagem5","tituloProjeto6","sobreProjeto6","ProjetoLink6","projetoImagem6",
                  "SobreContato","localizacaoVoce","imagemSobre","SobreHabilidades","imagemDeFundo","CorDeFundo", "CorPrimaria", "CorSecundaria","remover1","remover2","remover3"]
        


class PortfolioFormsThre(forms.ModelForm):
    class Meta:
        model = Portfolio3
        fields =  ["nome","ImagemDePerfil","desenvolvedor","linkdin","github","instagran","telefone","email","logo",
                   "cidade","SobreVoce","curriculo","SobreDesigner","SobreSocial","SobreCreativo",
                   "linguagen1","porcento1","linguagen2","porcento2","linguagen3","porcento3","linguagen4","porcento4","linguagen5","porcento5","linguagen6","porcento6","linguagen7","porcento7","linguagen8","porcento8","linguagen9","porcento9","linguagen10","porcento10",
                   "titulo1","imagemProjeto1","DescricaoProjeto1","LinkProjeto1","titulo2","imagemProjeto2","DescricaoProjeto2","LinkProjeto2","titulo3","imagemProjeto3","DescricaoProjeto3","LinkProjeto3","titulo4","imagemProjeto4","DescricaoProjeto4","LinkProjeto4",
                   "localizacaoVoce","CorPrimaria","CorSecundaria","CorDoFundo","ImagemSobreVoce"]