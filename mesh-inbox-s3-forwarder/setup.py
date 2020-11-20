from setuptools import find_packages, setup

setup(
    name="mesh-inbox-s3-forwarder",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["boto3~=1.16"],
    entry_points={
        "console_scripts": [
            "forward-mesh-inbox-to-s3=main:main",
        ]
    },
)
