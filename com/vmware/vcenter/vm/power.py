vm_name = testbed.config['VM_NAME_DEFAULT']
server, username, password, cleardata, skip_verification, vm_name = \
    parse_cli_args_vm(testbed.config['VM_NAME_DEFAULT'])
stub_config = vapiconnect.connect(server,
                                    username,
                                    password,
                                    skip_verification)

# Create Power stub used for making requests
global vm_power_svc
vm_power_svc = Power(stub_config)
