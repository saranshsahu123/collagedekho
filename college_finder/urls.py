# college_finder/urls.py 
# (Located in the same folder as settings.py)

from django.contrib import admin
from django.urls import path, include # Make sure include is imported
from django.conf import settings
from django.conf.urls.static import static

# DO NOT import any views directly here for signup/login/logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # This line correctly sends requests starting with 'accounts/' 
    # to your users/urls.py file (the one you posted)
    path('accounts/', include('users.urls')), 

    # This line correctly sends other requests (like the homepage)
    # to your colleges/urls.py file
    path('', include('colleges.urls')), 
]

# This part is for serving images during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)