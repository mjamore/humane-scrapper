

def updateLog():
	counter = 0

	for current_name in current_names:
		log_text = str(datetime.now()) + '\n'
		# if any of the current names are not in the dogs_names.json file, rewrite files, send email
		if current_name not in dogs_names2:
			print 'no match'
			log_text += "Updated file with the following URL's:\n"
			for link in current_links:
				log_text += link + '\n'
			# log_text += '----------------------------------'
			# log_text += '\n\n\n'
			names = ''
			for name in current_names:
				names += name + '\n'
			with open('dogs_names.txt', 'w') as file:
				file.write(names)
			with open('dogs_data.json', 'w') as file2:
				file2.write(json_string.encode('utf-8').strip())
			# with open('log.txt', 'a') as file3:
			# 	file3.write(log_text)
		else:
			counter += 1

	with open("dogs_names.txt", "r") as dogs_names_file3:
		dogs_names3 = dogs_names_file3.readlines()

	print counter
	print len(dogs_names3)
	if counter == len(dogs_names3):
		log_text += 'There have not been any new dogs added that meet the specified criteria.\n'

	log_text += '----------------------------------\n'
	log_text += '\n\n\n'

	with open('log.txt', 'a') as file3:
		file3.write(log_text)