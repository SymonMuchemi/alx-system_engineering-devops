#!/usr/bin/env ruby
# regex that checks if a string starts with `h` or `n`
# can have any single character in between

puts ARGV[0].scan(/h.n/).join
