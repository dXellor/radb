from django.contrib.auth.decorators import user_passes_test

def check_login_state(user):
    return not user.is_authenticated

user_logout_req = user_passes_test(check_login_state, '/profile', None)

def deny_for_logged_in(view_function):

    return user_logout_req(view_function)


