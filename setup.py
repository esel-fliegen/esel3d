import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="esel3d-Donkey",
    version="0.1.36",
    author="Khan Tran",
    author_email="esel.fliegen@gmail.com",
    description="A 3D plotter for Google Colab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/esel-fliegen/esel3d",
    project_urls={
        "Bug Tracker": "https://github.com/esel-fliegen/esel3d/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)