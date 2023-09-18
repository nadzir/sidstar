module "aks" {
  source  = "Azure/aks/azurerm"
  version = "7.3.2"


  prefix              = local.resource_name
  resource_group_name = local.resource_group_name

  kubernetes_version        = "1.26"
  automatic_channel_upgrade = "patch"

  client_id     = azuread_application.aks.application_id
  client_secret = azuread_service_principal_password.aks.value

  agents_availability_zones = ["1", "2"]
  agents_count              = null
  agents_min_count          = 1
  agents_max_count          = 1
  agents_max_pods           = 100
  agents_size               = "Standard_B2s_v2"
  agents_pool_name          = "default"
  agents_type               = "VirtualMachineScaleSets"

  azure_policy_enabled = true

  enable_auto_scaling              = true
  enable_host_encryption           = false
  http_application_routing_enabled = false

  ingress_application_gateway_enabled     = true
  ingress_application_gateway_name        = "${local.resource_name}-agw"
  ingress_application_gateway_subnet_cidr = "10.0.10.0/24"

  local_account_disabled          = true
  log_analytics_workspace_enabled = true

  net_profile_dns_service_ip = "10.10.0.10"
  net_profile_service_cidr   = "10.10.0.0/16"
  network_plugin             = "azure"
  network_policy             = "azure"
  os_disk_size_gb            = 60

  private_cluster_enabled       = false
  public_network_access_enabled = false

  rbac_aad                          = true
  rbac_aad_managed                  = true
  role_based_access_control_enabled = true
  rbac_aad_azure_rbac_enabled       = true

  key_vault_secrets_provider_enabled = true

  sku_tier       = "Standard"
  vnet_subnet_id = module.vnet.vnet_subnets[0]

  oidc_issuer_enabled = true

  agents_labels = {
    "node1" : "label1"
  }
  agents_tags = {
    "Agent" : "agentTag"
  }
  depends_on = [
    module.vnet,
    azuread_application.aks,
    azuread_service_principal_password.aks
  ]
}

