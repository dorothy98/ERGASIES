import tweepy
from tweepy import OAuthHandler

consumer_key = 'qihQ887wQ0i1lSv9gOednRAyM'
consumer_secret = 'TObHC5q79umPz7WiebcjQQBen4SaSBGqVR4rDJaZYEO8ARhA2j'
access_token = '475125651-nX0EWALsUlOlFXI2m0x30gulf2StJxP9mOpH9ZlX'
access_secret = 'oZNnm2PjeV51PllnoRLqDPumcgaSProTE3K5Jt26MqBgf'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
u1 = raw_input("parakalw dwse to username tou prwtou xrhsth: ")
stuff = api.user_timeline(screen_name = u1, count = 11, include_rts = False)
statuses1 = []
for status1 in stuff:
     s1 = status1.text
     utf8string1 = s1.encode("utf-8")
     wordlist1 = utf8string1.split()
     statuses1 = statuses1 + wordlist1
plithos_lexewn1 = len(statuses1)
u2 = raw_input("parakalw dwse to username tou deuterou xrhsth: ")
stuff = api.user_timeline(screen_name = u2, count = 11, include_rts = False)
statuses2 = []
for status2 in stuff:
     s2 = status2.text
     utf8string2 = s2.encode("utf-8")
     wordlist2 = utf8string2.split()
     statuses2 = statuses2 + wordlist2
plithos_lexewn2 = len(statuses2)
if (plithos_lexewn1 > plithos_lexewn2) == True:
 print "O xrhsths me tis perissoteres lekseis sta teleytaia 10 tweets einai o", u1, "me synolika", plithos_lexewn1, "lekseis,\n enw o xrhsths", u2, "eixe grapsei", plithos_lexewn2, "lekseis."
if (plithos_lexewn1 < plithos_lexewn2) == True:
  print "O xrhsths me tis perissoteres lekseis sta teleytaia 10 tweets einai o", u2, "me synolika", plithos_lexewn2, "lekseis,\n enw o xrhsths", u1, "eixe grapsei", plithos_lexewn1, "lekseis."
if (plithos_lexewn1 == plithos_lexewn2):
 print "Oi dyo xrhstes", u1, "kai", u2,"exoun grapsei twn idio arithmo leksewn (",plithos_lexewn1,") sta teleytaia tous 10 tweets."
