# Kills a process named killmenow
# File: 2-execute_a_command.pp
# Author: Oluwatobiloba Light

exec { 'pkill -f killmenow':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
