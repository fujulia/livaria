from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from livraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autores" , AutorViewSet)
router.register(r"livros", LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
]
