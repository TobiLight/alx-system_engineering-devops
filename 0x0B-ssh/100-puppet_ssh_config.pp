# Puppet script to make changes to ssh config

file { '/etc/ssh/ssh_config':
    ensure => file,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0644',
	content => "
	# This is the ssh client system-wide configuration file.  See
	# ssh_config(5) for more information.  This file provides defaults for
	# users, and the values can be changed in per-user configuration files
	# or on the command line.

	# Configuration data is parsed as follows:
	#  1. command line options
	#  2. user-specific file
	#  3. system-wide file
	# Any configuration value is only changed the first time it is set.
	# Thus, host-specific definitions should be at the beginning of the
	# configuration file, and defaults at the end.

	# Site-wide defaults for some commonly used options.  For a comprehensive
	# list of available options, their meanings and defaults, please see the
	# ssh_config(5) man page.

	Include /etc/ssh/ssh_config.d/*.conf

	Host *
	#   ForwardAgent no
	#   ForwardX11 no
	#   ForwardX11Trusted yes
	#   PasswordAuthentication yes
	#   HostbasedAuthentication no
	#   GSSAPIAuthentication no
	#   GSSAPIDelegateCredentials no
	#   GSSAPIKeyExchange no
	#   GSSAPITrustDNS no
	#   BatchMode no
	#   CheckHostIP yes
	#   AddressFamily any
	#   ConnectTimeout 0
	#   StrictHostKeyChecking ask
	#   IdentityFile ~/.ssh/id_rsa
	#   IdentityFile ~/.ssh/id_dsa
	#   IdentityFile ~/.ssh/id_ecdsa
	#   IdentityFile ~/.ssh/id_ed25519
	#   Port 22
	#   Ciphers aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc
	#   MACs hmac-md5,hmac-sha1,umac-64@openssh.com
	#   EscapeChar ~
	#   Tunnel no
	#   TunnelDevice any:any
	#   PermitLocalCommand no
	#   VisualHostKey no
	#   ProxyCommand ssh -q -W %h:%p gateway.example.com
	#   RekeyLimit 1G 1h
		SendEnv LANG LC_*
		HashKnownHosts yes
		GSSAPIAuthentication yes
	"
  }

  # Configure SSH to use the private key ~/.ssh/school
  file_line { 'ssh_key_file':
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/school',
    match   => '^[\s]*IdentityFile',
    ensure  => present,
    require => File['/etc/ssh/ssh_config'],
  }

  # Configure SSH to refuse password-based authentication
  file_line { 'ssh_password_authentication':
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    match   => '^[\s]*PasswordAuthentication',
    ensure  => present,
    require => File['/etc/ssh/ssh_config'],
  }