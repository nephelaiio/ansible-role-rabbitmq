# nephelaiio.rabbitmq

[![Build Status](https://github.com/nephelaiio/ansible-role-rabbitmq/actions/workflows/molecule.yml/badge.svg)](https://github.com/nephelaiio/ansible-role-rabbitmq/actions/wofklows/molecule.yml)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.rabbitmq.vim-blue.svg)](https://galaxy.ansible.com/nephelaiio/rabbitmq/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/rabbitmq) to install and configure rabbitmq

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook

- hosts: servers
  roles:
  - role: rabbitmq
    rabbitmq_package_state: latest

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):

- Ubuntu 24.04
- Ubuntu 22.04
- Debian 13
- Debian 12

You can test the role directly from sources using command `molecule test`

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
