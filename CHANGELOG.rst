==========================
Ansible Network cisco_nxos
==========================

.. _Ansible Network cisco_nxos_2.6.0:

2.6.0
=====

.. _Ansible Network cisco_nxos_2.6.0_Major Changes:

Major Changes
-------------

- Initial release of the ``cisco_nxos`` Ansible role.

- This role provides functions to perform automation activities on Cisco NX-OS devices.


.. _Ansible Network cisco_nxos_2.6.0_New Functions:

New Functions
-------------

- NEW ``get_facts`` function can be used to collect facts from Cisco NX-OS devices.

- NEW ``config_manager/get`` function returns the either the current active or current saved configuration from Cisco NX-OS devices.

- NEW ``config_manager/load`` function provides a means to load a configuration file onto a target device running Cisco NX-OS.

- NEW ``config_manager/save`` function saves the current active (running) configuration to the startup configuration.

