#!/usr/bin/python
# -*- coding: utf-8 -*-


{% load kdev_filters %}
{% block license_header %}
{% if license %}
{{ license|lines_prepend:"# "}}
{% endif %}
{% endblock license_header %}


DOCUMENTATION = '''
module: {{ name }}
short_description: Short description.
description:
  - Long description.
options:
  state:
    description:
      - Description of option1
    required: false
    default: "present"
    choices: ["present", "absent"]
    aliases: []
notes:
  - Extra information about the module, such as requirements of the system
requirements: [ python_module_name ]
author: Author Name
'''


EXAMPLES = '''
# Do something
- {{name}}: state=absent
'''


def main():
    module = AnsibleModule(
        argument_spec = dict(
            state=dict(default="present", choices=["absent", "present"]),
        )
    )


    module.exit_json(changed=False)


from ansible.module_utils.basic import *
main()
