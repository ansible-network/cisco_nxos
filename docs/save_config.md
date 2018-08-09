# Save active configuration to startup
The `save_config` function will save the current active (running) configuration
to the startup configuration. This function is performed regardless of whether
or not the running config and the startup config differ.

## How to save the active configuration
To save the current active configuration to the startup configuration simply
invoke the `save_config` function on the target device. There are no
additional configuration options for this function.

Below is an example of calling the `save_config` function from the playbook.

```
- hosts: nxos

  roles:
    - name: ansible-network.cisco_nxos
      function: save_config
```

## Arguments

None

## Notes
None
