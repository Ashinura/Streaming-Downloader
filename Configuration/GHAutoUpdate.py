import requests
import re
import subprocess
from packaging import version

# GitHub repository URL
repo_owner = 'Ashinura'
repo_name = 'Streaming-Downloader'
api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'



def get_readme_content():
    response = requests.get(f'https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/README.md')
    if response.status_code == 200:
        return response.text
    return None



def get_current_version(readme_content):
    match = re.search(r'Current Version: v(\d+\.\d+\.\d+)', readme_content)
    if match:
        return match.group(1)
    else: 
        match = re.search(r'Current Version: (\d+\.\d+\.\d+)', readme_content)


    if match:
        return match.group(1)   
    else: 
        return None



def github_update():

    from StreamMenu import main_menu
    from time import sleep

    with open('README.md', 'r', encoding='utf-8') as readme_file:
        readme_content = readme_file.read()

    if readme_content:
        current_version = get_current_version(readme_content)

        if current_version:

            response = requests.get(api_url)

            if response.status_code == 200:
                latest_version = response.json()['tag_name']

                if latest_version and version.parse(latest_version) > version.parse(current_version):

                    print(f"\n{api_url}\nNew version available: {latest_version}")
                    
                    update_choice = str(input("Do you want to update ? [y/n]: ")).lower()

                    if update_choice in ['y', 'yes']:

                        try:
                            subprocess.run(['git', 'pull'])

                            new_readme_content = re.sub(r'Current Version: v(\d+\.\d+\.\d+)', f'Current Version: {latest_version}', readme_content)
                            with open('README.md', 'w', encoding='utf-8') as readme_file:
                                readme_file.write(new_readme_content)

                            print("Update completed successfully.")
                            sleep(2)
                            # main_menu()
                        
                        except Exception as err: 
                            print(err)
                            sleep(5)
                            # main_menu()

                    else:
                        print(f"\n{api_url}\nUpdate declined.")
                        sleep(2)
                        # main_menu()
                else:
                    print(f"\n{api_url}\nNo updates available.")
                    sleep(2)
                    # main_menu()
            else:
                print(f"\n{api_url}\nError retrieving information from GitHub.")
                sleep(2)
                # main_menu()
        else:
            print(f"\n{api_url}\nUnable to retrieve current version from README.md .")
            sleep(2)
            # main_menu()
    else:
        print(f"\n{api_url}\nUnable to retrieve content from README.md .")
        sleep(2)
        # main_menu()