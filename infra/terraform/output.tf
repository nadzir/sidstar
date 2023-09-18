output "service_principal_aks" {
  value     = azuread_service_principal_password.aks
  sensitive = true
}
