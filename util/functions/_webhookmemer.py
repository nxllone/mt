import requests, json, time

hook = input("enter your webhook : ")

class memer:
    def __init__(self):
        pass

    @staticmethod
    def load_meme():
        url = "https://meme-api.com/gimme"
        img = requests.get(url)
        data = json.loads(img.text)
        meme = data["url"]
        r = requests.post(hook, json={"content": f"{meme}"})
        if r.ok:
            print("SENT MEME :D")
            memer.load_meme()
        else:
            print("INVALID WEBHOOK")
            time.sleep(3)