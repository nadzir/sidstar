terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-state-resource-group"
    storage_account_name = "nadterraformstate"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  skip_provider_registration = true
  features {
  }
}
