#
# (c) 2018 Red Hat, Inc.
#
# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.six import string_types
from ansible.errors import AnsibleFilterError
from datetime import datetime

def normalize_interface_name(name):
    """Return the normalized interface name"""
    if not name:
        return

    def _get_number(name):
        digits = ''
        for char in name:
            if char.isdigit() or char in '/.':
                digits += char
        return digits

    if name.lower().startswith('et'):
        if_type = 'Ethernet'
    elif name.lower().startswith('vl'):
        if_type = 'Vlan'
    elif name.lower().startswith('lo'):
        if_type = 'loopback'
    elif name.lower().startswith('po'):
        if_type = 'port-channel'
    elif name.lower().startswith('nv'):
        if_type = 'nve'
    else:
        if_type = None

    number_list = name.split(' ')
    if len(number_list) == 2:
        number = number_list[-1].strip()
    else:
        number = _get_number(name)

    if if_type:
        proper_interface = if_type + number
    else:
        proper_interface = name

    return proper_interface


def normalize_expire_date(expire):
    proper_expire_date = None
    if expire:
        proper_expire_date = datetime.strptime(expire, "%c").strftime("%Y-%m-%d")
    return proper_expire_date


def strip_roles(roles):
    stripped_roles = None
    if roles:
        stripped_roles = roles.strip()
    return stripped_roles


class FilterModule(object):
    """Filters for working with NXOS device"""

    def filters(self):
        return {
            'normalize_interface_name': normalize_interface_name,
            'normalize_expire_date': normalize_expire_date,
            'strip_roles': strip_roles
        }
