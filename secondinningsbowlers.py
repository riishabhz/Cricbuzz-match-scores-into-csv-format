
import os
import csv
from selenium.common.exceptions import NoSuchElementException

def secbowl(match_id, driver):

	url='https://www.cricbuzz.com/api/html/cricket-scorecard/{}'.format(match_id)
	driver.get(url)

	# give name of csv file 
	filename = "secondinningsbowlers.csv"
	  
	# open file in write mode 
	f = open(filename, 'w') 
	  
	# creat header in file 
	header = "player,overs,maiden,run,wickets,noball,wide,economy\n"
	  
	# write into the file 
	f.write(header) 

	for t in range(2, 8):
		try:
			player=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[{}]/div[1]".format(str(t))).text
			print(player)
			overs=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[{}]/div[2]".format(str(t))).text
			print(overs)
			maiden=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[{}]/div[3]".format(str(t))).text
			print(maiden)
			run=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[{}]/div[4]".format(str(t))).text
			print(run)
			wickets=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[{}]/div[5]".format(str(t))).text
			print(wickets)
			noball=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[{}]/div[6]".format(str(t))).text
			print(noball)
			wide=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[{}]/div[7]".format(str(t))).text
			print(wide)
			economy=driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[{}]/div[8]".format(str(t))).text
			print(economy)
			

			f.write(player + "," + overs + "," + maiden + "," + run + "," + wickets + "," + noball + "," + wide + "," + economy + "\n") 

		except NoSuchElementException as exception:
			pass