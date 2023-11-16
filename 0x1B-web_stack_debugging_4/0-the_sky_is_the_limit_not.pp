# HTTP Requests -> a WEB Server
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}
# NGINX
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
