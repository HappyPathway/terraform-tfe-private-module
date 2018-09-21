variable "github_organization" {
  type = "string"
}

variable "repo" {
  type = "string"
}

variable "oauth_token" {
  type = "string"
}

variable "tfe_org" {}

variable "tfe_token" {}

variable "tfe_api" {
  default = "app.terraform.io"
  
}
