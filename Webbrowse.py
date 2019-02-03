#! python3
import webbrowser,sys
if len(sys.argv)>1:
   address = ' '.join(sys.argv[1:])
link = 'https://www.google.com/maps/place/' + address
webbrowser.open(link)