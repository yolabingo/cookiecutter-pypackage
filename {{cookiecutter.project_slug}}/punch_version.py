{% set version_list = cookiecutter.version.split('.') %}
major = {{ version_list[0] }}
minor = {{ version_list[1] }}
patch = {{ version_list[2] }}
