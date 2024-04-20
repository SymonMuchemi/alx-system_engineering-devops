# kills a process called killmenow
exec {'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
}
