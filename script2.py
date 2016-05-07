#!/usr/bin/python

from lxml import html
from html2text import html2text
from datetime import datetime
import requests
import urllib2
import json
import smtplib
import credentials

page = requests.get("https://www.chittendenhumane.org/Dogs")
tree = html.fromstring(page.content)

base_url = 'https://www.chittendenhumane.org'
dogs_names2 = []
absolute_details_links2 = []
absolute_details_links3 = []
current_names = []
current_links = []
json_string = '{'
counter = 0
log_text = str(datetime.now()) + '\n'
FROM = credentials.username
TO = [credentials.username2]
SUBJECT = 'New Dogs Available At The Chittenden Humane Society!'
TEXT = ''

with open("criteria.json") as criteria_file:
	criteria_data = json.load(criteria_file)

with open("dogs_data.json") as dogs_data_file:
	dogs_data = json.load(dogs_data_file)

with open("dogs_names.txt", "r") as dogs_names_file:
	dogs_names = dogs_names_file.readlines()

for index in range(len(dogs_names)):
	dogs_names2.append(dogs_names[index].strip('\n'))

relative_details_links = tree.xpath('//div[@style="height:100px; width:100px; background:url(\'/get/files/image/galleries/Heart_to_Heart_Sponsor-0002.png\') center center no-repeat; position:absolute; top:-10px; right:-10px;"]/parent::*/following-sibling::a/@href')

absolute_details_links = [base_url + element for element in relative_details_links]
json_energy = criteria_data["criteria"]["energy_level"]
json_size = criteria_data["criteria"]["size"]

# print absolute_details_links

for link in absolute_details_links:
	for line in html2text(urllib2.urlopen(link).read()).split("\n"):
		# if the text "Energy Level:" exists in the line
		if "Energy Level:" in line:
			energy_level_value = line.split("**")
			energy_level_value = energy_level_value[2].strip().lower()
			energy_level_value = energy_level_value.split(' ')
			energy_level_value = energy_level_value[0].split('-')
			energy_level_value = energy_level_value[0]
			# if the dog's energy level matches what we've specified in our criteria.json file
			if energy_level_value in json_energy:
				absolute_details_links2.append(link)

for link in absolute_details_links2:
	for line in html2text(urllib2.urlopen(link).read()).split("\n"):
		if "Size/Weight:" in line:
			size = line.split("**")
			size = size[2].split("/")
			size = size[0].strip().lower()
			if size in json_size:
				absolute_details_links3.append(link)

print absolute_details_links3

for index, link in enumerate(absolute_details_links3):
	# print link
	page = requests.get(link)
	tree = html.fromstring(page.content)

	# get the images for each dog
	images = tree.xpath('//div[@class="petThumb"]/a/@href')
	images = [base_url + element for element in images]
	images2 = tree.xpath('//div[@class="blog"]/img/@src')
	images2 = [base_url + element for element in images2]
	images = images + images2
	# print images

	json_string += '"dog": {"Images": ['
	for i, image in enumerate(images):
		if i == len(images) - 1:
			# on the last iteration, don't include the comma
			json_string += '"' + image + '"'
		else:
			# all iterations except the last
			json_string += '"' + image + '",'
	json_string += '],'


	# get the name for each dog
	name = tree.xpath('//div[@class="blog"]/h2/text()')
	current_names.append(name[0])

	json_string += '"Name":"' + name[0] + '",'


	# get the keys for each ...
	details_keys = tree.xpath('//div[@class="blogPostContent"]/p[1]/b/text()')
	temp_keys = tree.xpath('//div[@class="blogPostContent"]/p[1]/span/b/text()')
	temp_keys.pop()
	print temp_keys
	details_keys = details_keys + temp_keys
	print details_keys

	# get the values for each ...
	details_values = tree.xpath('//div[@class="blogPostContent"]/p[1]/text()')
	del details_values[6:9]
	del details_values[0]
	details_values = [element.strip() for element in details_values]
	temp_value = tree.xpath('//div[@class="blogPostContent"]/p[1]/span/span/text()')
	details_values = details_values + temp_value
	print details_values

	for i in range(0,len(details_keys)):
		json_string += '"' + details_keys[i] + '":'
		json_string += '"' + details_values[i] + '",'


	# get the description for each dog
	description = tree.xpath('//div[@class="blogPostContent"]/p[2]/text()')

	json_string += '"Description":"' + description[0] + '",'

	current_links.append(link)
	json_string += '"Link":"' + link + '"'

	if index == len(absolute_details_links3) - 1:
		json_string += '}'
	else:
		json_string += '},'


json_string += '}'
print json_string

current_names2 = []
# if any of the current names are not in the dogs_names.json file, rewrite files
for current_name in current_names:
	# print current_name
	# print dogs_names2
	if current_name not in dogs_names2:
		print 'no match'
		names = ''
		for name in current_names:
			names += name + '\n'
		with open('dogs_names.txt', 'w') as file:
			file.write(names)
		with open('dogs_data.json', 'w') as file2:
			file2.write(json_string.encode('utf-8').strip())
		current_names2.append(current_name)
	else:
		counter += 1

with open("dogs_names.txt", "r") as dogs_names_file3:
	dogs_names3 = dogs_names_file3.readlines()

# print counter
# print len(dogs_names3)
# if we looped through all new dogs and none of them are in the dogs_names.json file
if counter == len(dogs_names3):
	log_text += 'There have not been any new dogs added that meet the specified criteria.\n'

for name in current_names2:
	# print name
	# print current_names2
	if name not in current_names2:
		log_text += "Updated file with the following URL's:\n"
		for link in current_links:
			log_text += link + '\n'
	else:
		log_text += 'There have not been any new dogs added that meet the specified criteria.\n'
	break

log_text += '----------------------------------\n'
log_text += '\n'

with open('log.txt', 'a') as file3:
	file3.write(log_text)

# send email
# TEXT = json_string.encode('utf-8').strip()
# message = """\
# From: %s
# To: %s
# Subject: %s

# %s
# """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

# try:
# 	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# 	server.ehlo()
# 	server.login(credentials.username, credentials.password)
# 	server.sendmail(FROM, TO, message)
# 	server.close()
# 	print 'Email sent!'
# except:
# 	print 'Something went wrong...'