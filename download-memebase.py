from bs4 import BeautifulSoup
import urllib
import os
import sys
import requests

dir = os.path.dirname(os.path.abspath(__file__))
memebase = dir +"\\MemebasePics"

if not os.path.exists(memebase):
        os.makedirs(memebase)

#supa za pocetnu
main_url = "http://memebase.cheezburger.com/"
print "Entered Page 1"
r = requests.get(main_url)
data = r.text
supaPocetna = BeautifulSoup(data, "html.parser")
   

for imglink in supaPocetna.findAll("img", {"class" : "resp-media"}):
		mylink =  imglink.get("src")
		current_comic_src = imglink.get("title")
		open_img = urllib.urlopen(mylink)
		img_data = open_img.read()
		filename = current_comic_src
		filename = filename + ".jpg"
		filename = filename.replace(':','')
		filename = filename.replace('?','')
		filename = filename.replace('#','Hashtag')
		path = os.path.join(memebase,filename)
		with open (path,"wb") as data:
			data.write(img_data)
		print "Completed download of image:" + filename

		
		
		
		
#supa za ostale stranice do 10		
for url_range in range(2,11):
	main_url = "http://memebase.cheezburger.com/page/" + str(url_range)
	print "Entered Page " + str(main_url)
	r = requests.get(main_url)
	data = r.text
	supa = BeautifulSoup(data, "html.parser")
   

        for imglink in supa.findAll("img", {"class" : "resp-media"}):
			mylink =  imglink.get("src")
			current_comic_src = imglink.get("title")
			open_img = urllib.urlopen(mylink)
			img_data = open_img.read()
			filename = current_comic_src
			filename = filename + ".jpg"
			filename = filename.replace(':','')
			filename = filename.replace('?','')
			filename = filename.replace('#','Hashtag')
			path = os.path.join(memebase,filename)
			with open (path,"wb") as data:
				data.write(img_data)
			print "Completed download of image:" + filename

   
	
	
    
