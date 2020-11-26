import json

with open("roku.sitemap.txt", "r") as sitemap_txt:
    cnt_da_lp = 0
    with open(f"ROKU_SITEMAP_CSV_RESULT\\roku_csv.csv", "x") as sitemap_csv:
        sitemap_csv.write("channelId,name,starRating,starRatingCount,description,developer,developerUserId"
                          ",publishedDate,createdDate,modifiedDate,storeId")
        while True:
            sitemap_csv.write("\n")
            readlin = sitemap_txt.readline()
            cnt_da_lp += 1
            #     if cnt_da_lp >= 18193:
            if readlin == "":
                break
            with open(f"ROKU_SITEMAP_JSON\\{readlin[59:-24]}.json", "r") as test_json:
                sv = test_json.read()
                if "\\" in sv:
                    sv = sv.replace("\\", "/")
                if cnt_da_lp > 780:
                    if '//","k' in sv:
                        sv = sv.replace('//","k', '","k')
                    if '//","h' in sv:
                        sv = sv.replace('//","h', '","h')
                    if '//"' in sv:
                        sv = sv.replace('//"', "//")
                # print(sv)
                test_json.close()
            with open(f"ROKU_SITEMAP_JSON\\{readlin[59:-24]}.json", "w") as json_write:
                json_write.truncate()
                json_write.write(str(sv))
                json_write.close()

            with open(f"ROKU_SITEMAP_JSON\\{readlin[59:-24]}.json", "r") as sitemap_json:
                data1 = dict(json.load(sitemap_json))
                # print(data1)
                sitemap_json.close()

                feed = dict(data1)["feedChannel"]
                feed_vals = {"channelId": str(feed["channelId"]), "name": '"' + str(feed["name"]) + '"',
                             "starRating": str(feed["starRating"]), "starRatingCount": str(feed["starRatingCount"]),
                             "description": '"' + str(feed["description"]).replace(",", "") + '"',
                             "developer": '"' + str(feed["developer"]) + '"'}
                detail = dict(data1).get("details")
                detail_vals = {"developerUserId": '"' + str(detail["developerUserId"]) + '"',
                               "publishedDate": str(detail["publishedDate"]),
                               "createdDate": str(detail["createdDate"]),
                               "modifiedDate": str(detail["modifiedDate"]),
                               "storeId": str(detail["storeId"])}

                for j in feed_vals.values():
                    sitemap_csv.write(str(j) + ",")
                for k in detail_vals.values():
                    sitemap_csv.write(str(k) + ",")
            print(cnt_da_lp)
        sitemap_csv.close()
    sitemap_txt.close()
