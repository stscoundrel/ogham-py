import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ogham",
    version="1.0.0",
    author="stscoundrel",
    description="Convert Ogham inscriptions to latin text & vice versa.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stscoundrel/ogham-py",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)