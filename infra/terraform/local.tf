data "azurerm_client_config" "current" {}
locals {
  location            = "Southeast Asia"
  resource_group_name = "thales"
  resource_name       = "thales"
}
