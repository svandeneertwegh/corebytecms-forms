
CMS_FORMS_IS_HONEYPOT_CAPTCHA_ENABLED = True
CMS_FORMS_SHOW_ALL_RECIPIENTS = False
# CMS_FORMS_TEMPLATES = ((DEFAULT_FORM_TEMPLATE, _('Default')),)
CMS_FORMS_DEFAULT_TEMPLATE = 'cms_forms/form.html'
CMS_FORMS_ACTION_BACKENDS = {
    'default': 'cms_forms.action_backends.DefaultAction',
    'email_only': 'cms_forms.action_backends.EmailAction',
    'none': 'cms_forms.action_backends.NoAction',
}
CMS_FORMS_EMAIL_THEMES = [('default', _('default'))]
