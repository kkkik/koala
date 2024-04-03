import requests,webbrowser,time
from time import sleep 
from webbrowser import open
class kny:
	def Create_Ai_Picture(text=None):
		cookies = {'cf_clearance': '9._wgKUAhK7e76OvWrsatn_LEgwYb1Va8ItjbLUHt38-1709007585-1.0-AQQxOjOx1J/j6UtGsJeuYVWqh/FFElu2092ICEOhnpzc9ZcA82bL0UY7ECdqJPYdW1O+Cj4BIw+40y855C2TnMU=','_iidt': 'wo9xc9gOavwmVExu7E5CWMCLwiF3qTI+tXBgilO9HOyVgpyrjvfQEYsoSfQS/KJB1wwZ/ztZ6YDmWg==','_vid_t': 'pfX2YWSD/TcfrlwRbjBONA3rn4wG4eoZsadyV5eEPZn0tsaBE4YrD6b+lMal4C9AIQQX61LFs7QYeg=='}
		headers = {
'authority': 'koala.sh','accept': 'application/json','accept-language': 'ar-EG,ar;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6','content-type': 'application/json','flag-real-time-data': 'true','origin': 'https://koala.sh','referer': 'https://koala.sh/chat?q=/dream','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 14; Aymen_K_n_Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Supported With KNY'}
		json_data = {'input': '/dream ' + text,'inputHistory': [],'outputHistory': [],'model': 'gpt-3.5-turbo'}
		r = requests.post('https://koala.sh/api/gpt/', cookies=cookies, headers=headers, json=json_data)
		if r.status_code == 200:
			x = (r.text).split('(')[1].split(')')[0].strip()
			print(x)
			try:
				print(" Image Saved Succsesfully and will open in Webbrowser after 2 sec!")
				sleep(2.1)
				open(x)
			except:
				pass
			finally:
				exit("im your servant !")
		else:
			print("Failed to get result. Status code:", response.status_code)
kny.Create_Ai_Picture(input("Enter :"))