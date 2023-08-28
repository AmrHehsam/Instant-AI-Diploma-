from bs4 import BeautifulSoup

file_path = r"E:\AI Diploma\Instant AI Diploma\Instant-AI-Diploma-\Session 10\All subscriptions - YouTube.html"

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with the class "style-scope ytd-channel-name"
div_elements = soup.find_all('div', class_='style-scope ytd-channel-name')

processed_names = set()  # To keep track of processed names

for div_element in div_elements:
    formatted_string = div_element.find('yt-formatted-string')

    if formatted_string:
        text_content = formatted_string.get_text(strip=True)
        if text_content not in processed_names:
            print(f"Text: {text_content}")
            processed_names.add(text_content)
    else:
        print("No yt-formatted-string element found.")
