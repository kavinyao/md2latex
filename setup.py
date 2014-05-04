from distutils.core import setup

setup(
    name='md2latex',
    version='0.0.1',
    author='Kavin Yao',
    author_email='kavinyao@gmail.com',
    packages=['md2latex'],
    scripts=['bin/md2latex'],
    url='https://github.com/kavinyao/md2latex',
    license='LICENSE',
    description='Simple markdown to LaTeX converter.',
    long_description=open('README.md').read(),
    install_requires=[
        "mistune == 0.2.0",
    ],
)
