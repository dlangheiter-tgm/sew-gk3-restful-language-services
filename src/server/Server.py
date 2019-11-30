import json
import pycld2 as cld2

import web

"""Definition of the accepted urls"""
urls = (
    '/', 'Index'
)


class Index:
    """
    Class to handle requests to the '/' path
    """

    def GET(self):
        """
        Handles the GET requests to '/'.

        The endpoint expects the GET parameter 'text' to be the text is should analyze.
        It returns a json object in this format:
        ```
        {
            reliable (boolean): reliability
            language (string): found language full name
            short (string): found language short name
            prob (integer): probability in percent
        }
        ```
        If there is an error it will return a json object in the format:
        ```
        {
            error (string): Error message
        }
        ```

        :return: String return (stringified json object)
        """
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
    """Runs the web server"""
    app = web.application(urls, globals())
    app.run()
