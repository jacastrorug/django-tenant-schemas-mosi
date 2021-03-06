from os.path import exists

from setuptools import setup

setup(
    name="django-tenant-schemas-mosi",
    author="Julian Castro Ruge",
    author_email="juliancastroruge@gmail.com",
    packages=[
        "tenant_schemas",
        "tenant_schemas.migration_executors",
        "tenant_schemas.postgresql_backend",
        "tenant_schemas.management",
        "tenant_schemas.management.commands",
        "tenant_schemas.templatetags",
        "tenant_schemas.test",
        "tenant_schemas.tests",
    ],
    scripts=[],
    url="https://github.com/jacastrorug/django-tenant-schemas-mosi",
    license="MIT",
    description="Tenant support for Django using PostgreSQL schemas.",
    long_description=open("README.rst").read() if exists("README.rst") else "",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=["Django>=1.11", "ordered-set", "psycopg2-binary", "six"],
    zip_safe=False,
    version=0.2
)
