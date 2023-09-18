data "azuread_user" "this" {
  user_principal_name = "nadz.muhd_gmail.com#EXT#@nadzmuhdgmail.onmicrosoft.com"
}
resource "azurerm_role_assignment" "admin" {
  scope                = module.aks.aks_id
  role_definition_name = "Azure Kubernetes Service RBAC Cluster Admin"
  principal_id         = data.azuread_user.this.object_id
}
