## SIAE Microelettronica ALFOplus Devices Nagios Check

This Nagios/Icinga Check provides the ability to query SIAE Microelettronica ALFOplus devices for status and parameters. It will output performance data to monitor reception quality and errors for tools like pnp4nagios.
Implementation is in Python. You will need Python libraries nagiosplugin and pysnmp as dependencies.

You need to add a SNMPv2 user on the SIAE device with SNMP read permissions. The name of this user is the SNMP read community. 

### Installation (manual using pip) on your Nagios Host
```
pip install nagiosplugin pysnmp
python setup.py install
ln -s /usr/bin/check_siae /usr/lib/nagios/plugins/check_siae
```

### Installation Debian package

For Debian you can use the provided Debian package. Debian Jessie should be fine without any additional packages. 


### Usage example

Nagios Plugin called manually:

```
./check_siae -H 1.2.3.4 -C public
```

See check_siae -h for additional command line arguments. Use -vvv to get Debug Output including serial, station ID, firmware data and additional information.


### Using a config file

You can use a config file to change ranges of the warning and critical value ranges for the different monitored devices. The config is expected to be named /etc/check_siae.conf.
Use the command line Switch --config (-c) to override this behaviour.

The config file must contain sections named after the specified hostname/hostaddress of the device (parameter -H) of the check_siae call. You can list the changed parameters within this section. Non present value will take over the defaults. Example (all values are the default values):

/etc/check_siae.conf
```
[1.2.3.4]
tx_data_rate_min = 1318182
tx_data_rate_max = 1318182

rx_data_rate_min = 1318182
rx_data_rate_max = 1318182

rx_power_min_warn = -55
rx_power_min_crit = -60
```


### Nagios Integration

Define the commands for Nagios checks and include it in the service definitions:

```
define command {
	command_name	check_siae
	command_line	/usr/lib/nagios/plugins/check_siae -C $ARG1$ -H $HOSTADDRESS$
}
define service {
	use			generic-service-perfdata
	hostgroup_name		siae
	service_description	check_siae
	check_command		check_siae!SNMP_COMMUNITY
}
```

### PNP4Nagios

A pnp4nagios template is provided in the pnp4nagios directory. For debian installations, it is installed in /usr/share/check_siae/check_siae.php and must be symlinked to the pnp4nagios templates directory (e.g. /etc/pnp4nagios/templates/):

```
ln -s /usr/share/check_siae/check_siae.php /etc/pnp4nagios/templates/check_siae.php
```
