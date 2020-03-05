from setuptools import setup, find_packages

setup(
    name='pytorch-openpose',
    version='0.0.2',
    description='Pure python implementation of openpose',
    author='Hzzone',
    url='https://github.com/rdhislop/pytorch-openpose',
    packages=['pytorch_openpose'],
    install_requires=[
        'numpy',
        'matplotlib',
        'opencv-python',
        'scipy',
        'scikit-image',
        'tqdm',
        'torch',
        'torchvision',
    ]
)