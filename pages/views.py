# from django.http import HttpResponse

from django.views.generic import TemplateView

# def homePageView(request):
#     return HttpResponse("안녕하세요 :)")

class HomePageView(TemplateView): #HomePageView는 내가 직접 만든 것임
    template_name = "home.html"

class HomePageLocation(TemplateView):
    template_name = "location.html"

class TermsView(TemplateView):
    template_name = "terms.html"