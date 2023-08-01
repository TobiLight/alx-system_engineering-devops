#!/usr/bin/env ruby
# Extracts Sender, Receiver and Flags used in text message

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")