import urllib.request,json
from .models import Quote

def get_quotes():
    quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(quote_url) as url:
        data = url.read()
        get_json = json.loads(data)

        if get_json['id'] and get_json['author'] and get_json['quote']:

            id = get_json['id']
            author = get_json['author']
            quote = get_json['quote']

            quote = Quote(author,id,quote)

            return quote
        return None

# def get_quotes(random):

#     get_quotes_url = base_url.format(random)

#     with urllib.request.urlopen(get_quotes_url) as url:
#         get_quotes_data = url.read()
#         get_quotes_response = json.loads(get_quotes_data)

#         quote_results = None

#         if get_quotes_response:
 
#             quote_results_list = get_quotes_response
#             quote_results = process_results(quote_results_list)

#     return quote_results

# def process_results(quote_list):

#     quote_results = []
#     for quote_item in quote_list.values():
#         author = quote_list.get('author')
#         id = quote_list.get('id')
#         quote = quote_list.get('quote')
#         permalink = quote_list.get('permalink_path')
      
#         if permalink:
#             quote_object = Quote(author,id,quote,permalink)
#             quote_results.append(quote_object)

#     return quote_results

# def get_quote(id):
#     get_quote_details_url = base_url.format(id)

#     with urllib.request.urlopen(get_quote_details_url) as url:
#         quote_details_data = url.read()
#         quote_details_response = json.loads(quote_details_data)

#         quote_object = None
#         if quote_details_response:
#             author = quote_details_response.get('author')
#             id = quote_details_response.get('id')
#             quote = quote_details_response.get('quote')
#             permalink = quote_details_response.get('permalink_path')

#             quote_object = Quote(author,id,quote,permalink)

#     return quote_object