import setuptools

with open("README.md" , "r",encoding="utf-8") as f :
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-ToEnd_MachineLearning_Project"
AUTHOR_USER_NAME = "abdelrahmangaber528"
SRC_REPO = "src"
AUTHOR_EMAIL = "abdelrahman.gaber.hamdy@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Implement for BMW Classification ",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={

    },
    package_dir={"" :"src"},
    packages=setuptools.find_packages(where="src")
)