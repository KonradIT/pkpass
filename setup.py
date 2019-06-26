from setuptools import setup
with open("README.md", "r") as fh:
      long_description = fh.read()
setup(name='pkpass',
      version='0.1.1',
      description='General-purpose .pkpass file reader, includes airline and train specific parsers',
      url='http://github.com/konradit/pkpass',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Konrad Iturbe',
      author_email='mail@chernowii.com',
      license='MIT',
      packages=['pkpass'],
      zip_safe=False)

