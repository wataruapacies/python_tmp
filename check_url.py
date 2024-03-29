import scraping_templete
import url_text
import page_txt_to_phone
import edit_csv
from bs4 import BeautifulSoup
from lxml import etree

def delete_blank_list(url_word_list):
    url_word_list = [i for i in url_word_list if i != ""]
    url_word_list = [i for i in url_word_list if i != " "]
    url_word_list = [i for i in url_word_list if i != "　"]
    url_word_list = [i for i in url_word_list if i != "-"]
    return url_word_list

def yukoyuko():
    beautiful_soup = scraping_templete.request_beautiful_soup()
    xpath = "//div[@class='pageTitle']/h1/a"
    for i in range(9999):
        number_str = str(i)
        url = "https://www.yukoyuko.net/" + number_str.zfill(4)
        res = beautiful_soup.return_response(url)
        res_status = str(res.status_code)
        print(url, res_status)
        if res_status.startswith("2"):
            ans = ["","","",""]
            ans[1] = url
            post_code = ""
            address = ""
            try:
                soup = BeautifulSoup(res.text,'html.parser')
                xml = etree.HTML(str(soup))
                company_name = xml.xpath(xpath)[0]
                #print(company_name.text)
                ans[0] = company_name.text
                url_txet = soup.get_text()
                url_word_list = [url_word.strip() for url_word in url_txet.splitlines()]
                word_list = delete_blank_list(url_word_list)
                #print(word_list)
                for i in range(len(word_list)):
                    if word_list[i] == "住所":
                        post_code = word_list[i+1]
                        address = word_list[i+2]
                ans[2] = post_code
                ans[3] = address
            except:
                pass
                #print('err')
            print(ans)
            edit_csv.make_result_file("yukoyuko_log.csv","log",ans)
        scraping_templete.s_random(2)

def kumapon():
    # https://kumapon.jp/shops/17557/deals
    # ここから再開
    beautiful_soup = scraping_templete.request_beautiful_soup()
    xpath1 = "//div[@class='shopinfo']/div[1]/div[2]"
    xpath2 = "//div[@class='shopinfo']/div[2]/div[2]/p[1]"
    xpath3 = "//div[@class='shopinfo']/div[2]/div[2]/p[2]"
    xpath4 = "//div[@class='shopinfo']/div[3]/div[2]"
    xpath5 = "//div[@class='shopinfo']/div[4]/div[2]/a/@href"
    for i in range(99999):
        if i < 17558:
            continue
        number_str = str(i)
        url = "https://kumapon.jp/shops/" + number_str.zfill(5) + "/deals"
        res = beautiful_soup.return_response(url)
        res_status = str(res.status_code)
        ans_list = ["", "", "", "", ""]
        print(url, res_status)
        if res_status.startswith("2"):
            soup = BeautifulSoup(res.text,'html.parser')
            xml = etree.HTML(str(soup))
            try:
                company_name = xml.xpath(xpath1)[0]
                ans_list[0] = company_name.text
            except:
                pass
                #print('err1')
            try:
                post_code = xml.xpath(xpath2)[0]
                ans_list[1] = post_code.text
            except:
                pass
                #print('err2')
            try:
                address = xml.xpath(xpath3)[0]
                ans_list[2] = address.text
            except:
                pass
                #print('err3')
            try:
                phone = xml.xpath(xpath4)[0]
                ans_list[3] = phone.text
            except:
                pass
                #print('err4')
            try:
                link_url = xml.xpath(xpath5)[0]
                ans_list[4] = link_url
            except:
                pass
                #print('err5')
        scraping_templete.s_random(5)
        if ans_list != ["", "", "", "", ""]:
            print(ans_list)
            edit_csv.make_result_file("kumapon_result.csv","result",ans_list)

def ponparemall():
    beautiful_soup = scraping_templete.request_beautiful_soup()
    for i in range(33):
        number_str = str(i+1)
        url = "https://store.ponparemall.com/?pn=" + number_str
        res = beautiful_soup.return_response(url)
        for j in range(30):
            xpath_name = "//div[@id='shopAvenueList']/div[" + str(j+1) + "]/div/div[@class='shopInfo']/h3/a"
            xpath_url = "//div[@id='shopAvenueList']/div[" + str(j+1) + "]/div/div[@class='shopInfo']/h3/a/@href"
            try:
                soup = BeautifulSoup(res.text,'html.parser')
                xml = etree.HTML(str(soup))
                company_name = xml.xpath(xpath_name)[0]
                link_url = xml.xpath(xpath_url)[0]
                line = [company_name.text, link_url]
                edit_csv.make_result_file("ponparemall_log.csv","log",line)
                print(line)
            except:
                print('err')
        scraping_templete.s_random(5)

def ponparemall_result():
    csv_list = edit_csv.read_csv(True,"log","ponparemall_log.csv",False,2)
    beautiful_soup = scraping_templete.request_beautiful_soup()
    for csv_i in csv_list:
        url = csv_i[1] + "profile"
        res = beautiful_soup.return_response(url)
        print(url)
        try:
            soup = BeautifulSoup(res.text,'html.parser')
            xml = etree.HTML(str(soup))
        except:
            print('soupできません')
            continue
        result_list = [csv_i[0],csv_i[1],url,"","","","","",""]
        for j in range(10):
            try:
                xpath = "//div[@class='sectionContentLv2']/table[@class='tblType02']/tbody/tr[" + str(j+1) + "]/th"
                col_name = xml.xpath(xpath)[0]
                if col_name.text == "会社名":
                    xpath_name = "//div[@class='sectionContentLv2']/table[@class='tblType02']/tbody/tr[" + str(j+1) + "]/td"
                    col_name = xml.xpath(xpath_name)[0]
                    print("会社名",col_name.text)
                    result_list[3] = col_name.text
                if col_name.text == "住所":
                    xpath_name = "//div[@class='sectionContentLv2']/table[@class='tblType02']/tbody/tr[" + str(j+1) + "]/td"
                    col_name = xml.xpath(xpath_name)[0]
                    print("郵便番号",col_name.text)
                    result_list[4] = col_name.text
                    xpath_name = "//div[@class='sectionContentLv2']/table[@class='tblType02']/tbody/tr[" + str(j+1) + "]/td/text()"
                    col_name = xml.xpath(xpath_name)
                    print("住所",col_name[1])
                    result_list[5] = col_name[1]
                if col_name.text == "電話番号":
                    xpath_name = "//div[@class='sectionContentLv2']/table[@class='tblType02']/tbody/tr[" + str(j+1) + "]/td"
                    col_name = xml.xpath(xpath_name)[0]
                    print("電話番号",col_name.text)
                    result_list[6] = col_name.text
                if col_name.text == "メールアドレス":
                    xpath_name = "//div[@class='sectionContentLv2']/table[@class='tblType02']/tbody/tr[" + str(j+1) + "]/td"
                    col_name = xml.xpath(xpath_name)[0]
                    mail_raw_text = col_name.text
                    print("メールアドレス",mail_raw_text.strip())
                    result_list[7] = mail_raw_text.strip()
                if col_name.text == "ショップ運営責任者":
                    xpath_name = "//div[@class='sectionContentLv2']/table[@class='tblType02']/tbody/tr[" + str(j+1) + "]/td"
                    col_name = xml.xpath(xpath_name)[0]
                    print("ショップ運営責任者",col_name.text)
                    result_list[8] = col_name.text
                    break
            except:
                continue
        edit_csv.make_result_file("ponparemall_result.csv","result",result_list)
        scraping_templete.s_random(3)

def ponpare_company_url():
    csv_list = edit_csv.read_csv(True,"result","ponparemall_result.csv",False,9)
    beautiful_soup = scraping_templete.request_beautiful_soup()
    xpath = "//div[@class='sw-Card Algo']/section/div/div/div/a/@href"
    i = 0
    for csv_i in csv_list:
        i += 1
        if i < 32:
            continue
        company_name = csv_i[3]
        soup = beautiful_soup.yahoo_soup([company_name,"ホームページ"])
        xml = etree.HTML(str(soup))
        link_url = ""
        try:
            link_url = xml.xpath(xpath)[0]
        except:
            print('err')
            beautiful_soup = scraping_templete.request_beautiful_soup()
        ans = csv_i + [link_url]
        print(ans)
        edit_csv.make_result_file("panpare_company_url_add2.csv","result",ans)
        scraping_templete.s_random(3)
        if i > 35:
            scraping_templete.s_random(10)

def ponpare_comp():
    csv_list = edit_csv.read_csv(True,"result","ponparemall_all_result.csv",False,10)
    beautiful_soup = scraping_templete.request_beautiful_soup()
    # xpath = "//div[@class='sw-Card Algo']/section/div/div/div/a/@href"
    xpath = "//div/section/div/div/div[@class='sw-Card__title']/a/@href"
    i = 0
    for csv_i in csv_list:
        i += 1
        second = False
        company_name = csv_i[3]
        if csv_i[9] == "":
            while True:
                soup = beautiful_soup.yahoo_soup([company_name])
                xml = etree.HTML(str(soup))
                link_url = ""
                try:
                    link_url = xml.xpath(xpath)[0]
                    csv_i[9] = link_url
                    print(i,csv_i)
                    scraping_templete.s_random(1)
                    break
                except:
                    print('err',csv_i)
                    scraping_templete.s_random(3)
                    beautiful_soup = scraping_templete.request_beautiful_soup()
                    if second:
                        break
                    second = True
        edit_csv.make_result_file("panpare_company_comp.csv","result",csv_i)
    
def yukoyuko_comp():
    csv_list = edit_csv.read_csv(True,"log","yukoyuko_log.csv",False,4)
    beautiful_soup = scraping_templete.request_beautiful_soup()
    # xpath = "//div[@class='sw-Card Algo']/section/div/div/div/a/@href"
    xpath = "//div/section/div/div/div[@class='sw-Card__title']/a/@href"
    for i in range(len(csv_list)):
        if i < 2974:
            continue
        company_name = csv_list[i][0]
        soup = beautiful_soup.yahoo_soup([company_name,"TEL"])
        xml = etree.HTML(str(soup))
        link_url = ""
        phone_number = ""
        try:
            link_url = xml.xpath(xpath)[0]
            raw_url_text = url_text.url_to_text(link_url)
            phone_list = page_txt_to_phone.phone_number_new(raw_url_text)
            phone_number = phone_list[0]
        except:
            pass
        if link_url == "":
            scraping_templete.s_random(7)
            beautiful_soup = scraping_templete.request_beautiful_soup()
            soup = beautiful_soup.yahoo_soup([company_name])
            xml = etree.HTML(str(soup))
            try:
                link_url = xml.xpath(xpath)[0]
                raw_url_text = url_text.url_to_text(link_url)
                phone_list = page_txt_to_phone.phone_number_new(raw_url_text)
                phone_number = phone_list[0]
            except:
                pass
        ans = csv_list[i] + [phone_number,link_url]
        print(i,ans)
        edit_csv.make_result_file("yukoyuko_phone_yahoo.csv","log",ans)
        scraping_templete.s_random(5)
            
def yukoyuko_phone_uahoo():
    csv_list = edit_csv.read_csv(True,"log","yukoyuko_phone_yahoo.csv",False,6)
    beautiful_soup = scraping_templete.request_beautiful_soup()
    xpath = "//div[@class='sw-Card Algo']/section/div/div/div/a/@href"
    xpath_2 = "//div/section/div/div/div[@class='sw-Card__title']/a/@href"
    for i in range(len(csv_list)):
        link_url = ""
        phone_number = ""
        if csv_list[i][4] == "":
            print(i,"電話番号格納なし")
            company_name = csv_list[i][0]
            scraping_templete.s_random(2)
            soup = beautiful_soup.yahoo_soup([company_name,"TEL"])
            xml = etree.HTML(str(soup))
            try:
                link_url_list = xml.xpath(xpath)
                print(link_url_list)
                k = 0
                for link_url in link_url_list:
                    k += 1
                    if k > 3:
                        break
                    raw_url_text = url_text.url_to_text(link_url)
                    phone_list = page_txt_to_phone.phone_number_new(raw_url_text)
                    phone_number = phone_list[0]
                    if phone_number != "":
                        csv_list[i][4] = phone_number
                        csv_list[i][5] = link_url
                        break
            except:
                pass
        if csv_list[i][4] == "":
            company_name = csv_list[i][0]
            scraping_templete.s_random(2)
            soup = beautiful_soup.yahoo_soup([company_name])
            xml = etree.HTML(str(soup))
            try:
                link_url_list = xml.xpath(xpath)
                k = 0
                for link_url in link_url_list:
                    k += 1
                    if k > 3:
                        break
                    raw_url_text = url_text.url_to_text(link_url)
                    phone_list = page_txt_to_phone.phone_number_new(raw_url_text)
                    phone_number = phone_list[0]
                    if phone_number != "":
                        csv_list[i][4] = phone_number
                        csv_list[i][5] = link_url
                        break
            except:
                pass
        if csv_list[i][4] == "":
            company_name = csv_list[i][0]
            scraping_templete.s_random(2)
            soup = beautiful_soup.yahoo_soup([company_name,"TEL"])
            xml = etree.HTML(str(soup))
            try:
                link_url_list = xml.xpath(xpath_2)
                k = 0
                for link_url in link_url_list:
                    k += 1
                    if k > 3:
                        break
                    raw_url_text = url_text.url_to_text(link_url)
                    phone_list = page_txt_to_phone.phone_number_new(raw_url_text)
                    phone_number = phone_list[0]
                    if phone_number != "":
                        csv_list[i][4] = phone_number
                        csv_list[i][5] = link_url
                        break
            except:
                pass
        print(i,"/",len(csv_list),csv_list[i])
        edit_csv.make_result_file("yukoyuko_phone_yahoo_new.csv","log",csv_list[i])



if __name__ == "__main__":
    yukoyuko_phone_uahoo()
    #kumapon()