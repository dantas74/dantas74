from django_distill import distill_path

from . import views

urlpatterns = [
    distill_path('', views.HomeView.as_view(), name='home')
]
