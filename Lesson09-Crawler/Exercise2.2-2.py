from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://www.imdb.com/title/tt4073790/?ref_=fn_al_tt_1')
link_set = set()
elements = response.html.find('div.credit_summary_item span a ')[0].find('.itemprop')
for element in elements:
    link_set.add(element.text)
print(link_set)