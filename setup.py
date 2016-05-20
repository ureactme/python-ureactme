from setuptools import setup, Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import unittest

        modules = ['ureactme.tests.test_client',
                   'ureactme.tests.test_models']
        suite = unittest.TestSuite()
        suite.addTests(unittest.defaultTestLoader.loadTestsFromNames(modules))
        unittest.TextTestRunner().run(suite)

long_description = "Client library for ureact.me API service"

try:
    long_description = open("README.md").read()
except:
    pass

setup(name='ureactme',
      version='0.2.1',
      packages=['ureactme', ],
      license='MIT',
      author='Thiago F. Pappacena',
      author_email='pappacena@gmail.com',
      url='https://github.com/pappacena/',
      description='UReact.me API lib',
      long_description=long_description,
      install_requires=['setuptools>=17.1', 'requests',
                        'mock', 'freezegun>=0.3.5'],
      tests_require=['freezegun>=0.3.5'],
      cmdclass={'test': TestCommand},
      classifiers=['Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4'])
