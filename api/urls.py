from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	# path('', views.ApiOverview.as_view(), name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	# path('task-list/', views.TaskListView.as_view(), name="task-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),

	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
	path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
	path('login/', views.UserLoginView.as_view(), name='user-login'),
]