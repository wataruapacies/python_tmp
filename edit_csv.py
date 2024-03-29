import csv,os

def append_blank(sample_list,n):
    list_len = len(sample_list)
    append_num = n - list_len
    if append_num <= 0:
        return sample_list
    else:
        sample_list += [""] * append_num
        return sample_list

def read_csv(flag,folder_name,file_name,a,number):#ディレクトリ下のCSVを読み込んで１行目以外の２次元配列を返す
    #flagがTrueやったらフォルダ以下のファイルを見る
    # a がTrueで一行目無視
    csv_list = []
    #with open(file_name, 'r', encoding='cp932') as f:
    if flag:
        with open(os.path.join(folder_name,file_name), 'r', encoding='cp932') as f:
            reader = csv.reader(f)
            i = 0
            for line in reader:
                i += 1
                if a and i == 1:
                    continue
                csv_list.append(append_blank(line,number))
    else:
        with open(file_name, 'r', encoding='cp932') as f:
            reader = csv.reader(f)
            i = 0
            for line in reader:
                i += 1
                if a and i == 1:
                    continue
                csv_list.append(append_blank(line,number))
    return csv_list

def make_result_file(name,fold,line):
    try:
        with open(os.path.join(fold,name), "a", encoding="cp932", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(line)
    except:
        print("書き込み失敗","line",line)
        with open(os.path.join(fold,name), "a", encoding="cp932", newline="", errors="ignore") as f:
            writer = csv.writer(f)
            writer.writerow(line)