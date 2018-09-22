# terraform-tfe-private-module
This module will create a private module in Terraform Enterprise. This module uses a null_resource in order to call a Python script
that uses the Terraform Enterprise API to create a private registry module.


## Dependencies
This module requires the following python libraries. 
- requests
- os
- json
- sys


