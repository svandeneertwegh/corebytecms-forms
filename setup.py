from setuptools import find_packages, setup

from cms_forms import __version__


REQUIREMENTS = [
    'django>=2.0<4',
    'django-cms>=3.5',
    'djangocms-text-ckeditor',
    'djangocms-attributes-field>=1.0.0',
    'pandas',
    'pillow',
    'django-filer',
    'django-sizefield',
    'six>=1.0',
    'django-simple-captcha',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Framework :: Django',
    'Framework :: Django :: 3.2',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='corebytecms-forms',
    version=__version__,
    author='Corebyte',
    author_email='info@corebyte.nl',
    url='https://github.com/svandeneertwegh/corebytecms-forms',
    license='BSD',
    description='Create forms and embed them on CMS pages',
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords='django django-cms form-builder form fields',
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='run_tests.run',
)
