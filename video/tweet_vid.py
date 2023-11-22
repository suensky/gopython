import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_video_url_from_tweet(tweet_url):
    # Setup a headless browser (using Chrome here)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the tweet URL
    driver.get(tweet_url)

    # Let the JavaScript run by waiting for a few seconds
    driver.implicitly_wait(10)

    # Get page source after it's rendered by JS
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Search for video URL; this can change based on Twitter's frontend structure
    video_tag = soup.find('video')
    if video_tag and video_tag.source:
        video_url = video_tag.source['src']
        return video_url
    
    return None

def download_video_from_url(video_url, output_filename):
    response = requests.get(video_url, stream=True)
    response.raise_for_status()

    with open(output_filename, 'wb') as out_file:
        for chunk in response.iter_content(chunk_size=8192):
            out_file.write(chunk)

if __name__ == "__main__":
    tweet_url = input("Enter the tweet URL: ")
    video_url = extract_video_url_from_tweet(tweet_url)
    
    if video_url:
        download_video_from_url(video_url, "downloaded_video.mp4")
        print("Video downloaded successfully!")
    else:
        print("Video URL not found!")
