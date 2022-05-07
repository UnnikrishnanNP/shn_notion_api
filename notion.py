import json
import requests 


class NotionClient:
    def __init__(self,token,database):
        self.database = database
        self.headers = {
            "Authorization": "Bearer " + token,
            "Notion-Version": "2022-02-22",
            "Content-Type": "application/json"
        }

    def create_page(self,description,date):
        create_url = "https://api.notion.com/v1/pages"
        data = {
        "parent": { "database": self.database },
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                            "start": date,
                            "end": None
                        }
                    }
                }
            }
        data = json.dumps(data)
        res = requests.post(create_url,headers=self.headers,data=data)
        print(res.status_code)
        return res
