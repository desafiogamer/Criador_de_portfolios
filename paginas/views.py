from typing import Any
from django.shortcuts import render, get_object_or_404
from .models import PortfolioOne, PortfolioTwo, Portfolio3
from .forms import PortfolioForms,PortfolioFormsTwo, PortfolioFormsThre
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponse

###### paginas #####

def erro(request):
    return render(request, 'erros/erro.html')

def index(request):
    return render(request, 'index.html')

def VerPortfolio1(request):
    return render(request, 'Ver-Portfolios/VerPort1.html')

def VerPortfolio2(request):
    return render(request, 'Ver-Portfolios/VerPort2.html')

def VerPortfolio3(request):
    return render(request, 'Ver-Portfolios/VerPort3.html')



####### create #######

class Portfolio_one(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = PortfolioForms
    template_name = 'template_portifolio/portfolio1.html'
    success_url = reverse_lazy ('listarTodosPortfolios')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        port = PortfolioOne.objects.filter(usuario=self.request.user)
        if port.exists():
            return redirect('erro')
        else:
            url = super().form_valid(form)
            return url
    

class Portfolio_Two(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = PortfolioFormsTwo
    template_name = 'template_portifolio/portfolio2.html'
    success_url = reverse_lazy ('listarTodosPortfolios')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        port = PortfolioTwo.objects.filter(usuario=self.request.user)
        if port.exists():
            return redirect('erro')
        else:
            url = super().form_valid(form)
            return url


class Portfolio_Thre(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = PortfolioFormsThre
    template_name = 'template_portifolio/portfolio3.html'
    success_url = reverse_lazy ('listarTodosPortfolios')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        port = Portfolio3.objects.filter(usuario=self.request.user)
        if port.exists():
            return redirect('erro')
        else:
            url = super().form_valid(form)
            return url



##### listar view #########

def detail_page(request, id):
    obj= get_object_or_404(PortfolioOne, pk=id)
    return render(request, 'template_portifolio/verPortfolio1.html', {'obj':obj})


def detail_page2(request, id):
    obj= get_object_or_404(PortfolioTwo, pk=id)
    return render(request, 'template_portifolio/verPortfolioTwo.html', {'obj':obj})

def detail_page3(request, id):
    obj= get_object_or_404(Portfolio3, pk=id)
    return render(request, 'template_portifolio/verPortfolioThre.html', {'obj':obj})


class ListarTodosPortfolios(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'Meus_Portfolios/listaDosPortfolios.html'
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        context = super(ListarTodosPortfolios, self).get_context_data(**kwargs)
        voted = self.object_list = PortfolioOne.objects.filter(usuario=self.request.user)
        voted2 = self.object_list = PortfolioTwo.objects.filter(usuario=self.request.user)
        voted3 = self.object_list = Portfolio3.objects.filter(usuario=self.request.user)
        context['Portfolio_one'] = voted
        context['Portfolio_Two'] = voted2
        context['Portfolio_Thre'] = voted3
        return context


###### Deletar views #########
class PortfolioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = PortfolioOne
    template_name = 'delete-Portfolios/deletar-Portfolios.html'
    success_url = reverse_lazy('listarTodosPortfolios')

    def get_object(self, queryset=None):
        self.object = PortfolioOne.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
    
class DeletePortfolio2(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = PortfolioTwo
    template_name = 'delete-Portfolios/deletar-Portfolios.html'
    success_url = reverse_lazy('listarTodosPortfolios')

    def get_object(self, queryset=None):
        self.object = PortfolioTwo.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
class DeletePortfolio3(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Portfolio3
    template_name = 'delete-Portfolios/deletar-Portfolios.html'
    success_url = reverse_lazy('listarTodosPortfolios')

    def get_object(self, queryset=None):
        self.object = Portfolio3.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    


####### Update views #############
    
class PortfolioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model =  PortfolioOne
    fields = ["logo","desenvolvedor","resumo_sobre","linkdin","github","instagran","curriculo","backgroundInicio","backgroundColorInicio",
                  "fotoSobre","sobreVoce","backgroundColorSobre","backgroundSobre",
                  "tituloOne","imagemProjetoOne","DescricaoProjetoOne","LinkProjetoOne","tituloTwo","imagemProjetoTwo","DescricaoProjetoTwo","LinkProjetoTwo","tituloThre","imagemProjetoThre","DescricaoProjetoThre","LinkProjetoThre","tituloFour","imagemProjetoFour","DescricaoProjetoFour","LinkProjetoFour","backgroundProjetos","backgroundColorProjetos",
                  "gmail","linkGmail","numero","linkWhatsap","backgroundContact","backgroundColorContact",
                  "linguagensProgramação1","linguagensProgramação2","linguagensProgramação3","linguagensProgramação4","linguagensProgramação5","linguagensProgramação6","linguagensProgramação7","linguagensProgramação8","linguagensProgramação9","linguagensProgramação10","linguagensProgramação11","linguagensProgramação12",
                  "nivelExperiencia1","nivelExperiencia2","nivelExperiencia3","nivelExperiencia4","nivelExperiencia5","nivelExperiencia6","nivelExperiencia7","nivelExperiencia8","nivelExperiencia9","nivelExperiencia10","nivelExperiencia11","nivelExperiencia12",
                  "img1","img2","img3","img4","img5","img6","img7","img8","img9","img10","img11","img12","backgroundHabilidades","backgroundColorHabilidades","corPrimaria","corSecundaria","alinharTexto"]
        
    
    template_name = 'template_portifolio/portfolio1.html'
    success_url = reverse_lazy('listarTodosPortfolios')

    def get_object(self, queryset=None):
        self.object = PortfolioOne.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    

class PortfolioUpdate2(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model =  PortfolioTwo
    fields = ["nome","imagemPerfil","desenvolvedor","linkdin","github","instagran","facebook",
                  "SobreVoce","nascimento","telefone","cidade","idade","grau","email",
                  "linguagen1","porcento1","linguagen2","porcento2","linguagen3","porcento3","linguagen4","porcento4","linguagen5","porcento5","linguagen6","porcento6",
                  "resumoSobre","city","curso1","nomeInstituição1","periodo1","sobreCurso1","curso2","nomeInstituição2","periodo2","sobreCurso1","função1","periodoSeviço1","local1","cargo1","função2","periodoSeviço2","local2","cargo2",
                  "SobreProjetos","tituloProjeto1","sobreProjeto1","ProjetoLink1","projetoImagem1","tituloProjeto2","sobreProjeto2","ProjetoLink2","projetoImagem2","tituloProjeto3","sobreProjeto3","ProjetoLink3","projetoImagem3","tituloProjeto4","sobreProjeto4","ProjetoLink4","projetoImagem4","tituloProjeto5","sobreProjeto5","ProjetoLink5","projetoImagem5","tituloProjeto6","sobreProjeto6","ProjetoLink6","projetoImagem6",
                  "SobreContato","localizacaoVoce","imagemSobre","SobreHabilidades","imagemDeFundo","CorDeFundo", "CorPrimaria", "CorSecundaria","remover1","remover2","remover3"]
        
    
    template_name = 'template_portifolio/portfolio2.html'
    success_url = reverse_lazy('listarTodosPortfolios')

    def get_object(self, queryset=None):
        self.object = PortfolioTwo.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    

class PortfolioUpdate3(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model =  Portfolio3
    fields = ["nome","ImagemDePerfil","desenvolvedor","linkdin","github","instagran","telefone","email","logo",
                   "cidade","SobreVoce","curriculo","SobreDesigner","SobreSocial","SobreCreativo",
                   "linguagen1","porcento1","linguagen2","porcento2","linguagen3","porcento3","linguagen4","porcento4","linguagen5","porcento5","linguagen6","porcento6","linguagen7","porcento7","linguagen8","porcento8","linguagen9","porcento9","linguagen10","porcento10",
                   "titulo1","imagemProjeto1","DescricaoProjeto1","LinkProjeto1","titulo2","imagemProjeto2","DescricaoProjeto2","LinkProjeto2","titulo3","imagemProjeto3","DescricaoProjeto3","LinkProjeto3","titulo4","imagemProjeto4","DescricaoProjeto4","LinkProjeto4",
                   "localizacaoVoce","CorPrimaria","CorSecundaria","CorDoFundo","ImagemSobreVoce"]
        
    
    template_name = 'template_portifolio/portfolio3.html'
    success_url = reverse_lazy('listarTodosPortfolios')

    def get_object(self, queryset=None):
        self.object = Portfolio3.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
