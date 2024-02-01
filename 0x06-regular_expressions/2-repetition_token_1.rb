#!/usr/bin/env ruby
# regex that checks if the `hbtn` string has:
# one or no 'b'

puts ARGV[0].scan(/h[b]?tn/).join
