from fasthtml.common import *

app = FastHTML()


@app.get("/")
def homepage():
    return "<h1>Hello Word</h1>"

serve()
