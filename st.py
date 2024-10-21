from modules import check
check.dependency()
check.check_started()
from colorama import Back,Fore,Style
from modules import banner,control
check.check_update()


PORT = 2525 

while True:
    banner.banner()
    control.run_php_server(PORT)
    try:
        ngrok_domain = "https://epic-koi-sensibly.ngrok-free.app"
        input(f" {Fore.WHITE+Back.RED}Access the app at {ngrok_domain}, press Enter or CTRL+C to exit {Style.RESET_ALL}")

        # input(" "+Fore.WHITE+Back.RED+"If You Want Exit And Turn Off localhost / press enter or CTRL+C "+Style.RESET_ALL)
        control.kill_php_proc()
        exit()
    
    except:
        control.kill_php_proc()
        exit()