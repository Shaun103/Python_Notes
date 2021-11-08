#_________________________________________________________#
# I preorderd this keyboard that is still in development
# so i used this program so that i can quickly see if 
# progress on the shippment of the keyboard has changed 
#_________________________________________________________#

import requests
import bs4
from bs4 import BeautifulSoup

res = requests.get('https://www.pcgamingrace.com/products/glorious-gmmk-pro-75-barebone-black-reservation')
soup = bs4.BeautifulSoup(res.text,"lxml")

print('\n')
print('Glorious GMMKPRO Keyboard launch Information: ')
for item in soup.select('.group-buy-status-content'):  # HTML code to look for change 
    print(item.text)

# Checks to see if the information has changed
if (item.text == 'RESERVATIONS LIVE'):
    print('No shipping change...')
else: 
    print('Change in shipping!')


#_________________________________________________________#
# Users types phrase and the program 
# scraps google and returns the top google response 
#_________________________________________________________#

# from bs4 import BeautifulSoup 
# import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# def google(query):
#     query = query.replace(" ","+")
#     try:
#         url = f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8'
#         res = requests.get(url,headers=headers)
#         soup = BeautifulSoup(res.text,'html.parser')
#     except:
#         print("Make sure you have a internet connection")
#     try:
#         try:
#             ans = soup.select('.RqBzHd')[0].getText().strip()
        
#         except:
#             try:
#                 title=soup.select('.AZCkJd')[0].getText().strip()
#                 try:
#                     ans=soup.select('.e24Kjd')[0].getText().strip()
#                 except:
#                     ans=""
#                 ans=f'{title}\n{ans}'
                
#             except:
#                 try:
#                     ans=soup.select('.hgKElc')[0].getText().strip()
#                 except:
#                     ans=soup.select('.kno-rdesc span')[0].getText().strip()
    
#     except:
#         ans = "can't find on google"
#     return ans

# phrase = 'Spongebob Squarepants'
# result = google(phrase)

# print('\n')
# print(result) 
