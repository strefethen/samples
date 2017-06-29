from com.vmware.vcenter.vm_client import Power
...
stub_config = vapiconnect.connect(server,
                                    username,
                                    password,
                                    skip_verification)

# Create Power stub used for making requests
global vm_power_svc
vm_power_svc = Power(stub_config)
