# You can use whatever Puppet resource type you want for you fix


exec { 'Fix wordpress site':
  command  => "sudo sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  provider => shell,
}
