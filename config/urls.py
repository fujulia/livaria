from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from usuario.router import router as usuario_router

from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

from drf_spectacular.views import ( SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView,
)

from livraria.views import UsuarioViewSet

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from livraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autores" , AutorViewSet)
router.register(r"livros", LivroViewSet)
router.register(r"usuarios", UsuarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
      path("api/", include(router.urls)),
]


urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)