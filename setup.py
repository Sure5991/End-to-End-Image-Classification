import setuptools

with open("README.md", "r",encoding = 'utf-8') as f:
    long_description = f.read()

version = '0.0.0'
repo_name = 'End-to-End-Image-Classification'
author_name = 'Sure5991'
src_repo = 'cnn_image_classifier'
author_mail = 'rsuresh5991@gmail.com'

setuptools.setup(
    name=repo_name,
    version=version,
    author=author_name,
    author_email=author_mail,
    description=" small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{author_name}/{repo_name}',
    project_urls={
        "Bug Tracker": f'https://github.com/{author_name}/{repo_name}/issues',
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)