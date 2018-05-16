import webbrowser
import sys

if len (sys.argv) <= 2 :
    print "Usage: python openbrowser.py word1 word2 "
    sys.exit (1)

arguments = sys.argv[1:]
#url = 'http://www.python.org/'

# Open URL in a new tab, if a browser window is already open.
#webbrowser.open_new_tab(url + 'doc/')

# Open URL in new window, raising the window if possible.
#webbrowser.open_new(url)
#text = request.form['word']

chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
#processed_text = text.lower()
#print (webbrowser.get())
for x in sys.argv[1:]:
	#text = raw_input("Enter word")
	#text = x
	processed_text = x.lower()
	# Open URL in a new tab, if a browser window is already open.
	webbrowser.get(using='chrome').open('https://wordsinasentence.com/'+processed_text+'-in-a-sentence/')

	# Open URL in new window, raising the window if possible.
	webbrowser.get(using='chrome').open('https://mnemonicdictionary.com/?word='+processed_text)

