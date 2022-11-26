Features
============
- Create a cms page where you can setup form fields, a captcha and submit button.
- Works in python3.
- Set the apphook to 'Forms' and then the redirect works.
- Create a 'thank you' page where you can redirect to.
- Forms and all fields are saved in the database.
- When set the ``send mail option`` it sends a mail with all the fields to the specified receivers.
- In the admin, can view every form submission with the fields.
- In the admin, export is possible to .csv.

Installation
============

Run ``pip install git+https://github.com/svandeneertwegh/corebytecms-forms``.

Update ``INSTALLED_APPS`` with ::

    INSTALLED_APPS = [
        ...
        'cms_forms',
        'cms_forms.contrib.email_notifications',
        'captcha',
    ]


Creating a Form
===============

You can create forms in the admin interface now. Search for the label ``Forms``.

Create a CMS page and install the ``Forms`` app there (choose ``Forms`` from the ``Advanced Settings -> Application`` dropdown).

Now redeploy/restart the site again.

The above CMS site has become a forms POST landing page - a place where submission errors get displayed if there are any.


Available Plug-ins
==================

``Form`` plugin lets you embed certain forms on a CMS page.

``Fieldset`` groups fields.

``Text Field`` renders text input.

``Text Area Field`` renders text input.

``Yes/No Field`` renders checkbox.

``Select Field`` renders single select input.

``Date Field`` renders date input.

``Multiple Select Field`` renders multiple checkboxes.

``File field`` renders a file upload input.

``Image field`` same as ``file field`` but validates that the uploaded file is an image.

