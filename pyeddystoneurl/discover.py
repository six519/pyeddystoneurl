"""
 * 2018 http://ferdinandsilva.com
 *
 * Python C Extension To Scan Eddystone-URL Beacons
 * 
 * Author:
 * Ferdinand Silva <ferdinandsilva@ferdinandsilva.com>
 * 
"""
from pyeddystoneurl_scan import *
import re, codecs

def discover(timeout):
    ret = {}

    devices = scan(timeout)

    #filter devices by address
    for dev in devices:
        if dev['address'] not in ret:
            # add to return
            ret[dev['address']] = {
                'name': '',
                'url': '',
                'rssi': dev['rssi']
            }

        if len(dev['info']) > 28:
            # valid info
            lineToRemove = dev['info'][:26]
            cleanLine = dev['info'].replace(lineToRemove, "")

            if re.search('^(00|01|02|03)', cleanLine):
                # URL
                justStarted = True
                urlStr = ""

                while len(cleanLine) > 0:
                    lineToRemove = cleanLine[:2]
                    # decode URL

                    if justStarted:
                        justStarted = False

                        if lineToRemove == "00":
                            urlStr = "http://www."
                        elif lineToRemove == "01":
                            urlStr = "https://www."
                        elif lineToRemove == "02":
                            urlStr = "http://"
                        else:
                            #03
                            urlStr = "https://"
                        cleanLine = cleanLine.replace(lineToRemove, "", 1)
                        continue

                    if lineToRemove == "00":
                        urlStr += ".com/"
                    elif lineToRemove == "01":
                        urlStr += ".org/"
                    elif lineToRemove == "02":
                        urlStr += ".edu/"
                    elif lineToRemove == "03":
                        urlStr += ".net/"
                    elif lineToRemove == "04":
                        urlStr += ".info/"
                    elif lineToRemove == "05":
                        urlStr += ".biz/"
                    elif lineToRemove == "06":
                        urlStr += ".gov/"
                    elif lineToRemove == "07":
                        urlStr += ".com"
                    elif lineToRemove == "08":
                        urlStr += ".org"
                    elif lineToRemove == "09":
                        urlStr += ".edu"
                    elif lineToRemove == "0a":
                        urlStr += ".net"
                    elif lineToRemove == "0b":
                        urlStr += ".info"
                    elif lineToRemove == "0c":
                        urlStr += ".biz"
                    elif lineToRemove == "0d":
                        urlStr += ".gov"
                    else:
                        urlStr += codecs.decode(lineToRemove, "hex")

                    cleanLine = cleanLine.replace(lineToRemove, "", 1)

                ret[dev['address']]['url'] = urlStr
            else:
                # name
                lineToRemove = cleanLine[:4]
                cleanLine = cleanLine.replace(lineToRemove, "")
                ret[dev['address']]['name'] = codecs.decode(cleanLine, "hex")

    #clean up devices
    #remove devices that doesn't have a url
    for k,v in ret.items():
        if ret[k]["url"] == "":
            del ret[k]

    return ret