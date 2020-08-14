#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver as wb

chromedriver= r"C:\Users\RAKSHITH R M\Downloads\chromedriver_win32\chromedriver.exe"
driver= wb.Chrome(chromedriver)
driver.get('https://webscraper.io/test-sites/e-commerce/static')


# In[2]:


clickObj=driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a')


# In[3]:


clickObj.click()


# In[4]:


driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()


# In[5]:


ll=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div')


# In[6]:


listOflinks=[]
condition=True
while condition:
    productInfoList=driver.find_elements_by_class_name('thumbnail')
    for el in productInfoList:
        ppp1=el.find_elements_by_tag_name('h4')[-1]
        pp2=ppp1.find_element_by_tag_name('a')
        listOflinks.append(pp2.get_property('href'))
    try:
#         webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/ul/li[13]/a').click()
        kk= driver.find_elements_by_class_name('page-link')[-1]
        print (kk.get_attribute('aria-label'))
        if kk.get_attribute('aria-label')== 'Next »':
            kk.click()
        else:
            condition=False            
    except:
        condition=False


# In[7]:


len(listOflinks)


# In[24]:


driver= wb.Chrome(chromedriver)
driver.get(listOflinks[1])


# In[38]:


nameOftheProduct=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]').text
                                               
priceoftheProduct=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text
                                                
descOfProduct=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p').text
                                            
revOfProduct=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p').text
                                           


# In[39]:



tempJ={'nameOftheProduct':nameOftheProduct,
       'priceoftheProduct':priceoftheProduct,
       'descOfProduct':descOfProduct,
       'revOfProduct':revOfProduct
      }


# In[40]:


tempJ


# In[25]:


from tqdm import tqdm
overallinfo=[]
for i in tqdm(listOflinks):
    driver.get(i)
    nameOftheProduct=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]').text
    priceoftheProduct=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text
    descOfProduct=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p').text
    revOfProduct=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p').text
    tempJ={'nameOftheProduct':nameOftheProduct,
          'priceoftheProduct':priceoftheProduct,
          'descOfProduct':descOfProduct,
          'revOfProduct':revOfProduct,
           'hyperlink':i
          }
    overallinfo.append(tempJ)


# In[33]:


import pandas as pd


# In[39]:


df=pd.DataFrame(overallinfo)
print(df.to_string())


# In[ ]:





# In[38]:


writer=pd.ExcelWriter('first.xlsx')
df.to_excel(writer, sheet_name='Sheet1',index=False)
writer.save()
print('data is written')
#df=to_excel(r'F:\Projects\python-web scraping')

