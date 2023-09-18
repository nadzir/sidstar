data "azuread_client_config" "current" {}

resource "azuread_application" "aks" {
  display_name = "${local.resource_name}-aks-application"
  owners       = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal" "aks" {
  application_id               = azuread_application.aks.application_id
  app_role_assignment_required = false
  owners                       = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal_password" "aks" {
  service_principal_id = azuread_service_principal.aks.object_id
}

locals {
  roles = [
    "Network Contributor",
    "AcrPull",
    "AcrPush",
    "Contributor",
    "Azure Kubernetes Service RBAC Cluster Admin"
  ]
}

resource "azurerm_role_assignment" "aks" {
  for_each = { for i in local.roles : i => i }

  scope                = azurerm_resource_group.this.id
  role_definition_name = each.value
  principal_id         = azuread_service_principal.aks.object_id
}
