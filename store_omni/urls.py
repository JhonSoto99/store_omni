"""store URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    path,
)
from django.conf.urls import url,include
from django.contrib import admin

# View
from accounts import views as accounts_views
from store_omni import views as store_views

# Django RestFRamework
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('payments/', include(('payments.urls', 'payments'), namespace='payments')),
    path('shipping/', include(('shipping.urls', 'shipping'), namespace='shipping')),

    # Api Rest Urls
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^api/(?P<version>(v1|v2))/accounts/', include(('accounts.api.urls', 'api_accounts'), namespace='api_accounts')),
    url(r'^api/(?P<version>(v1|v2))/products/', include(('products.api.urls', 'api_products'), namespace='api_products')),
    url(r'^api/(?P<version>(v1|v2))/orders/', include(('orders.api.urls', 'api_orders'), namespace='api_orders')),
    url(r'^api/(?P<version>(v1|v2))/payments/', include(('payments.api.urls', 'api_payments'), namespace='api_payments')),
    url(r'^api/(?P<version>(v1|v2))/shipping/', include(('shipping.api.urls', 'api_shipping'), namespace='api_shipping')),

    path(
      route='',
      view=accounts_views.login_view,
      name='store_login'
    ),
    path(
      route='404',
      view=store_views.not_found_view,
      name='not_found'
    ),
    path(
      route='500',
      view=store_views.server_error_view,
      name='server_error'
    )

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
