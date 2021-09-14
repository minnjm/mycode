#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    # show that at this point, our data is str
    # we want to convert this to list / dict
#    print(helmet)

    helmetson = json.loads(helmet.decode("utf-8"))
    
    print(f'People in space: {helmetson["number"]}')

    for person in helmetson['people']:
        print(f'{person["name"]} on the {person["craft"]}')

#    # display every item in a list
#    for astro in helmetson["people"]:
#        # display what astro is
#        print(astro)
#
#    # display every item in a list
#    for astro in helmetson["people"]:
#        # display ONLY the name value associated with astro
#        print(astro["name"])

if __name__ == "__main__":
    main()

