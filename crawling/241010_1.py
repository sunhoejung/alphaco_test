from bs4 import BeautifulSoup
import requests
import bs4
import pandas as pd
import warnings
warnings.filterwarnings('ignore') 


#1

with open('crawling/index.html', 'r', encoding='UTF8') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    # print(soup)
    print(soup.h2)
    print(soup.ul)
    print(soup.ul.li)

    companies = []
    for tag in soup.find_all('li'):
        companies.append(tag.text)
    print(companies[-1])

#2

    company_code = '005930' # 삼성전자
url ="https://finance.naver.com/item/sise_day.nhn?code=" + company_code

headers = { 
         'referer' : 'https://finance.naver.com/item/sise.naver?code=005930',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

def crawling(soup):
    last_page = int(soup.select_one('td.pgRR').a['href'].split('=')[-1])
    # print(last_page)
    
    df = None
    count = 0
    for page in range(1, last_page + 1):
      req = requests.get(f'{url}&page={page}', headers=headers)
      df = pd.concat([df, pd.read_html(req.text, encoding = "euc-kr")[0]], ignore_index=True)
      if count > 10:
        break
      count += 1
    
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    return df

def main():
    company_code = '005930' # 삼성전자
    url ="https://finance.naver.com/item/sise_day.nhn?code=" + company_code
    
    headers = { 
             'referer' : 'https://finance.naver.com/item/sise.naver?code=005930',
             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    result = crawling(soup)
    print(result)

if __name__ == "__main__":
    main()