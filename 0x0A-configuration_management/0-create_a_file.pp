# create a file with the following
# file path - /temp/school
# permission is 0744
# file owner - www-data
# file group - www-data
# content - "I love Pupper"

file { '/temp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'ww-data',
  mode    => '0744'
}
