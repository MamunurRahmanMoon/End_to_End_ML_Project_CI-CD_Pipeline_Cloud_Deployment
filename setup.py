from setuptools import setup, find_packages


def get_requirements(filepath):
    """This function returns a list of requirements."""
    with open(filepath) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith('#') and not line.startswith('-e')
        ]

setup(
    name="endtoend-ml-project",
    version="0.1",
    author="Md Mamunur Rahman Moon",
    author_email= "mrm.cs.890@gmail.com",
    description="End-to-end ML project",
    long_description="This is a sample end-to-end machine learning project.",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)


