from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT
from accounts.views import login, register, logout, profile, edit_profile, search_titles, edit_profilepicture, addcrush, removecrush, like, createwink, newsfeed, users, wall, fleekyvalue
import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

###########################################################

#Authentication#


    url(r'^$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^//logout/$', logout, name='logout'),


###########################################################

#Profile#

    url(r'^profile/$', profile, name='profile'),
    url(r'^wall/(?P<id>\d+)/$', wall, name='wall'),
    url(r'^profile/(?P<id>\d+)/$', profile),
    url(r'^profile/(?P<var>\d+)/$', profile),


    url(r'^fleekyvalue/$', fleekyvalue),

    url(r'^profile/(?P<id>\d+)/(?P<id2>\d+)/$', profile),
    url(r'^editprofile/$', edit_profile, name='editprofile'),
    url(r'^editprofilepicture/$', edit_profilepicture, name='edit_profilepicture'),
    url(r'^search/$', search_titles),

    url(r'^addcrush/(?P<id>\d+)/$', addcrush, name="addcrush"),
    url(r'^addcrush/(?P<id>\d+)/(?P<id2>\d+)/$', addcrush, name="addcrush2"),

    url(r'^removecrush/(?P<id>\d+)/$', removecrush, name="removecrush"),


    url(r'^like/$', like, name="ajaxlike"),
    url(r'^like/(?P<id>\d+)/$', like, name="like"),



    url(r'^createwink/(?P<id>\d+)/$', createwink, name="createwink"),
    url(r'^createwink/(?P<id>\d+)/(?P<id2>\d+)/$', createwink, name="createwink2"),

###########################################################

#Newsfeed#

    url(r'^newsfeed/$', newsfeed, name="feed"),


###########################################################

#Users#

    url(r'^users/$', users, name='users'),


    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
