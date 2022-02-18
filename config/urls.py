from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.conf.urls.static import static


# minor
urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug_toolbar', include('debug_toolbar.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
