import requests
from bs4 import BeautifulSoup

def get_links(query):
    # Function to scrape the web for the top 3 links related to the query
    url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for g in soup.find_all('a'):
        href = g.get('href')
        if href.startswith('/url?q='):
            actual_link = href.split('/url?q=')[1].split('&sa=U&')[0]
            if actual_link.startswith("http"):
                links.append(actual_link)
        if len(links) == 3:
            break

    return links

def main():
    print("Which services are you searching for (enter the number):")
    print("1. Therapy\n2. Neuropsychological Services\n3. Mental Health Counseling\n4. Support groups\n5. Case Management Services")
    choice = input()

    if choice == '1':
        print("Which kind of therapy (enter the number):")
        print("1. Physical therapy\n2. Occupational therapy\n3. Speech therapy")
        therapy_choice = input()
        therapies = ['Physical therapy', 'Occupational therapy', 'Speech therapy']
        query = therapies[int(therapy_choice) - 1] + " for TBI"
    else:
        services = ['Therapy', 'Neuropsychological Services', 'Mental Health Counseling', 'Support groups', 'Case Management Services']
        query = services[int(choice) - 1] + " for TBI"

    links = get_links(query)
    print(f"\nTop 3 links for {query}:")
    for link in links:
        print(link)

if __name__ == '__main__':
    main()