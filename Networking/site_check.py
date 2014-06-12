#import urllib module
import urllib

#Simply try to get the code from urlopen
print urllib.urlopen("http://www.picsmashup.com").getcode() """Returns 200 if site is live and error codes otherwise
