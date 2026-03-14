from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def app_home(request):
    return render(request, "users/app_home.html")


@ensure_csrf_cookie
def app_register(request):
    return render(request, "users/app_register.html")


@ensure_csrf_cookie
def app_login(request):
    return render(request, "users/app_login.html")


@ensure_csrf_cookie
def app_logout(request):
    return render(request, "users/app_logout.html")


@ensure_csrf_cookie
def app_forgot_password(request):
    return render(request, "users/app_forgot_password.html")


@ensure_csrf_cookie
def app_reset_password(request, uidb64=None, token=None):
    endpoint = ""
    if uidb64 and token:
        endpoint = f"/reset_password/{uidb64}/{token}/"
    context = {
        "uidb64": uidb64,
        "token": token,
        "endpoint": endpoint,
    }
    return render(request, "users/app_reset_password.html", context)


@ensure_csrf_cookie
def app_change_password(request):
    return render(request, "users/app_change_password.html")


@ensure_csrf_cookie
def app_profile(request):
    return render(request, "users/app_profile.html")


@ensure_csrf_cookie
def app_profile_update(request):
    return render(request, "users/app_profile_update.html")


@ensure_csrf_cookie
def app_token_verify(request):
    return render(request, "users/app_token_verify.html")


@ensure_csrf_cookie
def app_token_refresh(request):
    return render(request, "users/app_token_refresh.html")


@ensure_csrf_cookie
def app_account_delete(request):
    return render(request, "users/app_account_delete.html")


@ensure_csrf_cookie
def app_2fa_verify(request):
    return render(request, "users/app_2fa_verify.html")


@ensure_csrf_cookie
def app_2fa_enable(request):
    return render(request, "users/app_2fa_enable.html")


@ensure_csrf_cookie
def app_2fa_disable(request):
    return render(request, "users/app_2fa_disable.html")


@ensure_csrf_cookie
def app_security(request):
    return render(request, "users/app_security.html")
