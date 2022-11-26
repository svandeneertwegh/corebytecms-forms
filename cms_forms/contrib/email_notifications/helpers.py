# -*- coding: utf-8 -*-
import os
from string import Template


EMAIL_TEMPLATES_BASE = 'cms_forms/email_notifications/emails/'

EMAIL_THEMES_PATH = os.path.join(EMAIL_TEMPLATES_BASE, 'themes')
EMAIL_NOTIFICATIONS_PATH = os.path.join(EMAIL_TEMPLATES_BASE, 'notification')


def get_theme_template_name(theme, suffix='txt'):
    filename = '{0}.{1}'.format(theme, suffix)
    template_name = os.path.join(EMAIL_THEMES_PATH, filename)
    return template_name


def render_text(message, context):
    template = Template(template=message)
    return template.safe_substitute(**context)
