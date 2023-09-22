# Using Puppet, create a manifest that kills a process named killmenow (2. Execute a command)

exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
