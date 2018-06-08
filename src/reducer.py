#!/usr/bin/env python

import sys


# Store the previous article name
prev_article = None
# Store the current article name
curr_article = None
# Store the 31 daily views details for output
details = [0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,0]
# Store the count of current article
total_count = 0

# Read each line from large data set
for line in sys.stdin:
    # Split each line by tab '\t'
    curr_article, value = line.split("\t")
    # Split value by space ','
    date, count = value.split(",")
    date = int(date)    
    count = int(count)

    # Accumulate count if same article
    if prev_article == curr_article:
        total_count += count
        # Aggregate from hourly views to daily views
        details[date - 1] += count
    # Found a new article
    else:
        # Output the old article info
        if prev_article:
            # Output info if views over 100,000
            if total_count > 100000: 
                extra = ""
                day = 1
                # Fetch the daily views by date
                for view in details:
                    if day < 10:
                        extra += "\t2015080%i:%i" % (day, view)
                    else:
                        extra += "\t201508%i:%i" % (day, view)
                    day += 1
                print "%i\t%s%s" % (total_count, prev_article, extra)
        # Empty the dictionary
        details = [0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,
                   0,0,0,0,0,0,0,0,0,0,0]
        # Initialize count for new article
        total_count = count
        # Initialize buffer for daily views details
        details[date - 1] = count
        # Store old article name
        prev_article = curr_article

# Ouptut the last article info
if total_count > 100000: 
    extra = ""
    day = 1
    for view in details:
        if day < 10:
            extra += "\t2015080%i:%i" % (day, view)
        else:
            extra += "\t201508%i:%i" % (day, view)
        day += 1
    print "%i\t%s%s" % (total_count, prev_article, extra)

