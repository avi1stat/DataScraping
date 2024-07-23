#Working Script
import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    checkin_date = '2024-08-03'
    checkout_date = '2024-08-04'
    
    page_url = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency=USD&ss=Paris&ssne=Paris&ssne_untouched=Paris&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(page_url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    hotels = soup.find_all('div', {'data-testid': 'property-card'})
    print(f'There are: {len(hotels)} hotels.')
    
    hotels_list = []
    for hotel in hotels:
        hotel_dict = {}
        hotel_dict['hotel'] = hotel.find('div', {'data-testid': 'title'}).get_text(strip=True) if hotel.find('div', {'data-testid': 'title'}) else 'N/A'
        hotel_dict['price'] = hotel.find('span', {'data-testid': 'price-and-discounted-price'}).get_text(strip=True) if hotel.find('span', {'data-testid': 'price-and-discounted-price'}) else 'N/A'
        hotel_dict['score'] = hotel.find('div', {'data-testid': 'review-score'}).find('div').get_text(strip=True) if hotel.find('div', {'data-testid': 'review-score'}) and hotel.find('div', {'data-testid': 'review-score'}).find('div') else 'N/A'
        review_elements = hotel.find('div', {'data-testid': 'review-score'}).find_all('div')[1].find_all('div') if hotel.find('div', {'data-testid': 'review-score'}) else []
        hotel_dict['avg review'] = review_elements[0].get_text(strip=True) if len(review_elements) > 0 else 'N/A'
        hotel_dict['reviews count'] = review_elements[1].get_text(strip=True).split()[0] if len(review_elements) > 1 else 'N/A'
        
        hotels_list.append(hotel_dict)
    
    df = pd.DataFrame(hotels_list)
    df.to_excel('hotels_list.xlsx', index=False) 
    df.to_csv('hotels_list.csv', index=False) 

if __name__ == '__main__':
    main()


#working script with empty data present
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    checkin_date = '2024-08-02'
    checkout_date = '2024-08-03'
    
    page_url = f'https://www.qantas.com/hotels/properties/18482?adults=2&checkIn={checkin_date}&checkOut={checkout_date}&children=0&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash&searchType=list&sortBy=popularity'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(page_url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    hotels = soup.find_all('div', {'data-testid': 'property-card'})
    print(f'There are: {len(hotels)} hotels.')
    
    hotels_list = []
    for hotel in hotels:
        hotel_dict = {}
        hotel_dict['Room_name'] = hotel.select_one('.css-19vc6se-Heading-Heading-Text').get_text(strip=True) if hotel.select_one('.css-19vc6se-Heading-Heading-Text') else 'N/A'
        hotel_dict['Rate_name'] = hotel.select_one('.css-1bjudru').get_text(strip=True) if hotel.select_one('.css-1bjudru') else 'N/A'
        hotel_dict['Number of Guests'] = hotel.select_one('.css-1j7tv8c-Text').get_text(strip=True) if hotel.select_one('.css-1j7tv8c-Text') else 'N/A'
        hotel_dict['Cancellation Policy'] = hotel.select_one('.css-x2p3h8-Text').get_text(strip=True) if hotel.select_one('.css-x2p3h8-Text') else 'N/A'
        hotel_dict['Price'] = hotel.select_one('.css-1bjudru').get_text(strip=True) if hotel.select_one('.css-1bjudru') else 'N/A'
        hotel_dict['Boolean value if the room is a Top Deal'] = hotel.select_one('.css-1qgagpw-Text').get_text(strip=True) if hotel.select_one('.css-1qgagpw-Text') else 'N/A'
        hotel_dict['CCurrency'] = hotel.select_one('.css-1nfdnz8-Text').get_text(strip=True) if hotel.select_one('.css-1nfdnz8-Text') else 'N/A'
        
        hotels_list.append(hotel_dict)
    
    df = pd.DataFrame(hotels_list)
    df.to_excel('hotels_list.xlsx', index=False) 
    df.to_csv('hotels_list.csv', index=False) 

if __name__ == '__main__':
    main()
"""
