#!/usr/bin/env python
from __future__ import division, print_function, unicode_literals


HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'tests',
        'aldryn_forms.contrib.email_notifications',
        'djangocms_text_ckeditor',
        'captcha',
        'easy_thumbnails',
        'emailit',
        'filer',
    ],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'CMS_TEMPLATES': (
        ('test_fullwidth.html', 'Fullwidth'),
        ('test_page.html', 'Normal page'),
    ),
    'LANGUAGE_CODE': 'en',
    'EMAIL_BACKEND': 'django.core.mail.backends.dummy.EmailBackend',
}


def run():
    from djangocms_helper import runner
    runner.cms('cms_forms')


if __name__ == '__main__':
    run()