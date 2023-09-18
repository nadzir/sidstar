resource "azurerm_key_vault" "aks" {
  name                        = "${local.resource_name}keyvault"
  location                    = local.location
  resource_group_name         = local.resource_group_name
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false

  sku_name = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    secret_permissions = [
      "List",
      "Get",
      "Set"
    ]
  }

  access_policy {
    tenant_id = azuread_service_principal.aks.application_tenant_id
    object_id = azuread_service_principal.aks.object_id

    secret_permissions = [
      "List",
      "Get",
      "Set"
    ]
  }
}
