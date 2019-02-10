from flask import Blueprint


user_blueprint = Blueprint("user", __name__, url_prefix='/user')


#     url("^$", usersMap, name="show_map"),
#     url("^view_users.html$", usersMap, name="show_map"),
@user_blueprint.route('/')
@user_blueprint.route('/view_users.html')
def show_map():
    pass


#     url("^edit/(?P<theId>[0-9a-z\-]+)/$", updateUser, name="update_user"),
@user_blueprint.route('/edit/<int:user_id>')
def update_user(user_id):
    pass


#     url("^update_user.html$", emailEditAddress, name="email_update_user_link"),
@user_blueprint.route('/update_user.html')
def email_update_user_link():
    pass


#     url(r'^edit/email_confirm.html$',TemplateView.as_view(template_name='email_confirm.html')),


#     url(r'^user/(?P<username>\w+)/block/$', user_block, {}, name='user_block'),
@user_blueprint.route('/<username>/block')
def user_block(username):
    pass


#     url(r'^user/(?P<username>\w+)/unblock/$', user_unblock, {}, name='user_unblock'),
@user_blueprint.route('/<username>/unblock')
def user_unblock(username):
    pass


#     url(r'^user/(?P<username>\w+)/trust/$', user_trust, {}, name='user_trust'),
@user_blueprint.route('/<username>/trust')
def user_trust(username):
    pass


#     url(r'^user/(?P<username>\w+)/untrust/$', user_untrust, {}, name='user_untrust'),
@user_blueprint.route('/<username>/untrust')
def user_untrust(username):
    pass


#     url(r'^user/(?P<username>\w+)/admin$', UserDetailsPluginsList.as_view(), name='user_details'),
@user_blueprint.route('/<username>/admin')
def user_details(username):
    pass


#     url(r'^user/(?P<username>\w+)/manage/$', user_permissions_manage, {}, name='user_permissions_manage'),
@user_blueprint.route('/<username>/manage')
def user_permissions_manage(username):
    pass
