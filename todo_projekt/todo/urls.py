from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from todo import views  # Import widoków aplikacji "todo"

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),  # Logowanie jako strona startowa
    path('tasks/', views.task_list, name='task_list'),  # Lista zadań (ścieżka poprawiona)
    path('add/', views.add_task, name='add_task'),  # Dodawanie zadania
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Usuwanie zadania
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Edycja zadania
    path('admin/', admin.site.urls),  # Panel administracyjny
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Wylogowanie
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
path('change_status/<int:task_id>/', views.change_task_status, name='change_task_status'),
]


