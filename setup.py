from setuptools import setup

packages = ['Django']

setup(
    name="django_zoneblog",
    version="0.1",
    url="http://github.com/argaen/django_zoneblog",
    description="Lightweight blog app",
    author="argaen",
    author_email="manu.mirandad@gmail.com",
    packages=['zone_blog'],
    include_package_data=True,
    keywords=['django', 'blog', 'light'],
    install_requires=packages
)
