#13.01.2024
import colorama,wget
print("""
╭━━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━━━┳━━━╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭━╮┃╭━╮┃
╰╯┃┃┣┻━┳━┳╮╭┳┳━╮╭━━┫┃┃┃╱┃┃╰━━╮
╱╱┃┃┃┃━┫╭┫╰╯┣┫╭╮┫╭╮┃┃┃┃╱┃┣━━╮┃
╱╱┃┃┃┃━┫┃┃┃┃┃┃┃┃┃╭╮┃╰┫╰━╯┃╰━╯┃
╱╱╰╯╰━━┻╯╰┻┻┻┻╯╰┻╯╰┻━┻━━━┻━━━╯""")
try:
	while True:
		colors = colorama.Fore.GREEN
		cmd = input(colors+"user@root$")
		if cmd.startswith("print "):
	  	 	nw = cmd.replace("print ","")
	   		print(nw)
		if cmd.startswith("dffw "):
			nw = cmd.replace("dffw ","")   
			wget.download(nw)	
		if cmd.startswith("info "):
			nw = cmd.replace("info ","")
			if nw == "osname":
				print("OS:TerminalOS")
			elif nw == "version":
				print("Version:v1")
			elif nw == "creator":
				print("Creator:TechGamingGeek")
		
			
except:
	print(colorama.Fore.RED+"ERROR:404")