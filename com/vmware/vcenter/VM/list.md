### Example
Fetch a summary list of Virtual Machines on the server.

<pre>
<code class="language-python">
client = create_vsphere_client(server=server,
                               username=username,
                               password=password,
                               session=session)

list_of_vms = self.client.vcenter.VM.list()
</code>
</pre>
