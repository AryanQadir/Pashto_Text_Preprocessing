from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pashto_text_preprocessing',
    version='1.0.0',
    author='Abdul Qadir, Ihsan Ullah',
    author_email='aryanqadira1@gmail.com',
    description='Pashto Text Preprocessing Toolkit for Low-Resource Language NLP',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/AryanQadir/Pashto_Text_Preprocessing,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Natural Language :: Pashto"
    ],
    python_requires='>=3.6',
    install_requires=[],
    license='MIT'
)
