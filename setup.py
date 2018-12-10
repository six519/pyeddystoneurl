#!/usr/bin/env python
import pyeddystoneurl_helper
 
from distutils.core import setup
from distutils.extension import Extension

setup(name="pyeddystoneurl",
    version="1.0.0",
    description="Python C Extension To Scan Eddystone-URL Beacons",
    author="Ferdinand Silva",
    author_email="ferdinandsilva@ferdinandsilva.com",
    url="https://github.com/six519/pyeddystoneurl",
    packages=['pyeddystoneurl'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
		'Programming Language :: C',
        'License :: Freeware',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    download_url="https://github.com/six519/pyeddystoneurl",
    ext_modules=[
        Extension("pyeddystoneurl_scan",
            include_dirs = ['/usr/include/bluetooth'],
            libraries = ['bluetooth'], 
            sources = ["pyeddystoneurl_scan.c"]
        )
    ]
)