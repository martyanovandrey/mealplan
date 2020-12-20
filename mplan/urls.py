from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create_recipe', views.create_recipe, name='create_recipe'),
    path('create_recipe_api', views.create_recipe_api, name='create_recipe_api'),
    path('food/<str:foodName>', views.food_API, name='food'),
    path('ingredient/<int:ingredientId>', views.ingredient_API, name='ingredient')
    ]