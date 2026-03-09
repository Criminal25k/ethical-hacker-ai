"""
Setup configuration for Ethical Hacker AI
"""

from setuptools import setup, find_packages

setup(
    name='ethical-hacker-ai',
    version='1.0.0',
    description='An AI-powered system for ethical hacking and security research',
    author='Criminal25k',
    author_email='your-email@example.com',
    url='https://github.com/Criminal25k/ethical-hacker-ai',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'torch',
        'transformers',
        'scapy',
        'requests',
        'paramiko',
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)