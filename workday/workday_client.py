from zeep import Client
WSDL = 'https://example.com/workday?wsdl'
client = Client(WSDL)
print('Mock call result:', 'ok')
