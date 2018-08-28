# Load configuration into device
The `load_config` function provides a means to load a configuration file onto a
target device running Cisco NXOS. The `load_config` function provides
configuration values that allow the source configuration to either be merged
with the current active configuration (default) or to replace the current
active configuration on the device.  


## How to load a configuration
Loading a configuration onto a target device is fairly simple and
straightforward.  By default, the `load_config` function will merge the
contents of the provided configuration file with the configuration running on
the target device.  

Below is an example of how to call the `load_config` function.

```
- hosts: nxos
  
  roles:
    - name: ansible-network.cisco_nxos
      function: load_config
      config_file: nxos.cfg
```

The example playbook above will simple load the contents of `nxos.cfg` onto the
target network devices.

### How to load and replace a configuration
The `load_config` function also provides support for replacing the current
configuration on a device. `replace` option is only supported on Cisco NXOS
9K devices.

In order to replace the configuration, the function as before but adds the
value `replace: yes` to the playbook to indicate that the configuration should
be replace and `replace_fs: <destination>` where the file will be placed.

Note: Take caution when doing configuration replace that you do not
inadvertantly replace your access to the device.

```
- hosts: nxos

  roles:
    - name: ansible-network.cisco_nxos
      function: load_config
      config_file: nxos.cfg
      replace: yes
      replace_fs: 'bootflash:'
```

## Arguments

### nxos_config_replace

This value enables or disables the configuration replace feature of the
function. In order to use `nxos_config_replace` the target device must
support config replace function, currently only NXOS 9K device supports
replace.

The default value is `False`

#### Aliases
* replace

### nxos_config_replace_fs

This value provides the directory on the device where the config file will be
pushed during replace.

The default value is `bootflash:`

This value is *required* when `nxos_config_replace is set` to `yes` or `True`.

#### Aliases

* replace_fs

### nxos_config_file

This required value provides the path to the configuration file to load when
the function is called. The path to the file can either be provided as
relative to the playbook root or an absolute path.  

The default value is `null`

This value is *required*

#### Aliases

* config_file

### nxos_config_remove_temp_files

Configures the function to remove or not remove the temp files created when
preparing to load the configuration file. There are two locations for temp
files, one on the Ansible controller and one on the device. This argument
accepts a boolean value.

The default value is `True`

##### Aliases

* remove_temp_files
