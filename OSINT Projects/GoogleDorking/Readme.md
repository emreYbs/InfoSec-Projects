
### EXAMPLE Google Dorks that you can use with this script:
````intitle:"Webcam" inurl:WebCam.htm````

- **If you need a worksheet related to Essay Writing, for example a Goole Search Operator example can be as follows:**
````inurl:itu.edu.tr filetype:pdf intitle:"Writing"````

### intitle:
The intitle operator is used to specify that the search results must contain a certain word or phrase in the title.

**Syntax:** intitle:keyword

### -site:
-site: operator is another operator in Google Dorking which is used to exclude results from a specific site or domain in your search. 
 The **-site**: operator can be used to exclude irrelevant or untrusted domains from search results, focusing the search on more reliable sources.

**Syntax:** keyword -site:example.com

**Syntax:** Info:example.com
This simple Google search operator will find the information related to a specific domain name.

### Output of a Google Dork search with this script: 
````inurl:zoom.us/j and intext:scheduled for````

<img width="1519" alt="image" src="https://github.com/emreYbs/InfoSec-Projects/assets/59505246/5f0fb417-df58-4a8a-ae85-f249c672b86f">

<img width="1520" alt="image" src="https://github.com/emreYbs/InfoSec-Projects/assets/59505246/c1ec49a5-a558-4561-8629-a7e39f081753">

<img width="656" alt="image" src="https://github.com/emreYbs/InfoSec-Projects/assets/59505246/f5f1c4d2-802a-4cd6-858e-f1911c5bc4b4">

### Some Google Dorks that you can test:
- inurl:8080 intitle:"Dashboard [Jenkins]"
- "index of" "database.sql.zip"
- intitle:"Apache2 Ubuntu Default Page: It works"
- "Index of" inurl:phpmyadmin
- inurl:Dashboard.jspa intext:"Atlassian Jira Project Management Software"
- inurl:app/kibana intext:Loading Kibana
- inurl:_cpanel/forgotpwd
- intitle:”index of” inurl:ftp
- Intitle:”webcamXP 5”’
- (site:facebook.com | site:twitter.com) & intext:"login"
- intitle:”index of” inurl:ftp.*edu
- linux @reddit  (Most of you may already know, but for anyone who doesn't know or use this @ command operator, I'd highly suggest it to narrow down your search for a specific social media site.
- news @reddit  (This operator will work in Google. So the script will give an irrelevant results when you prefer to use it via Bing, but for other searches, Google Dorks can also be used in a similar way in Bing, Yandex, etc to some extent.
- Fact Check @dw.com
- Fransa @eksisozluk

````I could give some more examples but no need because you can get more up to date and working Dorks via exloit.db or various blogs, from different Github repos. You may encounter Google Block and you may also need to be cautious with some sites because while I wrote this script and tested different Dorks, some sites were honepots and some had some malicous code. Since I tested on an updated and protected Windows VM for testing, not an issue for me. Yet, better to be cautious if you use Google Dorks and test sites a lot. Be respectful to the law and fair use of the script````

### I have added some example Google Dorks in the script and in the terminal output when the code is run, it will show few of them to give you an idea. Also provided some good resource for Google dorks in the code by commenting out.

### NOTE: 
- Sometimes, depending on whether you have chosen Bing or the Default search engine Google, and the based on the ecoding settings, you may rarely get an error code like this: ````"UnicodeEncodeError: 'charmap' codec can't encode characters in position 26-29: character maps to <undefined>"````
**Easy to fix but I didn't need since I nearly always use English and encoding can be an issue with some other languages with the current encoding setting in this script.**

- **Sometimes I rerun the script to test Bing and Google search results because Google tend to cencor the results or show some irrelevant results.**
