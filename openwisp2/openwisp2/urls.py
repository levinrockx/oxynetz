from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from openwisp_utils.admin_theme.admin import admin, openwisp_admin

try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy

openwisp_admin()

redirect_view = RedirectView.as_view(url=reverse_lazy('admin:index'))

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('openwisp_controller.urls')),
            url(r'', include('openwisp_monitoring.urls')),
        url(r'^', include('openwisp_radius.urls', namespace='freeradius')),
        url(r'^$', redirect_view, name='index'),
    url(r'^payments/', include('payments.urls')),
    url(r'^', include('openwisp_radius.subscriptions.urls', namespace='subscriptions')),
]

urlpatterns += staticfiles_urlpatterns()
