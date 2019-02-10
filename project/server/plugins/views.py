"""
Views for plugins
"""
from flask import Blueprint

from .models import Plugin, PluginVersion


plugin_blueprint = Blueprint("plugin", __name__, url_prefix='/plugins')


#     url(r'^plugins_new.xml$', xml_plugins_new, {}, name='xml_plugins_new'),
@plugin_blueprint.route('/plugins_new.xml')
def xml_plugins_new():
    pass


#     url(r'^plugins.xml$', xml_plugins, {}, name='xml_plugins'),
#     url(r'^plugins_(?P<qg_version>\d+\.\d+).xml$', xml_plugins, {}, name='xml_plugins_version_filtered_cached'),
#     url(r'^version_filtered/(?P<qg_version>\d+\.\d+).xml$', xml_plugins, {}, name='xml_plugins_version_filtered_uncached'),
@plugin_blueprint.route('/plugins.xml')
@plugin_blueprint.route('/plugins_<version:qg_version>.xml')
@plugin_blueprint.route('/version_filtered/<version:qg_version>.xml')
def xml_plugins(qg_version=None, stable_only=None, package_name=None):
    pass


#     url(r'^tags/(?P<tags>[^\/]+)/$', TagsPluginsList.as_view(), name='tags_plugins'),
@plugin_blueprint.route('/tags/<tags>')
def tags_plugins(tags):
    pass


#     url(r'^add/$', plugin_upload, {}, name='plugin_upload'),
@plugin_blueprint.route('/add')
def plugin_upload():
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/manage/$', plugin_manage, {}, name='plugin_manage'),
@plugin_blueprint.route('/<package_name>/manage')
def plugin_manage(package_name):
    pass



#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/delete/$', plugin_delete, {}, name='plugin_delete'),
@plugin_blueprint.route('/<package_name>/delete')
def plugin_delete(package_name):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/update/$', plugin_update, {}, name='plugin_update'),
@plugin_blueprint.route('/<package_name>/update')
def plugin_update(package_name):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/set_featured/$', plugin_set_featured, {}, name='plugin_set_featured'),
@plugin_blueprint.route('/<package_name>/set_featured')
def plugin_set_featured(package_name):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/unset_featured/$', plugin_unset_featured, {}, name='plugin_unset_featured'),
@plugin_blueprint.route('/<package_name>/unset_featured')
def plugin_unset_featured(package_name):
    pass


#     url(r'^$', PluginsList.as_view(), name='approved_plugins'),
@plugin_blueprint.route('/')
def approved_plugins():
    pass


#     url(r'^my$', login_required(MyPluginsList.as_view(additional_context={'title':_('My Plugins')})), name='my_plugins'),
@plugin_blueprint.route('/my')
def my_plugins():
    pass


#     url(r'^featured/$', PluginsList.as_view(queryset=Plugin.featured_objects.all(), additional_context={'title' : _('Featured plugins')}), name='featured_plugins'),
@plugin_blueprint.route('/featured')
def featured_plugins():
    pass


#     url(r'^user/(?P<username>\w+)/$', UserPluginsList.as_view(), name='user_plugins'),
@plugin_blueprint.route('/user/<username>')
def user_plugins(username):
    pass


#     url(r'^server/$', PluginsList.as_view(queryset=Plugin.server_objects.all(), additional_context={'title' : _('QGIS Server plugins')}), name='server_plugins'),
@plugin_blueprint.route('/server')
def server_plugins():
    pass


#     url(r'^unapproved/$', PluginsList.as_view(queryset=Plugin.unapproved_objects.all(), additional_context={'title' : _('Unapproved plugins')}), name='unapproved_plugins'),
@plugin_blueprint.route('/unapproved')
def unapproved_plugins():
    pass


#     url(r'^deprecated/$', PluginsList.as_view(queryset=Plugin.deprecated_objects.all(), additional_context={'title' : _('Deprecated plugins')}), name='deprecated_plugins'),
@plugin_blueprint.route('/deprecated')
def deprecated_plugins():
    pass


#     url(r'^fresh/$', PluginsList.as_view(queryset=Plugin.fresh_objects.all(), additional_context={'title' : _('Fresh plugins')}), name='fresh_plugins'),
@plugin_blueprint.route('/fresh')
def fresh_plugins():
    pass


#     url(r'^stable/$', PluginsList.as_view(queryset=Plugin.stable_objects.all(), additional_context={'title' : _('Stable plugins')}), name='stable_plugins'),
@plugin_blueprint.route('/stable')
def stable_plugins():
    pass


#     url(r'^experimental/$', PluginsList.as_view(queryset=Plugin.experimental_objects.all(), additional_context={'title' : _('Experimental plugins')}), name='experimental_plugins'),
@plugin_blueprint.route('/experimental')
def experimental_plugins():
    pass


#     url(r'^popular/$', PluginsList.as_view(queryset=Plugin.popular_objects.all(), additional_context={'title' : _('Popular plugins')}), name='popular_plugins'),
@plugin_blueprint.route('/my')
def popular_plugins():
    pass


#     url(r'^most_voted/$', PluginsList.as_view(queryset=Plugin.most_voted_objects.all(), additional_context={'title' : _('Most voted plugins')}), name='most_voted_plugins'),
@plugin_blueprint.route('/most_voted')
def most_voted_plugins():
    pass


#     url(r'^most_downloaded/$', PluginsList.as_view(queryset=Plugin.most_downloaded_objects.all(), additional_context={'title' : _('Most downloaded plugins')}), name='most_downloaded_plugins'),
@plugin_blueprint.route('/most_downloaded')
def most_downloaded_plugins():
    pass


#     url(r'^most_rated/$', PluginsList.as_view(queryset=Plugin.most_rated_objects.all(), additional_context={'title' : _('Most rated plugins')}), name='most_rated_plugins'),
@plugin_blueprint.route('/most_rated')
def most_rated_plugins():
    pass


#     url(r'^author/(?P<author>[^/]+)/$', AuthorPluginsList.as_view(), name='author_plugins'),
@plugin_blueprint.route('/author/<author>')
def author_plugins(author):
    pass


# # Version Management
# urlpatterns += [
#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/version/(?P<version>[^\/]+)/manage/$', version_manage, {},  name='version_manage'),
@plugin_blueprint.route('/<package_name>/version/<version>/manage')
def version_manage(package_name, version):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/version/add/$', version_create, {}, name='version_create'),
@plugin_blueprint.route('/<package_name>/version/add')
def version_create(package_name):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/version/(?P<version>[^\/]+)/$', version_detail, {}, name='version_detail'),
@plugin_blueprint.route('<package_name>/version/<version>')
def version_detail(package_name, version):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/version/(?P<version>[^\/]+)/delete/$', version_delete, {}, name='version_delete'),
@plugin_blueprint.route('<package_name>/version/<version>/delete')
def version_delete(package_name, version):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/version/(?P<version>[^\/]+)/update/$', version_update, {}, name='version_update'),
@plugin_blueprint.route('<package_name>/version/<version>/update')
def version_update(package_name, version):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/version/(?P<version>[^\/]+)/download/$', version_download, {}, name='version_download'),
@plugin_blueprint.route('<package_name>/version/<version>/download')
def version_download(package_name, version):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/version/(?P<version>[^\/]+)/approve/$', version_approve, {}, name='version_approve'),
@plugin_blueprint.route('<package_name>/version/<version>/approve')
def version_approve(package_name, version):
    pass


#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/version/(?P<version>[^\/]+)/unapprove/$', version_unapprove, {}, name='version_unapprove'),
@plugin_blueprint.route('<package_name>/version/<version>/unapprove')
def version_unapprove(package_name, version):
    pass


# TODO: What does the RPC allow for?

# # RPC
# urlpatterns += [
#     # rpc4django will need to be in your Python path
#     url(r'^RPC2/$', 'rpc4django.views.serve_rpc_request'),
# ]


# TODO: Implement rating system

# # plugin rating
# from djangoratings.views import AddRatingFromModel
# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
#
#
# urlpatterns += [
#     url(r'rate/(?P<object_id>\d+)/(?P<score>\d+)/', require_POST(csrf_protect(AddRatingFromModel())), {
#         'app_label': 'plugins',
#         'model': 'plugin',
#         'field_name': 'rating',
#     }, name='plugin_rate'),
# ]
#
#
# # Plugin detail (keep last)
# urlpatterns += [
#     url(r'^(?P<package_name>[A-Za-z][A-Za-z0-9-_]+)/$', PluginDetailView.as_view(slug_url_kwarg='package_name', slug_field='package_name'), name='plugin_detail'),
@plugin_blueprint.route('<package_name>')
def plugin_detail(package_name):
    pass
