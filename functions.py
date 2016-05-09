#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

# def updateLog():
# 	counter = 0

# 	for current_name in current_names:
# 		log_text = str(datetime.now()) + '\n'
# 		# if any of the current names are not in the dogs_names.json file, rewrite files, send email
# 		if current_name not in dogs_names2:
# 			print 'no match'
# 			log_text += "Updated file with the following URL's:\n"
# 			for link in current_links:
# 				log_text += link + '\n'
# 			# log_text += '----------------------------------'
# 			# log_text += '\n\n\n'
# 			names = ''
# 			for name in current_names:
# 				names += name + '\n'
# 			with open('dogs_names.txt', 'w') as file:
# 				file.write(names)
# 			with open('dogs_data.json', 'w') as file2:
# 				file2.write(json_string.encode('utf-8').strip())
# 			# with open('log.txt', 'a') as file3:
# 			# 	file3.write(log_text)
# 		else:
# 			counter += 1

# 	with open("dogs_names.txt", "r") as dogs_names_file3:
# 		dogs_names3 = dogs_names_file3.readlines()

# 	print counter
# 	print len(dogs_names3)
# 	if counter == len(dogs_names3):
# 		log_text += 'There have not been any new dogs added that meet the specified criteria.\n'

# 	log_text += '----------------------------------\n'
# 	log_text += '\n\n\n'

# 	with open('log.txt', 'a') as file3:
# 		file3.write(log_text)


def build_html(json_string):
	json_string.replace("'", "\'")
	html = '<!DOCTYPE html><html><head><title>New Dogs Available At The Chittenden Humane Society!</title></head><body>'
	html += '<div class="email-wrapper" style="text-align: center; background: #DADADA; font-family: arial; padding= 10px;">'
	json_object = json.loads(json_string)


	for dog in json_object['dogs']:
		html += '<div class="dog" style="margin: 50px auto;">'
		html += '<h1>Name: ' + dog['Name:'] + '</h1>'
		html += '<ul>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Sex: </span>' + dog['Sex:'] + '</li>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Breed: </span>' + dog['Breed:'] + '</li>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Age: </span>' + dog['Age:'] + '</li>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Reason Here: </span>' + dog['Reason Here:'] + '</li>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Arrival Date: </span>' + dog['Arrival Date:'] + '</li>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Energy Level: </span>' + dog['Energy Level:'] + '</li>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Size/Weight: </span>' + dog['Size/Weight:'] + '</li>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Description: </span>' + dog['Description:'] + '</li>'
		html += '<li style="list-style-type: none; margin-bottom: 10px;"><span style="font-weight: bold;">Link: </span><a href="' + dog['Link:'] + '">' + dog['Link:'] + '</a></li>'
		for image in dog["Images:"]:
			html += '<li style="list-style-type: none; margin-bottom: 10px;"><img style="max-width: 100%; height: auto;" src="' + image + '">'
		html += '</ul>'
		html += '</div>'
		html += '<hr>'

	html += '</div>'
	html += '</body></html>'

	return html
