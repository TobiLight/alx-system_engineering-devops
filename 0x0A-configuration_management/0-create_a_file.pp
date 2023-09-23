# Create a File in /tmp directory
# File: 0-create_a_file.pp
# Author: Oluwatobiloba Light

file { 'school':
  ensure  => 'present',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  path    => '/tmp/school',
}
