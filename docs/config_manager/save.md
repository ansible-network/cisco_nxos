# Save active configuration to startup
The `config_manager/save` function will save the current active (running) configuration
to the startup configuration. This function is performed regardless of whether
or not the running config and the startup config differ.

## How to save the active configuration
To save the current active configuration to the startup configuration simply
invoke the `config_manager/save` function on the target device. There are no
additional configuration options for this function.

Below is an example of calling the `config_manager/save` function from the playbook.

```
- hosts: nxos

  roles:
    - name: ansible-network.cisco_nxos
      function: config_manager/save
```

## Arguments

None

## Notes
None
