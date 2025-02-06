module "outputdemo"{
    source = "../../../lab101"
    # message = ""
    ami ="ami-0c02fb55956c7d316"
    publicip="202.0.0.0"
    region="us-east-1"
}


    output "printmodule" {
        value = module.outputdemo
    }


