import requests
import threading
from termcolor import colored, cprint




logo = f'''
      {colored('.=*#***#*=', 'red')}              
     {colored('+%-      .=%=', 'green')}            
    {colored('*#-         .%=', 'blue')}           
    {colored('@-           +%', 'yellow')}           
    {colored('%+-          #*', 'cyan')}           
    {colored(':%+        .*%.', 'magenta')}           
      {colored('=#*=::-=*#@@*=', 'red')}          
        {colored('.:-=-:. .%*%%+', 'green')}        
                  {colored('=+*%%+', 'blue')}      
                    {colored('=+*%%+', 'yellow')}    
                      {colored('=+@#', 'cyan')}  
            {colored("##############################", 'magenta')}
            {colored("#    User Finder. (2rootv3)   #", 'yellow')}
            {colored("##############################", 'magenta')}
'''


def check_username(site, username):
    fail_messages = [
        "Log in to Facebook",
        "Couldn't find this account",
        "This profile could not be found",
        "Page not found",
        "Sorry!",
        "Oops",
        "404",
        "This page is no longer available",
        "Sorry. Unless you’ve got a time machine, that content is unavailable.",
        "Out of nothing, something",
        "Sorry, nobody on Reddit goes by that name.",
        "Hmm...this page doesn’t exist. Try searching for something else",
        "Sorry, this page isn't available.",
        "Loading failed",      
        
        
    ]
    
    
    try:
        res = requests.get(site, timeout=5)  # Set timeout to 10 seconds
        if res.status_code == 200:
            for fail_msg in fail_messages:
                if fail_msg in res.text:
                    print(colored(f"\n[*] Account not found '{username}' on '{site} '",'red'))
                    break  # Move to the next site on failure
            else:
                if username in res.text:
                    print(colored(f"\n[+] Results for '{username}' on '{site} '",'green'))
                    
                else:
                    print(colored(f"\n[*] Please check it manually '{username}' on '{site} '",'yellow'))
        else:
            print(colored(f"\n[-] Failed to retrieve data from {site}.",'red'))
    
    except requests.RequestException as e:
        # print(f"\n[-] Error accessing {site}: {e}")
        pass


def search_username(username):
    
    hps = 'https://www.'
    
    sites_for_find = [
    hps + 'github.com/' + username,
    hps + 'facebook.com/' + username,
    hps + 'imdb.com/name/' + username,
    'https://en.wikialpha.org/wiki/' + username,
    hps + 'tiktok.com/@' + username,
    hps + 'instagram.com/' + username,
    hps + 'youtube.com/@' + username,
    hps + 'twitter.com/' + username,
    hps + 'filmfreeway.com/' + username,
    hps + username + '.blogspot.com',
    hps + 'mojapp.in/@' + username,
    hps + 'blog.jit.com.bd/author/' + username,
    hps + 'binance.com/en-IN/feed/profile/' + username,
    hps + 'en.everybodywiki.com/' + username,
    hps + 'researchgate.net/profile/' + username,
    hps + 'quora.com/profile/' + username,
    # Add more websites below:
    hps + 'linkedin.com/in/' + username,
    hps + 'reddit.com/user/' + username,
    hps + 'pinterest.com/' + username,
    hps + 'snapchat.com/add/' + username,
    hps + 'medium.com/@' + username,
    hps + 'soundcloud.com/' + username,
    hps + 'gist.github.com/' + username,
    hps + 'behance.net/' + username,
    hps + 'vimeo.com/' + username,
    hps + 'flickr.com/photos/' + username,
    hps + 'dribbble.com/' + username,
    hps + 'stackoverflow.com/users/' + username,
    hps + 'deviantart.com/' + username,
    hps + 'producthunt.com/@' + username,
    hps + 'hackerrank.com/' + username,
    hps + 'twitch.tv/' + username,
    hps + 'discord.com/users/' + username,
    hps + 'angel.co/' + username,
    hps + 'slideshare.net/' + username,
    hps + 'about.me/' + username,
    hps + 'etsy.com/people/' + username,
    hps + 'goodreads.com/user/show/' + username,
    hps + 'last.fm/user/' + username,
    hps + 'mixcloud.com/' + username,
    hps + 'bandcamp.com/' + username,
    hps + 'patreon.com/' + username,
    hps + 'vimeo.com/' + username,
    hps + 'cash.app/$' + username,
    hps + 'discogs.com/users/' + username,
    hps + 'wattpad.com/user/' + username,
    hps + 'fiverr.com/' + username,
    hps + 'tripadvisor.com/members/' + username,
    hps + 'tripit.com/people/' + username,
    hps + 'virustotal.com/ui/users/' + username,
    hps + 'blip.fm/' + username,
    hps + 'codementor.io/' + username,
    hps + 'bitbucket.org/' + username,
    hps + 'hub.docker.com/u/' + username,
    hps + 'keybase.io/' + username,
    hps + 'letterboxd.com/' + username,
    hps + 'scribd.com/' + username,
    hps + 'gumroad.com/' + username,
    hps + 'dribbble.com/' + username,
    hps + 'kaggle.com/' + username,
    hps + 'medium.com/@' + username,
    hps + 'soundcloud.com/' + username,
    hps + 'behance.net/' + username,
    hps + 'ello.co/' + username,
    hps + 'codepen.io/' + username,
    hps + 'dailymotion.com/' + username,
    hps + 'slides.com/' + username,
    hps + 'hubpages.com/@' + username,
    hps + 'steamcommunity.com/id/' + username,
    hps + 'twitch.tv/' + username,
    hps + 'trello.com/' + username,
    hps + 'gravatar.com/' + username,
    hps + 'gitlab.com/' + username,
    hps + 'sourceforge.net/u/' + username,
    hps + 'openstreetmap.org/user/' + username,
    hps + 'freecodecamp.org/' + username,
    hps + 'hackaday.io/' + username,
    hps + 'redbubble.com/people/' + username,
    hps + 'patreon.com/' + username,
    hps + 'ello.co/' + username,
    hps + 'codepen.io/' + username,
    hps + 'dailymotion.com/' + username,
    hps + 'slides.com/' + username,
    hps + 'hubpages.com/@' + username,
    hps + 'khanacademy.org/profile/' + username,
    hps + 'steamcommunity.com/id/' + username,
    hps + 'twitch.tv/' + username,
    hps + 'trello.com/' + username,
    hps + 'gravatar.com/' + username,
    hps + 'gitlab.com/' + username,
    hps + 'sourceforge.net/u/' + username,
    hps + 'openstreetmap.org/user/' + username,
    hps + 'freecodecamp.org/' + username,
    hps + 'hackaday.io/' + username,
    hps + 'redbubble.com/people/' + username,
    hps + 'patreon.com/' + username,

    # Additional websites:
    hps + 'itch.io/profile/' + username,
    hps + 'myanimelist.net/profile/' + username,
    hps + 'dribbble.com/' + username,
    hps + 'behance.net/' + username,
    hps + 'dev.to/' + username,
    hps + 'codecademy.com/profiles/' + username,
    hps + 'uid.me/' + username,
    hps + 'newgrounds.com/' + username,
    hps + 'giphy.com/' + username,
    hps + 'ask.fm/' + username,
    hps + 'crunchyroll.com/' + username,
    hps + 'repl.it/@' + username,
    hps + 'bitly.com/' + username,
    ]

    
    checked_sites = set()  # To keep track of checked sites
    
    threads = []
    
    for site in sites_for_find:
        if site not in checked_sites:
            t = threading.Thread(target=check_username, args=(site, username))
            threads.append(t)
            t.start()                
            checked_sites.add(site)  # Add the site to the checked list
        
        for thread in threads:
            thread.join()
    
if __name__ == "__main__":
    print(logo)
    user_name = input(colored('Enter the username: ','yellow'))
    if user_name:
        try:
            search_username(user_name)
        except KeyboardInterrupt:
            print('Allah Hafez.')