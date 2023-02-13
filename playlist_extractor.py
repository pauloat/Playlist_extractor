from selenium import webdriver
from selenium.webdriver.common.by import By

playlistAddress = '' #copy the playlist address here

browser = webdriver.Firefox()

browser.get(playlistAddress)

elems = browser.find_elements(By.ID, 'video-title')

playlist = []

for i in range(len(elems)):
    playlist.append(elems[i].text)
    
playlistFile = open('./playlist.txt', 'w')

for i in playlist:
    playlistFile.write(i + '\n')
    
playlistFile.close()
browser.close()
