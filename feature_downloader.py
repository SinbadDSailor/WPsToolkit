import requests
from bs4 import BeautifulSoup
import urllib


def feature():

	urladd = input("Unesi URL: ")
	
	url = requests.get(urladd)
	soup = BeautifulSoup(url.content, 'html.parser')
	images = soup.find_all('div', class_="image--dyn-height")


	def img_finder_pc():
		for img in images:
			imgtags = img.find_all('img', class_="image__main")
			for tag in imgtags:
				tags = tag.attrs.get("data-desktop-src")
				data_str = str(tags)
				data = "feature"
				img_name = tag.attrs.get("alt")
				spec_chars="!@#$%^&*()/:; "
				for i in spec_chars:
					updated_name = img_name.replace(i, "-")
				full_link = "https:" + data_str
				if data in data_str:
					filename = str(updated_name) + "-PC" + ".png"
					urllib.request.urlretrieve(full_link, filename)
					print(filename)


	def img_finder_mo():
		for img in images:
			imgtags = img.find_all('img', class_="image__main")
			for tag in imgtags:
				tags = tag.attrs.get("data-mobile-src")
				data_str = str(tags)
				data = "feature"
				img_name = tag.attrs.get("alt")
				spec_chars="!@#$%^&*()/:; "
				for i in spec_chars:
					updated_name = img_name.replace(i, "-")
				full_link = "https:" + data_str
				if data in data_str:
					filename = str(updated_name) + "-MO" + ".png"
					urllib.request.urlretrieve(full_link, filename)
					print(filename)

	img_finder_pc()
	img_finder_mo()
