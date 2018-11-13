==========================
Ansible Network cisco_nxos
==========================

.. _Ansible Network cisco_nxos_v2.7.0:

v2.7.0
======

.. _Ansible Network cisco_nxos_v2.7.0_Major Changes:

Major Changes
-------------

- Initial release of 2.7.0 ``cisco_nxos`` Ansible role that is supported with Ansible 2.7.0


.. _Ansible Network cisco_nxos_v2.7.0_Minor Changes:

Minor Changes
-------------

- Fix config_manager/load function and use cli_config `cisco_nxos#45 <https://github.com/ansible-network/cisco_nxos/pull/45>`_.


.. _Ansible Network cisco_nxos_v2.6.1:

v2.6.1
======

.. _Ansible Network cisco_nxos_v2.6.1_New Tasks:

New Tasks
---------

- Add ``configure_vlans`` task.


.. _Ansible Network cisco_nxos_v2.6.1_Bugfixes:

Bugfixes
--------

- Fix parameters to align with config_manager role `cisco_nxos#34 <https://github.com/ansible-network/cisco_nxos/pull/34>`_.

- validate_role_spec to only consider config_manager_text parameter `cisco_nxos#35 <https://github.com/ansible-network/cisco_nxos/pull/35>`_.


.. _Ansible Network cisco_nxos_v2.6.0:

v2.6.0
======

.. _Ansible Network cisco_nxos_v2.6.0_Major Changes:

Major Changes
-------------

- Initial release of the ``cisco_nxos`` Ansible role.

- This role provides functions to perform automation activities on Cisco NX-OS devices.


.. _Ansible Network cisco_nxos_v2.6.0_New Functions:

New Functions
-------------

- NEW ``get_facts`` function can be used to collect facts from Cisco NX-OS devices.

- NEW ``config_manager/get`` function returns the either the current active or current saved configuration from Cisco NX-OS devices.

- NEW ``config_manager/load`` function provides a means to load a configuration file onto a target device running Cisco NX-OS.

- NEW ``config_manager/save`` function saves the current active (running) configuration to the startup configuration.

