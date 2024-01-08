from flask import Flask, render_template

app = Flask(__name__)

params = {
    # 全部/兼職/...
    "ro": 0,
    "kwop": 7,
    # 工作關鍵字
    "keyword": "",
    "expansionType": "area,spec,com,job,wf,wktm",
    # 上班地點
    "area": "",
    # 薪資待遇最低
    "scmin": "",
    # 薪資待遇最高
    "scmax": "",
    "order": 15,
    "asc": 0,
    # 1有22個職缺
    "page": "",
    "mode": "s",
    "jobsource": "index_s",
    "langFlag": 0,
    "langStatus": 0,
    "recommendJob": 1,
    "hotJob": 1,
}


@app.route("/")
def index():
    name = "這是方便查詢104職缺和詳細內容的網站,歡迎使用"
    return render_template("./index.html", **locals())


if __name__ == "__main__":
    app.run(debug=True)
