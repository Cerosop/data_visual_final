import time
from google_images_download import google_images_download
import sqlite3 as lite
import os

def download_images(query):
    response = google_images_download.googleimagesdownload()

    arguments = {"keywords": query,
                 "limit": 1,
                 "print_urls": False,
                 "output_directory": "C:/Users/hsu/Desktop/3u/資料視覺化/final/templates/images/head",
                 "prefix": query,
                 "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    paths = response.download(arguments)
    time.sleep(2)  # 添加 2 秒的延遲

    if paths:
        return paths[0][query]
    else:
        return None


def check_directory_permission(directory_path):
    if os.path.exists(directory_path):
        if os.access(directory_path, os.W_OK):
            print(f"The directory '{directory_path}' exists and has write permissions.")
        else:
            print(f"The directory '{directory_path}' exists, but does not have write permissions.")
    else:
        print(f"The directory '{directory_path}' does not exist.")


def main():
    # 指定要檢查的目錄路徑
    directory_to_check = "C:/Users/hsu/Desktop/3u/資料視覺化/final/templates/images/head"  # 替換成實際路徑
    # 調用函數檢查權限
    check_directory_permission(directory_to_check)
        
    con = lite.connect('mydb.db')
    limit = 10
    res = {}
    with con:
        cur=con.cursor()
        for y in range(2022, 2023):
            cur.execute(f"select name from data where year = {y} limit {limit}")
            con.commit()
            data = cur.fetchall()
        for d in data:
            search_query = d[0]
            download_path = download_images(search_query)

            if download_path:
                print(d[0] + "圖片下載成功！保存在:", download_path)
            else:
                print(d[0] + "無法下載圖片。")

if __name__ == "__main__":
    main()
    # 無法下載
