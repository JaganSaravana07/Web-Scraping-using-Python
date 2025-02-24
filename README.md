# Web Scraping using Python - Booking.com
## Project Overview
This project is a web scraping application that extracts hotel details from [Booking.com](https://www.booking.com/index.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AtbN770GwAIB0gIkOGE5ZTJkOWQtNmNmZi00N2M3LThmYzktMWU5NTk3YzY2Zjk22AIF4AIB&sid=3d09adecee66e77e25fa12ed8bf3511c&aid=304142). It gathers information such as hotel name, price, location, ratings, reviews, and booking links for a specified city and date range. The collected data is then saved as a CSV file in the local directory.
## Objectives
1. **Automate Hotel Data Collection** – Extract key details from Booking.com efficiently.
2. **Flexible Scraping** – Allow users to input a URL and filename for custom searches.
3. **Data Storage** – Save extracted hotel details in a structured CSV format.
4. **Error Handling & Performance** – Implement sleep timers and request headers for smooth scraping.
5. **User-Friendly Execution** – Provide a seamless command-line experience for users.
## Technologies & Libraries Used
- Python 3.x
- BeautifulSoup4 – This is for parsing HTML and extracting hotel details.
- Requests – For sending HTTP requests to Booking.com.
- CSV – To store extracted data in a structured format.
- LXML – For fast and efficient HTML parsing.
## Features & Workflow
1. Users input a Booking.com search URL and specify a file name.
2. The scraper retrieves the webpage and extracts the following details:
   - Hotel Name 🏨
   - Price 💰
   - Location 📍
   - Rating ⭐
   - Review Count 📝
   - Booking Link 🔗
3. The extracted data is stored as a CSV file in the local directory.
4. To simulate human behavior and prevent blocking, the program incorporates random sleep
## Example Output (CSV Format)
`Hotel_Name,Location,Price,Rating,Score,Review,Link
DownTown Arambol - The River Side Hostel,Arambol,"2,878",Superb,9.4,45 reviews,https://www.booking.com/hotel/in/downtown-arambol-the-river-side-hostel.en-gb.html?label=en-in-booking-desktop-SoQWfYhAMBURf0HSQntj1AS652796016141%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-334108349%3Alp9302084%3Ali%3Adec%3Adm&aid=2311236&ucfs=1&arphpl=1&checkin=2025-02-27&checkout=2025-02-28&dest_id=4127&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=f0816bafc3240608&srepoch=1740323936&all_sr_blocks=1287241603_401681623_2_42_0_790191&highlighted_blocks=1287241603_401681623_2_42_0_790191&matching_block_id=1287241603_401681623_2_42_0_790191&sr_pri_blocks=1287241603_401681623_2_42_0_790191_287760&from=searchresults`


## Disclaimer
This project is intended for educational purposes only. Scraping websites without permission may violate the terms of service. You can use responsibly and check Booking.com's scraping policies before deploying.
