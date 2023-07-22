import requests #module for making request to a webpage
import threading #module for multi-threading
import argparse #module for parsing command line arguments
#Fancy banner :p
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
logo = ("""
\033[38;5;46m .d8888b.  8888888888 888b    888        d8888 Y88b   d88P 8888888888 888      
\033[38;5;46md88P  Y88b 888        8888b   888       d88888  Y88b d88P  888        888      
\033[38;5;46mY88b.      888        88888b  888      d88P888   Y88o88P   888        888      
\033[38;5;46m "Y888b.   8888888    888Y88b 888     d88P 888    Y888P    8888888    888      
\033[38;5;46m    "Y88b. 888        888 Y88b888    d88P  888     888     888        888      
\033[38;5;46m      "888 888        888  Y88888   d88P   888     888     888        888      
\033[38;5;46mY88b  d88P 888        888   Y8888  d8888888888     888     888        888      
\033[38;5;46m "Y8888P"  8888888888 888    Y888 d88P     888     888     8888888888 88888888 
         
 \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mCREATED BY\033[38;5;196m   :  \033[38;5;195mSENAYEL ISLAM (DIP)   \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mFACEBOK      \033[38;5;196m: \033[38;5;195m SENAYE ISLAM          \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mGITHUB       \033[38;5;196m:  \033[38;5;195mMAGIC-DIP..           \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mTOOL STATUS  \033[38;5;196m: \033[38;5;195m Random Cloning BD     \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mTEAM         \033[38;5;196m:  \033[38;5;195mKGF                   \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mTOOL VIRSION \033[38;5;196m:  \033[38;5;195mMAX                   \033[38;5;46m|
 \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××
 \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m PLZ SAPPORT ME BRO....
 \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m SENAYEL TERMUX HELPING ZONE....
 \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××""")
    
ab = input("\033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195menter you domain without https , www : ")

target = target.replace('http://', '') #and http:// from the url
target = target.replace('/', '') #removes / from url so we can have example.com and not example.com/
target = 'http://' + target #adds http:// before url so we have a perfect URL now
if args.prefix != None:
    target = target + args.prefix
try:
    r = requests.get(target + '/robots.txt') #Requests to example.com/robots.txt
    if '<html>' in r.text: #if there's an html error page then its not robots.txt
        print ('  \033[1;31m[-]\033[1;m Robots.txt not found\n')
    else: #else we got robots.txt
        print ('  \033[1;32m[+]\033[0m Robots.txt found. Check for any interesting entry\n')
        print (r.text)
except: #if this request fails, we are getting robots.txt
    print ('  \033[1;31m[-]\033[1;m Robots.txt not found\n')
print ('\033[1;93m ×××××××××××××××××××××××××××××××××××××××××××××××××\n')

def scan(links):
    for link in links: #fetches one link from the links list
        link = target + link # Does this--> example.com/admin/
        r = requests.get(link) #Requests to the combined url
        http = r.status_code #Fetches the http response code
        if http == 200: #if its 200 the url points to valid resource i.e. admin panel
            print ('  \033[1;32m[+]\033[0m Admin panel found: %s'% link)
        elif http == 404: #404 means not found
            print ('  \033[1;31m[-]\033[1;m %s'% link)
        elif http == 302: #302 means redirection
            print ('  \033[1;32m[+]\033[0m Potential EAR vulnerability found : ' + link)
        else:
            print ('  \033[1;31m[-]\033[1;m %s'% link)
paths = [] #list of paths
def get_paths(type):
    try:
        with open('paths.txt','r') as wordlist: #opens paths.txt and grabs links according to the type arguemnt
            for path in wordlist: #too boring to describe
                path = str(path.replace("\n",""))
                try:
                    if 'asp' in type:
                        if 'html' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'php' in type:
                        if 'asp' in path or 'html' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'html' in type:
                        if 'asp' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                except:
                    paths.append(path)
    except IOError:
        print ('\033[1;31m[-]\033[1;m Wordlist not found!')
        quit()

if args.fast == True: #if the user has supplied --fast argument
    type = args.type #gets the input from --type argument
    get_paths(type) #tells the link grabber to grab links according to user input like php, html, asp
    paths1 = paths[:len(paths)/2] #The path/links list gets
    paths2 = paths[len(paths)/2:] #divided into two lists
    def part1():
        links = paths1 #it is the first part of the list
        scan(links) #calls the scanner
    def part2():
        links = paths2 #it is the second part of the list
        scan(links) #calls the scanner
    t1 = threading.Thread(target=part1) #Calls the part1 function via a thread
    t2 = threading.Thread(target=part2) #Calls the part2 function via a thread
    t1.start() #starts thread 1
    t2.start() #starts thread 2
    t1.join() #Joins both
    t2.join() #of the threads
else: #if --fast isn't supplied we go without threads
    type = args.type
    get_paths(type)
    links = paths
    scan(links)
