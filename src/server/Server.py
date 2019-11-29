import json
import pycld2 as cld2

import web

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        data = web.input()
        if not 'text' in data.keys():
            return json.dumps({"error": "Parameter 'text' was not set."})

        reliable, _, details = cld2.detect(data.text)

        print(details)

        ret = {
            "reliable": reliable,
            "language": details[0][0],
            "short": details[0][1],
            "prob": details[0][2]
        }
        return json.dumps(ret)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
