__config_version__ = 1

{% raw %}
GLOBALS = {
    'serializer': '{{major}}.{{minor}}.{{patch}}',
}
{% endraw %}

FILES = ["setup.py", "{{ cookiecutter.project_slug }}/__init__.py"]

VERSION = ['major', 'minor', 'patch']
