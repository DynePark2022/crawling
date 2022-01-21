import openpyxl


def CreateExcelFile():
    print("File created")
    WB = openpyxl.Workbook()  # 엑셀 파일 생성

    WS = WB.active
    keys = ["title", "image", "image_small", "url", "platform", "publisher", 'genre', "days", "synopsis",
            "original", "age", "latest_episode", "first_episode_url", "category", "author", "run_start", "run_end"]
    WS.append(keys)

    WB.save("test.xls")
    print("File saved")
