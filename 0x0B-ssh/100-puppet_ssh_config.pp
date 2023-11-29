#Creates an ssh config file
file { "/home/ubuntu/.ssh":
  ensure  => directory,
}

file {  "/home/ubuntu/.ssh/ssh_config":
  ensure  => file,
  content => @(EOT),
    IdentityFile ~/.ssh/school
    PasswordAuthentication No
  EOT
  mode    => '644'
}

