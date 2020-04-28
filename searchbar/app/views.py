# from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City,Scholarship,Citty,Country


class HomePageView(TemplateView):
    template_name = 'home.html'

# class SearchResultsView(ListView):
#     model = City
#     template_name = 'search_results.html'

# class SearchResultsView(ListView):
#     model = City
#     template_name = 'search_results.html'
#     queryset = City.objects.filter(name__icontains='Boston') # new
# class SearchResultsView(ListView):
#     model = City
#     template_name = 'search_results.html'
#
#     def get_queryset(self): # new
#         return City.objects.filter(name__icontains='Boston')
class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list
    # return redirect('/dataflair')


# youtube
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Journal, Category
# from .serializers import JournalSerializer


def is_valid_queryparam(param):
    return param != '' and param is not None


# def filter(request):
#     qs = Journal.objects.all()
#     categories = Category.objects.all()
#     title_contains_query = request.GET.get('title_contains')
#     id_exact_query = request.GET.get('id_exact')
#     title_or_author_query = request.GET.get('title_or_author')
#     view_count_min = request.GET.get('view_count_min')
#     view_count_max = request.GET.get('view_count_max')
#     date_min = request.GET.get('date_min')
#     date_max = request.GET.get('date_max')
#     category = request.GET.get('category')
#     reviewed = request.GET.get('reviewed')
#     not_reviewed = request.GET.get('notReviewed')
#
#     if is_valid_queryparam(title_contains_query):
#         qs = qs.filter(title__icontains=title_contains_query)
#
#     elif is_valid_queryparam(id_exact_query):
#         qs = qs.filter(id=id_exact_query)
#
#     elif is_valid_queryparam(title_or_author_query):
#         qs = qs.filter(Q(title__icontains=title_or_author_query)
#                        | Q(author__name__icontains=title_or_author_query)
#                        ).distinct()
#
#     if is_valid_queryparam(view_count_min):
#         qs = qs.filter(views__gte=view_count_min)
#
#     if is_valid_queryparam(view_count_max):
#         qs = qs.filter(views__lt=view_count_max)
#
#     if is_valid_queryparam(date_min):
#         qs = qs.filter(publish_date__gte=date_min)
#
#     if is_valid_queryparam(date_max):
#         qs = qs.filter(publish_date__lt=date_max)
#
#     if is_valid_queryparam(category) and category != 'Choose...':
#         qs = qs.filter(categories__name=category)
#
#     if reviewed == 'on':
#         qs = qs.filter(reviewed=True)
#
#     elif not_reviewed == 'on':
#         qs = qs.filter(reviewed=False)
#
#     return qs

#
# def infinite_filter(request):
#     limit = request.GET.get('limit')
#     offset = request.GET.get('offset')
#     return Journal.objects.all()[int(offset): int(offset) + int(limit)]


# def is_there_more_data(request):
#     offset = request.GET.get('offset')
#     if int(offset) > Journal.objects.all().count():
#         return False
#     return True


# def BootstrapFilterView(request):
#     qs = filter(request)
#     context = {
#         'queryset': qs,
#         'categories': Category.objects.all()
#     }
#     return render(request, "bootstrap_form.html", context)


# class ReactFilterView(generics.ListAPIView):
#     serializer_class = JournalSerializer
#
#     def get_queryset(self):
#         qs = filter(self.request)
#         return qs


# class ReactInfiniteView(generics.ListAPIView):
#     serializer_class = JournalSerializer
#
#     def get_queryset(self):
#         qs = infinite_filter(self.request)
#         return qs
#
#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response({
#             "journals": serializer.data,
#             "has_more": is_there_more_data(request)
#         })
# myyy
def filtr(request):
    qs = Scholarship.objects.all()
    countries = Country.objects.all()
    # name_contains_query=request.GET.get('q')
    name_contains_query = request.GET.get('searchbar')
    # print(name_contains_query)
    # description_exact_query = request.GET.get('id_exact')
    # title_or_author_query = request.GET.get('title_or_author')
    # view_count_min = request.GET.get('view_count_min')
    # view_count_max = request.GET.get('view_count_max')
    # date_min = request.GET.get('date_min')
    # date_max = request.GET.get('date_max')
    city = request.GET.get('cities')
    country = request.GET.get('countries')
    # not_reviewed = request.GET.get('notReviewed')
    # p=request.GET.get('title_contains')
    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(Q(name__icontains=name_contains_query) | Q(description__icontains=name_contains_query)).distinct()

                       # | Q(url__icontains=name_contains_query)
                       # | Q(city__icontains=name_contains_query)
                       # | Q(country__icontains=name_contains_query)
                       # | Q(research__icontains=name_contains_query)
                       #  ).distinct()

    if is_valid_queryparam(city) and city != 'Choose...':
            qs = qs.filter(city__name=city)
    if is_valid_queryparam(country) and country != 'Choose...':
                qs = qs.filter(country__name=country)
    return qs
def BootstrapFilterViews(request):
    qs = filtr(request)
    context = {
        'queryset': qs,
        'countries': Country.objects.all(),
        'cities': Citty.objects.all(),

    }
    return render(request, "find_bootstrap.html", context)