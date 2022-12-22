from setuptools import setup

setup(
    name="tsutil",
    description="Tree sequence utilities",
    long_description="Various functions useful for working with tskit tree sequences in Python",
    url="https://github.com/hyanwong/tsutil",
    author="Tskit Developers",
    python_requires=">=3.10",
    author_email="yan.wong@bdi.ox.ac.uk",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="tree sequence",
    packages=["tsutil"],
    include_package_data=True,
    install_requires=[
        "tskit",
        "tqdm",
    ],
    project_urls={
        "Bug Reports": "https://github.com/hyanwong/tsutil/issues",
        "Source": "https://github.com/tskit-dev/tsconvert",
    },
    license="MIT",
    platforms=["POSIX", "MacOS X"],
    setup_requires=["setuptools_scm"],
    use_scm_version={"write_to": "tsutil/_version.py"},
)
