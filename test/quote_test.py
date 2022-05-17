import unittest
from models import quote
Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote('C. A. R. Hoare',1,'We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.','http://quotes.stormconsultancy.co.uk/quotes/1')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()