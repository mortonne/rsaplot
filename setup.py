import glob
import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


scripts = glob.glob('bin/[a-z]*')

setuptools.setup(
    name='rsaplot',
    version='0.1.0',
    description='Tools for visualizing representational dissimilarity data.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Neal Morton',
    author_email='mortonne@gmail.com',
    license='GPLv3',
    url='http://github.com/mortonne/rsaplot',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'scipy',
        'sklearn',
        'matplotlib',
        'pandas',
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
    ]
)
