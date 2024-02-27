#!/usr/bin/env ruby
# This regular expression will only match strings that have at least one uppercase letter.
puts ARGV[0].scan(/[A-Z]+/).join
