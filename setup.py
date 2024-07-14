from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='diec',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A tool that encodes text and give out a key, that you can decode with this program too!',
    author='D&I',
    author_email='projectsdi02@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/wfxey/binaryconvert',
    download_url='https://github.com/D-I-Projects/diec/archive/refs/tags/v0.1.tar.gz',
    keywords=['binary', '8-bit', 'text-to-binary'],
    install_requires=[
        #Empty
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Text Converter',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
