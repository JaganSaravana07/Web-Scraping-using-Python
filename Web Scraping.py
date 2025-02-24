import requests
from bs4 import BeautifulSoup
import lxml
import csv
import re
import time

# Booking.com URL
# url = 'https://www.booking.com/searchresults.en-gb.html?ss=Goa%2C+India&efdco=1&label=en-in-booking-desktop-SoQWfYhAMBURf0HSQntj1AS652796016141%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-334108349%3Alp9302084%3Ali%3Adec%3Adm&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=4127&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=fa2b2f27b58c01cb&ac_meta=GhBmYTJiMmYyN2I1OGMwMWNiIAAoATICZW46AmdvQABKAFAA&checkin=2025-02-27&checkout=2025-02-28&group_adults=2&no_rooms=1&group_children=0'

def web_scrapper2(web_url, file_name):
    
    # greetings
    print("Thank you sharing the url and file name!\n⏳\nReading the content!")
    
    
    # processing
    time.sleep(3)

    # Headers to mimic a real browser request
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

    response = requests.get(web_url, headers=header)

    if response.status_code == 200:
        print("Connected to the website")
        html_content = response.text

        # Creating soup object
        soup = BeautifulSoup(html_content, 'lxml')

        # Finding hotel containers
        hotel_divs = soup.find_all('div', role="listitem")

        with open(f"{file_name}.csv", 'w', encoding='utf-8', newline='') as file_csv:
            writer = csv.writer(file_csv)

            # Adding header row
            writer.writerow(['Hotel_Name', 'Location', 'Price', 'Rating', 'Score', 'Review', 'Link'])

            for hotel in hotel_divs:
                # Hotel Name
                hotel_name = hotel.find('div', class_="f6431b446c a15b38c233")
                hotel_name = hotel_name.text.strip() if hotel_name else "NA"

                # Location
                location = hotel.find('span', class_="aee5343fdb def9bc142a")
                location = location.text.strip() if location else "NA"

                # Price
                price = hotel.find('span', class_="f6431b446c fbfd7c1165 e84eb96b1f")
                price = price.text.strip() if price else "NA"
                price = re.sub(r"[^\d,]", "", price)  # Removes all non-numeric characters except commas

                # Rating
                rating = hotel.find('div', class_="a3b8729ab1 e6208ee469 cb2cbb3ccb")
                rating = rating.text.strip() if rating else "NA"

                # Score
                score = hotel.find('div', class_="a3b8729ab1 d86cee9b25")
                score = score.text.strip().split(' ')[-1] if score else "NA"

                # Review Count
                review = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47")
                review = review.text.strip() if review else "NA"

                # Hotel Link
                link = hotel.find('a', href=True)
                link = link.get('href') if link else "NA"

                # Writing row to CSV
                writer.writerow([hotel_name, location, price, rating, score, review, link])

        print("Web Scraping Completed")

    else:
        print(f"Connection Failed! Status Code: {response.status_code}")

    print(response.status_code)

# if using this script directly than below task will be executed
if __name__ == '__main__':

    url = input("Please enter url! :")
    file_name = input('Please give file name! :')

    # calling the function
    web_scrapper2(url, file_name)
