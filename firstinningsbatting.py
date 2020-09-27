
import os
import csv
from selenium.common.exceptions import NoSuchElementException


def fibat(match_id, driver):
	url='https://www.cricbuzz.com/api/html/cricket-scorecard/{}'.format(match_id)
	driver.get(url)

	# give name of csv file 
	filename = "firstinningsbatsman.csv"
	  
	# open file in write mode 
	f = open(filename, 'w') 
	  
	# creat header in file 
	header = "player,runs,bowls,fours,sixs,strikerate\n"
	  
	# write into the file 
	f.write(header) 

	for t in range(3, 14):
		try:
			player=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[{}]/div[1]".format(str(t))).text
			print(player)
			runs=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[{}]/div[3]".format(str(t))).text
			print(runs)
			bowls=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[{}]/div[4]".format(str(t))).text
			print(bowls)
			fours=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[{}]/div[5]".format(str(t))).text
			print(fours)
			sixs=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[{}]/div[6]".format(str(t))).text
			print(sixs)
			strikerate=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[{}]/div[7]".format(str(t))).text
			print(strikerate)

			f.write(player + "," + runs + "," + bowls + "," + fours + "," + sixs + "," + strikerate + "\n") 

		except NoSuchElementException as exception:
			pass
		
