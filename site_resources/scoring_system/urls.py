from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.team_rankings),
    path('match/<int:field>', views.match),
    path('scoring', views.scoring),
    path('judge_panel', views.judge_panel),
    path('submit_score', views.submit_score, name='submit_score'),
    path('generate_results', views.generate_results, name='generate_results')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)