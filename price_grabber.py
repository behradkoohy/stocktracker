from time import sleep


TIME_TO_PAUSE = 30 #seconds




def main():
	while True:
		sleep(TIME_TO_PAUSE)
		print('30 seconds passed')

if __name__ == '__main__':
	main()