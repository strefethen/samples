vm_name = testbed.config['VM_NAME_DEFAULT']
server, username, password, cleardata, skip_verification, vm_name = \
    parse_cli_args_vm(testbed.config['VM_NAME_DEFAULT'])
stub_config = vapiconnect.connect(server,
                                    username,
                                    password,
                                    skip_verification)
atexit.register(vapiconnect.logout, stub_config)

global vm
vm = get_vm(stub_config, vm_name)
if not vm:
    raise Exception('Sample requires an existing vm with name ({}).'
                    'Please create the vm first.'.format(vm_name))

# Create Power stub used for making requests
global vm_power_svc
vm_power_svc = Power(stub_config)

# Get the vm power state
print('\n# Example: Get current vm power state')
status = vm_power_svc.get(vm)
