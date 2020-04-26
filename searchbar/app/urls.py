from django.urls import path

# from .views import HomePageView, SearchResultsView,BootstrapFilterView,BootstrapFilterViews
from .views import HomePageView, SearchResultsView,BootstrapFilterViews

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    # path('boot/', BootstrapFilterView, name='bootstrap'),
    path('boots/', BootstrapFilterViews, name='bootstrap'),

]