#!/usr/bin/env ruby
# regex that checks if the `hbtn` string has:
# Zero or more 't's

puts ARGV[0].scan(/hb[t]*n/).join
