from setuptools import setup, find_namespace_packages


setup(
    name='auto-tb-amr-amplicon',
    version='0.1.0',
    packages=find_namespace_packages(),
    entry_points={
        "console_scripts": [
            "auto-tb-amr-amplicon = auto_tb_amr_amplicon.__main__:main",
        ]
    },
    scripts=[],
    package_data={
    },
    install_requires=[
    ],
    description='Automated analysis of targeted amplicon sequencing data for TB AMR and species identification',
    url='https://github.com/BCCDC-PHL/auto-tb-amr-amplicon',
    author='Dan Fornika, Adriana CabreraDelgado',
    author_email='dan.fornika@bccdc.ca, adriana.cabreradelgado@phsa.ca',
    include_package_data=True,
    keywords=[],
    zip_safe=False
)
