from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.login_app.urls")),
    url(r'^admin/', include('apps.admin_app.urls')),
    # url(r'^courses/', include('apps.course_app.urls')),
    url(r'^plans/', include('apps.plan_app.urls')),
]
