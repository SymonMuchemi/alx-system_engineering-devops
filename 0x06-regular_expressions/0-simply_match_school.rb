#!/usr/bin/env ruby
# Regular expression that matches `School`

puts ARGV[0].scan(/[a-zA-Z]*School[a-zA-Z]*/).join
