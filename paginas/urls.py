from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#### Templates #######
from .views import ListarTodosPortfolios
from .views import PortfolioDelete, DeletePortfolio2, DeletePortfolio3
from .views import PortfolioUpdate, PortfolioUpdate2, PortfolioUpdate3
from .views import Portfolio_one, Portfolio_Two, Portfolio_Thre



urlpatterns = [
    
    ###### paginas #####
    path('', views.index, name='index'),
    path('erro/', views.erro, name='erro'),

    ##### Ver templates #######
    path('VerPortfolio1/', views.VerPortfolio1, name='VerPortfolio1'),
    path('VerPortfolio2/', views.VerPortfolio2, name='VerPortfolio2'),
    path('VerPortfolio3/', views.VerPortfolio3, name='VerPortfolio3'),
    
    ##### Criar templates ######
    path('portfolio_one/', Portfolio_one.as_view(), name='portfolio_one'),
    path('portfolio_two/', Portfolio_Two.as_view(), name='portfolio_Two'),
    path('portfolio_Thre/', Portfolio_Thre.as_view(), name='portfolio-thre'),


    ###### Lista dos seus templates ########
    path('listarTodosPortfolios/', views.ListarTodosPortfolios.as_view(), name='listarTodosPortfolios'),


    ##### Excluir templates ######
    path('excluir/carro/<int:pk>/', PortfolioDelete.as_view(), name='excluir-Portifolio'),
    path('excluir/portfolio/<int:pk>/', DeletePortfolio2.as_view(), name='excluir-PortifolioTwo'),
    path('excluir/portfolio3/<int:pk>/', DeletePortfolio3.as_view(), name='excluir-PortifolioThre'),


    ######### Ver sua criação ######
    path('<int:id>', views.detail_page, name='detail'),
    path('MeuPortfolio/<int:id>', views.detail_page2, name='detail2'),
    path('MeuPortfolioThre/<int:id>', views.detail_page3, name='detailThre'),


    ##### Editar template #######
    path('editar/portfolio/<int:pk>/', PortfolioUpdate.as_view(), name='editar-portfolio'),
    path('editar/portfolio2/<int:pk>/', PortfolioUpdate2.as_view(), name='editar-portfolio2'),
    path('editar/portfolio3/<int:pk>/', PortfolioUpdate3.as_view(), name='editar-portfolio3'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)