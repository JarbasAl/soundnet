from setuptools import setup

setup(
    name='soundnet',
    version='0.1.2',
    packages=['soundnet'],
    install_requires=["numpy",
                      "keras",
                      "tensorflow<=1.15.2",
                      "librosa"],
    include_package_data=True,
    url='https://github.com/JarbasAl/soundnet',
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='sound classification with SoundNet'
)
