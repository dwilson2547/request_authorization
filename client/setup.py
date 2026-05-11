from setuptools import find_packages, setup

setup(
    name="dwilson-request-auth-client",
    version="0.1.0",
    description="Python client for the Request Authorization gRPC service",
    py_modules=["request_auth_client"],
    packages=find_packages(include=["proto", "proto.*"]),
    python_requires=">=3.11",
    install_requires=[
        "grpcio>=1.64.0",
        "protobuf>=5.0.0",
    ],
)
