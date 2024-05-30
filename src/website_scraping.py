import requests
from bs4 import BeautifulSoup
import pandas as pd
PATH = '/home/er_bim/Indonesia_COE/data/raw/'


def COE_scrape(c: str, 
               y: str, 
               save_file: bool = True,
               return_file: bool = True) -> pd.DataFrame:
    """This function extract a specific country and year of Cup of Excellence (COE) auctions data
    from its official website. The website's homepage URL is defined as the parent_url variable,
    while the specific country and year of auction are specified as c and y arguments rescpectively.
    The function will return the COE Auction Result table.
    The function will also save the COE Competition Result and COE Auction Result tables, and store it
    in the local, the folder directory path is specified outside the function.
    
    Args:
        c (str): Define a country listed in Cup of Excellence
        y (str): Define the year period of Coffee of Excellence award 
        save_file (bool, optional): The tables saved as csv. Defaults to True.
        return_file (bool, optional): Defaults to True.

    Returns:
        pd.DataFrame: The Cup of Excellence auction result table.
    """
    parent_url = 'https://allianceforcoffeeexcellence.org/'
    url = parent_url+c+'-'+y
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    tabs = soup.select('ul.vc_tta-tabs-list')[0]
    tabs_links = tabs.find_all('a')
    relative_links = [t.get("href") for t in tabs_links]
    table_urls = [url + '/' + l for l in relative_links]
    tables_Response = requests.get(table_urls[0])
    tables = pd.read_html(tables_Response.text, header = 0)
    competition_results = tables[0]
    auction_results = tables[1]
    
    if save_file:  
        competition_results.to_csv(PATH+c+'_'+y+'_'+'coffee.csv') 
        auction_results.to_csv(PATH+c+'_'+y+'_'+'auction.csv')  
    
    if return_file:
        return auction_results