import os


EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"


INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.messages",
    "easy_thumbnails",
    "filer",
    "mptt",
    "cms",
    "menus",
    "treebeard",
    "djangocms_text_ckeditor",
    "sekizai",

    "cms_forms",
    "cms_forms.contrib.email_notifications",
    "captcha",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]
CMS_LANGUAGES = {
    1: [
        {
            "code": "en",
            "name": "English",
        }
    ]
}

# required otherwise subject_location would throw an error in the template
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

LANGUAGE_CODE = "en"
ALLOWED_HOSTS = ["localhost"]
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = False
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES_VIEWPORT_BREAKPOINTS = [576, 768, 992]

SECRET_KEY = "fake-key"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

CMS_TEMPLATES = (
    ('test_fullwidth.html', 'Fullwidth'),
    ('test_page.html', 'Normal page'),
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase.sqlite",  # This is where you put the name of the db file.
        # If one doesn't exist, it will be created at migration time.
    }
}

SITE_ID = 1

ROOT_URLCONF = "tests.test_urls"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
