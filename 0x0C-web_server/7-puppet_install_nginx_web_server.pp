# Installs and configures an nginx web server

exec { 'apt-get update':
command  => 'apt-get update',
provider => 'shell',
}
package { 'nginx':
ensure  => installed,
require => Exec['apt-get update'],
}
file {'/var/www/html/index.html':
ensure  => file,
content => 'Hello World!',
}
file {'/var/www/html/redirect_me/':
ensure => directory,
}
exec {'set_redirect':
command  => 'sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://www.github.com/MwangiGregory permanent;" /etc/nginx/sites-available/default',
provider => 'shell',
require  => Package['nginx'],
}
exec {'restart_nginx':
command  => 'service nginx restart',
provider => 'shell',
}
