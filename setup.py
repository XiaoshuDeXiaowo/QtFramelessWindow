import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read().replace('./', 'https://raw.githubusercontent.com/XiaoshuDeXiaowo/QtFramelessWindow/main/')

setuptools.setup(
    name="QtFramelessWindow",
    version="0.0.1",
    keywords="pyqt pyside frameless",
    author="zhiyiYo, XiaoshuDeXiaowo",
    author_email="shokokawaii@outlook.com, xiaoshu312@xiaoshu312.top",
    description="A cross-platform frameless window based on PyQt/PySide, support Win32, macOS and Linux.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="LGPLv3",
    url="https://github.com/XiaoshuDeXiaowo/QtFramelessWindow",
    packages=setuptools.find_packages(),
    install_requires=[
        "qtpy",
        "pywin32;platform_system=='Windows'",
        "pyobjc;platform_system=='Darwin'",
        "PyCocoa;platform_system=='Darwin'",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent'
    ]
)
