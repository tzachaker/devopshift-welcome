provider "aws" {
 region = var.region
}

variable "region" {
 default = "us-east-1"
}

# data "aws_ami_ids" "my-privateami" {
#     owners = ["self"]


# }

variable "ami" {
#  default = "ami-0ff8a91507f77f867"
  default ="ami-0ecc0e0d5986a576d"
 }
variable "vm_name" {
 default = "vm-[YOURNAME]"
}

variable "admin_username" {
 default = "admin-user"
}

variable "admin_password" {
 default = "Password123!"
}

variable "vm_size" {
 default = "t2.micro"
}
