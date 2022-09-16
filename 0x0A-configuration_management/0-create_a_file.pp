# Creates a file /tmp/school with the following requirements:
# File permission is 0744, File owner is www-data, File group is
# www-data, File content "I love Puppet"
file {'/tmp/school':
ensure  => 'file',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}
