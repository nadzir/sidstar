resource "azurerm_resource_group" "this" {
  location = local.location
  name     = local.resource_group_name
}

resource "azurerm_network_security_group" "this" {
  location            = local.location
  name                = "${local.resource_name}nsg"
  resource_group_name = local.resource_group_name
}

resource "azurerm_route_table" "this" {
  location            = local.location
  name                = "${local.resource_name}rt"
  resource_group_name = local.resource_group_name
}

module "vnet" {
  source              = "Azure/vnet/azurerm"
  vnet_name           = "${local.resource_name}-vnet"
  resource_group_name = local.resource_group_name
  use_for_each        = false
  address_space       = ["10.0.0.0/16"]
  subnet_prefixes     = ["10.0.1.0/24"]
  subnet_names        = ["${local.resource_name}-aks-subnet"]
  vnet_location       = local.location

  nsg_ids = {
    "${local.resource_name}-aks-subnet" = azurerm_network_security_group.this.id
  }

  route_tables_ids = {
    "${local.resource_name}-aks-subnet" = azurerm_route_table.this.id
  }

  tags = {
    environment = "dev"
  }

}
