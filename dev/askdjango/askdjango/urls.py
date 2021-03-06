"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^weblog/', include('blog.urls', namespace='blog')), # url(r'^weblog/', include('blog.urls'), namespace='blog'),으로 작성하면 안된다. include 안에 namespace를 작성해야 한다. 
]

'''
스태틱 파일은 장고에서 서빙 기능을 지원하지만
미디어 파일은 장고에서 기본적으로 서빙 기능을 지원하지 않는다.
(단, 디버그 옵션이 꺼져있으면 static 함수는 빈 리스트를 반환한다)
'''
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''django-debug-toolbar를 사용하기 위한 설정
'''
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^__debug__/', include(debug_toolbar.urls)),
	]
