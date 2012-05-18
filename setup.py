from setuptools import setup, find_packages

def listify(filename):
    return filter(None, open(filename,'r').read().split('\n'))

setup(
    name = "jmbo-your-words",
    version = "0.0.1",
    url = 'http://github.com/praekelt/jmbo-word-suggest',
    license = 'BSD',
    description = 'Provides users to submit their own stories',
    author = 'Praekelt Foundation',
    author_email = 'dev@praekeltfoundation.org',
    packages = find_packages(),
    install_requires = ['setuptools'],
    classifiers = [
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking'
    ]
)
