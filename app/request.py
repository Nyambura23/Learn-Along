from app import app
import urllib.request,json
from .models import quote

Quote = quote.Quote

# Getting api key
# api_key = app.config['QUOTE_API_KEY']


# Getting the movie base url
base_url = None


def get_quotes(random):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(random)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_results = None

        if get_quotes_response:
 
            quote_results_list = get_quotes_response
            quote_results = process_results(quote_results_list)

    return quote_results

def process_results(quote_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''
    quote_results = []
    for quote_item in quote_list.values():
        author = quote_list.get('author')
        id = quote_list.get('id')
        quote = quote_list.get('quote')
        permalink = quote_list.get('permalink_path')
      
        if permalink:
            quote_object = Quote(author,id,quote,permalink)
            quote_results.append(quote_object)

    return quote_results

def get_quote(id):
    get_quote_details_url = base_url.format(id)

    with urllib.request.urlopen(get_quote_details_url) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)

        quote_object = None
        if quote_details_response:
            author = quote_details_response.get('author')
            id = quote_details_response.get('id')
            quote = quote_details_response.get('quote')
            permalink = quote_details_response.get('permalink_path')

            quote_object = Quote(author,id,quote,permalink)

    return quote_object