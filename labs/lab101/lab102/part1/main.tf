

# data "aws_availability_zones" "available" {
#   state = "available"

#   filter {
#     name   = "yaniv-vm"
#     values = "i-09df7e0ed385f871b"
#   }
# }

# output "public_ip_address" {
#   value = aws_availability_zones.ip_address
#   description = " IP address of the VM"
# }

# -----------
provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

data "aws_instance" "yaniv_vm" {
  instance_id = "i-09df7e0ed385f871b"
}

output "yaniv_vm_public_ip" {
  value = data.aws_instance.yaniv_vm.public_ip
}
