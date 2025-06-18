from setuptools import setup

setup(
    name='ml-project-generator',
    version='0.1.0',
    packages=['ml_project_generator'],
    entry_points={
        'console_scripts': [
            'ml-project = ml_project_generator.__main__:main',
        ],
    },
    python_requires='>=3.6',
    author='Marcus Schou',
    description='A simple CLI tool to generate ml project folder templates.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
