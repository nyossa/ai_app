from django.shortcuts import render
import pandas as pd
import pickle

category_data = pd.read_csv("idx2category.csv")
idx2category = {row.k: row.v for idx, row in category_data.iterrows()} 

with open("rdmf.pickle", mode="rb") as f:
    model = pickle.load(f)

def index(request):
    if request.method == "GET":
        #GETできた場合
        return render(
            request,
            "nlp/home.html"
        )
    else:
        #POSTできた場合
        title = [request.POST["title"]]#モデルへの値はリストで与えてやる必要がある。
        print("title:", title)
        result = model.predict(title)[0]
        print("result:", result)
        pred = idx2category[result]
        print(idx2category)

        return render(
            request,
            "nlp/home.html",
            {"title": pred}#titleという名前でhome.htmlに送り込む。
        )