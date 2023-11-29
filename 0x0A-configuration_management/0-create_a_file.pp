# A basic Puppet manifest that declares a file resource

file {'/tmp/school':
  content =>'I love Puppet',
  mode    =>'0744',
  group   =>'www-data',
  owner   =>'www-data',
}
