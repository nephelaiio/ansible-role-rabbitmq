set allow-duplicate-variables := true

import '.devbox/virtenv/pokerops.ansible-utils.molecule/justfile'

MOLECULE_DOCKER_IMAGE := 'ubuntu2404'
MOLECULE_DOCKER_COMMAND := '/lib/systemd/systemd'
