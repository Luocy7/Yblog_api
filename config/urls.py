"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from blog.views_api import PostViewSet, CategoryViewSet, TagViewSet, FriendLinkViewSet
from blog.views import PostDetailView

router = routers.DefaultRouter()

router.register(r"posts", PostViewSet, basename="post")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"tags", TagViewSet, basename="tag")
router.register(r"friendlink", FriendLinkViewSet, basename="friendlink")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include(router.urls)),
    url(r'admin/', admin.site.urls, name="admin_site"),
    url(r'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r"ypost/(?P<pk>\d+)/$", PostDetailView.as_view(), name="detail"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
