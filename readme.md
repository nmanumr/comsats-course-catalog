# COMSATS Course Catalog

## Running Locally

```sh
# install mkdocs and other dependencies
pip install mkdocs Pygments pymdown-extensions

# install our custom plugin mkdocs_course_plugin
cd ./plugins/mkdocs_course_plugin
python setup.py develop

# serve locally
mkdocs serve
```