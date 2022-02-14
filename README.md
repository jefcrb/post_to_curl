# post_to_curl
Simple python script that converts an intercepted POST request from tools such as Burp Suite into a curl command. They say it's good practice to always mimic a request as closely as possible.
(Please not that I'm not very good at this)
# How to use
Simply paste your intercepted POST body into input.txt and execute the script. Make sure input.txt is empty before pasting in new content, that includes deleting the text that's already there. Also make sure that every header is on a new line.
# Example
Example of an intercepted POST request:

![image](https://user-images.githubusercontent.com/83902653/153951378-bcbddfd2-d63f-424a-8378-f949e76d4563.png)

Copy the entire body into input.txt:

![image](https://user-images.githubusercontent.com/83902653/153951939-c6207336-1f6f-4eb4-bd27-045e684f9064.png)

Execute the file and optionally change some of the data if you want:

![image](https://user-images.githubusercontent.com/83902653/153952695-303f0565-1a1a-435d-813d-68b197c285ab.png)
