# Makes changes to the system wide ssh configuration file /etc/ssh/ssh_config
# Adds a rule to prevent password login
# sets default identity file to ~/.ssh/school



exec {'prevent password login':
  command  => '/usr/bin/echo "PasswordAuthentication no" >> /etc/ssh/config',
}

exec {'set default ssh identity file':
  command => '/usr/bin/echo "IdentityFile ~/.ssh/school" >> /etc/ssh/config',
}
