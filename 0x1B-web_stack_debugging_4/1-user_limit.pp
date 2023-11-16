# OS Configuration -> Holberton 
exec {'replace-1':
  provider => shell,
  command  => 'sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace-2'],
}
# NGINX
exec {'replace-2':
  provider => shell,
  command  => 'sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
