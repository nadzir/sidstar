resource "azurerm_container_registry" "acr" {
  name                = local.resource_name
  resource_group_name = local.resource_group_name
  location            = local.location
  sku                 = "Basic"

  admin_enabled = true
}

output "acr_admin_user" {
  value     = azurerm_container_registry.acr.admin_username
  sensitive = true
}

output "acr_admin_password" {
  value     = azurerm_container_registry.acr.admin_password
  sensitive = true
}
