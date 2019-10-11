import requests
import pyfiglet
import termcolor

ascii = pyfiglet.figlet_format('jokes py', font='isometric2') 
print(termcolor.colored(ascii, color='green'))

while True:
		print(termcolor.colored("You want a joke about what?", color="yellow"))
		term = input()

		url = "https://icanhazdadjoke.com/search"

		response = requests.get(
			url, 
			headers={"Accept": "application/json"},
			params={"term": term}
		).json()
		
		jokes_ = len(response['results'])

		if jokes_ != 0:
			break
		else:
			print(termcolor.colored("No Jokes found for that term, try again...", color="yellow"))

user_input = 1
if jokes_ > 1:
	print(termcolor.colored(f'Found {jokes_} jokes for that, wich one do you want?', color="yellow"))
	user_input = input()

joke = response['results'][int(user_input) - 1]['joke'] 
print(termcolor.colored(joke, color='cyan'))

ascii = pyfiglet.figlet_format('HA HA', font='larry3d') 
print(ascii)