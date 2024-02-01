#!/usr/bin/env ruby
# regular expression that matches a 10 digit number
# must contain only numbers

puts ARGV[0].scan(/^[\d]{10}$/).join
