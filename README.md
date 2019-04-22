# ansible-role-logrotate #

[![Build Status](https://travis-ci.com/cisagov/ansible-role-logrotate.svg?branch=develop)](https://travis-ci.com/cisagov/ansible-role-logrotate)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-logrotate.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-logrotate/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-logrotate.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-logrotate/context:python)

An Ansible role for installing and configuring
[`logrotate`](https://github.com/logrotate/logrotate).

## Requirements ##

This role uses the `package` Ansible module, so [its
requirements](https://docs.ansible.com/ansible/latest/modules/package_module.html#requirements)
apply.

## Role Variables ##

None.

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - logrotate
```

## Contributing ##

We welcome contributions!  Please see [here](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE.md).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

David Redmin <david.redmin@trio.dhs.gov>
