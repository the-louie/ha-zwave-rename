ha-zwave-renamer
=

Small utility to rename a zwave node and all subnodes. Since the built in function has been working sub-optimal since around 0.76 (about a year by now Oct 2019) I built this TINY script to rename a Z-wave node and all subnodes from the commandline.
The feature missing in the UI is accually available in the API, so it was as simple as calling the service "`zwave/rename_node`" with the attribute "`update_ids`".

Please note that this is only confirmed to work on my installation, so if you're not me, test it on a single node before renaming all your stuff.


Usage:
--
`python3 ha-zwave-renamer <node id> <new name>`

*   *node id* is an integer representing the id of the node.
*   *new name* is a string with the new name (doh).
