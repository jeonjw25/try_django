from django.urls import path

from . import views
app_name = 'news'
urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]

# url request/ 호출할 함수/ 템플릿에서 쓰일 이름