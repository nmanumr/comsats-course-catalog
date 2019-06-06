from setuptools import setup, find_packages

setup(
    name='mkdocs_course_plugin',
    version='0.0.1',
    description="",
    long_description="",
    keywords='mkdocs python markdown wiki',
    author='nmanumr',
    author_email='nmanumr@gmail.com',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs>=1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    entry_points={
        'mkdocs.plugins': [
            'auto-course-plugin = mkdocs_course_plugin.plugin:AutoCoursePlugin'
        ]
    }
)