from django.urls import include, path
from . import views
urlpatterns =[
    path("signup/",views.userSignup.as_view()),
    path("getMembershipDetails/<email>/",views.userMembership.as_view())

]