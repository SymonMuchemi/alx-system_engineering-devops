#!/usr/bin/env ruby
# Run statistics on text transactions
# Information is diplayed using the following format:
#   `[SENDER],[RECEIVER],[FLAGS]`
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

sender_phone_number_pattern = /from:([a-zA-Z]+|[+]?[0-9]{11})/
receiver_phone_number_pattern = /to:([a-zA-Z]+|[+]?[0-9]{11})/
flag_pattern = /flags:((0|-1):(0|-1):(0|-1):(0|-1):(0|-1))/

input_log = ARGV[0]

if input_log.nil?
    puts ""
else
    receiver_match = input_log.match(receiver_phone_number_pattern)
    receiver_number = receiver_match[1].sub('to', '')

    sender_match = input_log.match(sender_phone_number_pattern)
    sender_number = sender_match[1].sub('from:', '')

    flag_match = input_log.match(flag_pattern)
    flag = flag_match[1].sub('flags:', '')

    puts "#{sender_number},#{receiver_number},#{flag}"
end
