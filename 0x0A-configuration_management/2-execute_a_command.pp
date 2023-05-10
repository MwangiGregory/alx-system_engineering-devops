# Kills a process named killmenow
# Must use pkill
exec {'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
}
