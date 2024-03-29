import scraping_templete
from bs4 import BeautifulSoup

def delete_blank(txt):
    return_txt = txt.replace(" ","")
    return_txt = return_txt.replace("　","")
    return_txt = return_txt.replace("\n","")
    return_txt = return_txt.replace("\t","")
    return_txt = return_txt.replace("\v","")
    return_txt = return_txt.replace("\f","")
    return_txt = return_txt.replace("\r","")
    return return_txt

def zenkaku_number_to_hankaku(txt):
    zenkaku = ["０","１","２","３","４","５","６","７","８","９","ー","－","（","）"]
    hankaku = ["0","1","2","3","4","5","6","7","8","9","-","-","(",")"]
    return_txt = ""
    for i in range(len(txt)):
        change_flag = False
        for j in range(len(zenkaku)):
            if txt[i] == zenkaku[j]:
                return_txt += hankaku[j]
                change_flag = True
                break
        if not change_flag:
            return_txt += txt[i]
    return return_txt

def url_to_text(url):
    beautiful_soup = scraping_templete.request_beautiful_soup()
    res = beautiful_soup.return_response(url)
    soup = BeautifulSoup(res.text,'html.parser')
    soup_text = soup.get_text()
    return_text = zenkaku_number_to_hankaku(delete_blank(soup_text))
    #print(return_text)
    return return_text

if __name__ == "__main__":
    url_to_text("https://liquidjumper.com/programming/python/python_new_line_strip_replace")