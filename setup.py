import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="protect_pdfs", # Replace with your own username
    version="0.0.1",
    author="Chaitanya Daphal",
    author_email="Chaitanya.Daphal84@Gmail.com",
    description="A small utility to add password to PDF file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DChaitanya/protect_pdfs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
