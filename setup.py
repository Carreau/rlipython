from distutils.core import setup

with open('readme.md') as f:
    data = f.read()
try:
    import pypandoc
    description = pypandoc.convert(data, 'rst', format='markdown')
    print("""
========================
pypandoc run sucessfully
========================""")
except:
    print("""
=================================================================
pypandoc conversion fail your readme will not be rendered on PyPI
=================================================================""")
    description = data


setup(
    name='rlipython',
    version='0.1.1',
    packages=['rlipython',],
    install_requires=["ipython>5.3"],
    extras_requires={':sys_platform == "darwin"': ['gnureadline']},
    license='BSD',
    author='The IPython Development Team',
    author_email='ipython-dev@python.org',
    url='https://github.com/ipython/rlipython',
    description="readline integration for IPython 5.4+ and 6.0+",
    long_description=open('readme.md').read(),
)
