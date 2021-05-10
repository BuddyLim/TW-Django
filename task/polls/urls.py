from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    #By default the path for '' is polls/
    path('', views.index, name='index'),
    #This would be polls/thank-you, for specific forms, follow '<int:question_id>/thank-you
    path('thank-you', views.thank_you, name='thank-you')
]