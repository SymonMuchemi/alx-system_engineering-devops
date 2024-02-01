#!/usr/bin/env ruby
# regex that checks if the `hbtn` string has more than 2 but less than 4 't's  

puts ARGV[0].scan(/hb[t]{2,4}n/).join
