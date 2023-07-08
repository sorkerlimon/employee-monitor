from user_agents import parse
# from browser_history.browsers import Chrome

# f = Chrome()
# outputs = f.fetch_bookmarks()

# # bms is a list of (datetime.datetime, url, title, folder) tuples
# bms = outputs.bookmarks
# for bookmark in bms:
#     url = bookmark[1]
#     print(url)

# from browser_history.browsers import Chrome
# import datetime

# f = Chrome()
# outputs = f.fetch_history()

# # hist is a list of (datetime.datetime, url, title, visit_count) tuples
# hist = outputs.histories

# # Get the last 10 URLs from the history
# last_10_history = hist[-10:]
# bst_offset = datetime.timedelta(hours=6)  # Set the offset for Bangladesh Standard Time (BST)
# for history in last_10_history:
#     url = history[1]
#     timestamp = history[0] + bst_offset
#     formatted_timestamp = timestamp.strftime("%Y-%m-%d %I:%M:%S %p")  # Format the timestamp in 12-hour format
#     print(f"{url} | {formatted_timestamp}")


# workable code

# from browser_history.browsers import Chrome
# import datetime

# f = Chrome()
# outputs = f.fetch_history()

# # hist is a list of (datetime.datetime, url, title, visit_count) tuples
# hist = outputs.histories

# # Get the current date
# current_date = datetime.date.today()

# # Iterate over the history and filter for today's URLs containing Facebook or YouTube
# for history in hist:
#     timestamp = history[0]
#     url = history[1]
#     if timestamp.date() == current_date and ("facebook" in url or "youtube" in url):
#         formatted_timestamp = timestamp.strftime("%Y-%m-%d %I:%M:%S %p")  # Format the timestamp in 12-hour format
#         print(f"{url} | {formatted_timestamp}")

# Facebook youtube history

# from browser_history.browsers import Chrome, Edge
# import datetime

# chrome = Chrome()
# chrome_outputs = chrome.fetch_history()

# edge = Edge()
# edge_outputs = edge.fetch_history()

# # Combine histories from Chrome and Edge
# histories = chrome_outputs.histories + edge_outputs.histories

# # Get the current date
# current_date = datetime.date.today()

# # Iterate over the combined history and filter for today's URLs containing Facebook or YouTube
# for history in histories:
#     timestamp = history[0]
#     url = history[1]
#     if timestamp.date() == current_date and ("facebook" in url or "youtube" in url):
#         formatted_timestamp = timestamp.strftime("%Y-%m-%d %I:%M:%S %p")  # Format the timestamp in 12-hour format
#         print(f"{url} | {formatted_timestamp}")


# facebook youtube percentage with all history

# from browser_history.browsers import Chrome, Firefox, Edge
# import datetime

# chrome = Chrome()
# chrome_outputs = chrome.fetch_history()

# firefox = Firefox()
# firefox_outputs = firefox.fetch_history()

# edge = Edge()
# edge_outputs = edge.fetch_history()

# # Combine histories from Chrome, Firefox, and Edge
# histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories

# # Initialize counters for Facebook and YouTube
# facebook_count = 0
# youtube_count = 0
# current_date = datetime.date.today()
# print('Current Date : ',current_date)
# # Iterate over the combined history and count occurrences of Facebook and YouTube URLs
# for history in histories:
#     url = history[1]
#     timestamp = history[0]
#     if timestamp.date() == current_date and "facebook" in url:
#         facebook_count += 1
#         print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")
#     elif timestamp.date() == current_date and "youtube" in url:
#         youtube_count += 1
#         print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")

# # Calculate the total count and percentages
# total_count = len(histories)
# facebook_percentage = (facebook_count / total_count) * 100
# youtube_percentage = (youtube_count / total_count) * 100

# # Print the percentages
# print(f"Facebook Percentage: {facebook_percentage:.2f}%")
# print(f"YouTube Percentage: {youtube_percentage:.2f}%")



# from browser_history.browsers import Chrome, Firefox, Edge
# import datetime

# chrome = Chrome()
# chrome_outputs = chrome.fetch_history()

# firefox = Firefox()
# firefox_outputs = firefox.fetch_history()

# edge = Edge()
# edge_outputs = edge.fetch_history()

# # Combine histories from Chrome, Firefox, and Edge
# histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories

# # Initialize dictionary to store counts for each domain
# domain_counts = {}

# # Get current date
# current_date = datetime.date.today()
# print('Current Date:', current_date)

# # Iterate over the combined history and count occurrences of each domain
# for history in histories:
#     url = history[1]
#     timestamp = history[0]
#     if timestamp.date() == current_date:
#         domain = url.split('//')[-1].split('/')[0]  # Extract the domain from the URL
#         if domain in domain_counts:
#             domain_counts[domain] += 1
#         else:
#             domain_counts[domain] = 1
#         print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")

# # Calculate the total count
# total_count = sum(domain_counts.values())

# # Calculate the percentage for each domain and print the results
# for domain, count in domain_counts.items():
#     percentage = (count / total_count) * 100
#     print(f"{domain} Percentage: {percentage:.2f}%")



from browser_history.browsers import Chrome, Firefox, Edge
import datetime

chrome = Chrome()
chrome_outputs = chrome.fetch_history()

firefox = Firefox()
firefox_outputs = firefox.fetch_history()

edge = Edge()
edge_outputs = edge.fetch_history()

# Combine histories from Chrome, Firefox, and Edge
histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories

# Initialize dictionary to store counts for each domain
domain_counts = {}

# Get current date
current_date = datetime.date.today()
print('Current Date:', current_date)

# Set the desired time range
start_time = datetime.time(10, 1, 34)  # 11:18:34 AM
end_time = datetime.time(10, 4, 34)    # 11:20:34 AM

# Iterate over the combined history and count occurrences of each domain
for history in histories:
    url = history[1]
    timestamp = history[0]
    if timestamp.date() == current_date and start_time <= timestamp.time() <= end_time:
        domain = url.split('//')[-1].split('/')[0]  # Extract the domain from the URL
        if domain in domain_counts:
            domain_counts[domain] += 1
        else:
            domain_counts[domain] = 1
        print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")

# Calculate the total count
total_count = sum(domain_counts.values())

# Calculate the percentage for each domain and print the results
for domain, count in domain_counts.items():
    percentage = (count / total_count) * 100
    print(f"{domain} Percentage: {percentage:.2f}%")




# single single 
       # Initialize counters for Facebook and YouTube
        # facebook_count = 0
        # youtube_count = 0
        # print("current data : ", current_date)
   


        # # Iterate over the combined history and count occurrences of Facebook and YouTube URLs
        # for history in histories:
        #     url = history[1]
        #     timestamp = history[0]
        #     if timestamp.date() == current_date and "facebook" in url:
        #         facebook_count += 1
        #         print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")
        #     elif  "youtube" in url:
        #         youtube_count += 1
        #         print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")

        # # Calculate the total count and percentages
        # total_count = len(histories)
        # facebook_percentage = (facebook_count / total_count) * 100
        # youtube_percentage = (youtube_count / total_count) * 100

        # # Print the percentages
        # print(f"Facebook Percentage: {facebook_percentage:.2f}%")
        # print(f"YouTube Percentage: {youtube_percentage:.2f}%")
