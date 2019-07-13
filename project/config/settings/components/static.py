STATIC_URL = '/static/'
STATICFILES_DIRS = []

if ENV == 'production':
    pass
elif ENV == 'staging':
    pass
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'assets')