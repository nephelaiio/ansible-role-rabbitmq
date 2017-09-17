import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rabbitmq(host):
    assert re.match('.molecule_vhost.*)',
                    host.check_output('rabbitmqctl list_vhosts'))
    assert re.match('.molecule_user.*)',
                    host.check_output('rabbitmqctl list_users'))
