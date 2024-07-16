from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='diec',
    version='1.4',
    packages=find_packages(),
    license='MIT',
    description='A tool that encodes text and provides a key for decoding!',
    author='D&I',
    author_email='projectsdi02@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/wfxey/diec',
    download_url='https://github.com/D-I-Projects/diec/archive/refs/tags/v1.4.tar.gz',
    keywords=['diec', 'encoding', 'decoding'],
    install_requires=[
        'binaryconvert',
    ],
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points='''
        [console_scripts]
        diec-cli=diec.cli:cli
    ''',
)
