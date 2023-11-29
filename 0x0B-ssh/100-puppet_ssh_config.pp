#Creates an ssh config file
file { "/home/alphonce/.ssh":
  ensure  => directory,
}

file {  "/home/alphonce/.ssh/ssh_config":
  ensure  => file,
  content => @(EOT),
    IdentityFile ~/.ssh/school
    PasswordAuthentication No
  EOT
  mode    => '644'
}

