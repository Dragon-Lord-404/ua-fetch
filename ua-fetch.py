import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def fetch_user_agents(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        user_agents = soup.find_all(text=lambda text: "Mozilla/5.0" in text)
        return user_agents
    else:
        print("Failed to fetch user agent list")
        return []

def main():
    banner = """

    ____  ____  ___   __________  _   __
   / __ \/ __ \/   | / ____/ __ \/ | / /
  / / / / /_/ / /| |/ / __/ / / /  |/ / 
 / /_/ / _, _/ ___ / /_/ / /_/ / /|  /  
/_____/_/ |_/_/  |_\____/\____/_/ |_/   
                                        

    """
    print(banner)
    print("Welcome to the User Agent Fetcher")
    print("Author: FIRDAWS SAPNO")
    print("GitHub: https://github.com/Dragon-Lord-404")
    print("Facebook: https://facebook.com/coderet.d.looper")
    print("WhatsApp: +8801576593082\n")

    url = "https://iplogger.org/useragents/?device=random&count=1000"  # Fixed URL
    save_location = input("Enter the path to save the text file (e.g., /sdcard/filename.txt): ")
    repeat_count = int(input("Enter the number of times to repeat the process: "))

    for repeat in range(repeat_count):
        print(f"\nFetching user agents from {url} (Repeat {repeat + 1}/{repeat_count})")

        # Simulate fetching with an animation
        for _ in tqdm(range(10), desc="Fetching", ascii=True, unit=" pages"):
            time.sleep(0.1)

        user_agents = fetch_user_agents(url)

        if user_agents:
            with open(save_location, "a") as file:
                for user_agent in user_agents:
                    file.write(user_agent + "\n")
            print("\nUser agents saved to", save_location)
        else:
            print("\nNo user agents found")

        # Refresh the website content (at least 2 times) before the next iteration
        for _ in range(2):
            requests.get(url)

if __name__ == "__main__":
    main()
