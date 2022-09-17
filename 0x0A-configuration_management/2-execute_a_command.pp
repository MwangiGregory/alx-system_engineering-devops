-- Kill a process named killmenow using pkill
exec { 'pkill -f killmenow':
  provider => 'shell'
}
