# Installs a package
# File: 1-install_a_package.pp
# Author: Oluwatobiloba Light


package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
