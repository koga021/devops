from setuptools import setup


setup(name='devops',
      version='0.2',
      keywords='devops python-devops devops-tools',
      description='Devops Template Init Tools',
      url='https://github.com/koga021/devops',
      author='Douglas de Araujo Silva Ribas',
      author_email='ribas.douglas@gmail.com',
      license='MIT',
      packages=['devops','jinja2','argparse'],
      scripts=['bin/devops'],
      entry_points={'console_scripts': ['devops = devops:main']},
      zip_safe=False)
