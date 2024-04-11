from setuptools import setup

package_name = 'fleet_adapter_template'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['config.yaml']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='SoftBank Corp.',
    maintainer_email='SBGRP-git@g.softbank.co.jp',
    description='A template for an RMF fleet adapter',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fleet_adapter=fleet_adapter_template.fleet_adapter:main'
        ],
    },
)
