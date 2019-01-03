"""
Export Directory API client
"""

from setuptools import setup, find_packages

setup(
    name='directory_proxy',
    version='0.1.0',
    url='https://github.com/uktrade/directory-proxy',
    license='MIT',
    author='Department for International Trade',
    description='Proxy',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'django>=1.11.15,<2.0a1',
        'django-revproxy>=0.9.15,<1.0.0',
        'django-environ>=0.4.5,<1.0.0',
        'gunicorn>=19.9.0,<20.0.0',
        'raven>=6.10.0,<7.0.0',
        'sigauth>=4.0.1,<5.0.0',
        'directory-components>=3.5.0,<4.0.0',
    ],
    extras_require={
        'test': [
            'pytest==4.0.2',
            'pytest-cov==2.6.0',
            'pytest-sugar==0.9.2',
            'pytest-django==3.4.4',
            'flake8==3.6.0',
            'codecov==2.0.15',
            'requests_mock==1.5.2',
            'twine>=1.11.0,<2.0.0',
            'wheel>=0.31.0,<1.0.0',
            'setuptools>=38.6.0,<39.0.0'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
