data "template_file" "module" {
  template = "${file("${path.module}/module.json.tpl")}"

  vars {
    repo_org       = "${var.github_organization}"
    repo_name      = "${var.repo}"
    oauth_token_id = "${var.oauth_token}"
  }
}

resource "null_resource" "module_publish" {
  provisioner "local-exec" {
    command = "echo '${data.template_file.module.rendered}' > ${path.module}/module.json"
  }
  provisioner "local-exec" {
    command = "python ${path.module}/scripts/module_publish.py --org=${var.tfe_org} --api=${var.tfe_api} --token=${var.tfe_token} --config=${path.module}/module.json"
  }
  provisioner "local-exec" {
    command = "rm ${path.module}/module.json"
  }
}
