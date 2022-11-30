from django.urls import path
from .views import HomePageView, HomePageLocation, TermsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"), #class HomePageView를 넣는다. name은 home이다. 
    path("location/", HomePageLocation.as_view(), name="location"), # /다음에 연결할 이름을 넣는다.
    path("terms/", TermsView.as_view(), name="terms")
]