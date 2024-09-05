def get_theme_user(request):
    theme = 'default'
    if request.user.is_authenticated and request.user.profile.theme is not None:
        theme = request.user.profile.theme
    return {
        'theme_user': f'css/themes/{theme}.css'
    }
