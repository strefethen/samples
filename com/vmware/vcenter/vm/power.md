## Example
Here is an example of calling the power API for a VM.

<pre>
<code class="language-python">
    from com.vmware.vcenter.vm_client import (Power)
    from samples.vsphere.vcenter.helper.vm_helper import get_vm

    vm = get_vm(self.client, self.vm_name)
    if vm:
        # Get the current power state
        state = self.client.vcenter.vm.Power.get(vm)
        if state == Power.Info(state=Power.State.POWERED_ON):
            self.client.vcenter.vm.Power.stop(vm)
        elif state == Power.Info(state=Power.State.SUSPENDED):
            self.client.vcenter.vm.Power.start(vm)
            self.client.vcenter.vm.Power.stop(vm)
</code>
</pre>
