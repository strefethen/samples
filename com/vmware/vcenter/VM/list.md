### Example
Fetch a summary list of Virtual Machines on the server.

client = create_vsphere_client(server=server,
                               username=username,
                               password=password,
                               session=session)

list_of_vms = self.client.vcenter.VM.list()
