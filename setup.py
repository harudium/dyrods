from distutils.core import setup

setup(
    name = "dyrods",
    version = "0.1",
    packages = [
        "dyrods",
        "dyrods.management",
        "dyrods.management.commands",
        "dyrods.templatetags",
        "dyrods.tests",
    ],
    author = "Kyongjin Jo",
    author_email = "kyongjin.jo@sk.com",
    description = "dyrods web documents",
    url = "https://github.com/harudium/dyrods/master",
    package_data = {
        'https://github.com/harudium/dyrods': [
            'templates/*.html',
            'templates/kong/*.html',
            'templates/kong/*.txt',
            'fixtures/*.json',

        ],
    },
)
