#!/usr/bin/python
from shotwell import app
from optparse import OptionParser
import sys

usage = """
usage: runserver.py [options] 
"""
def main(args):
    parser = OptionParser( usage=usage, )
    parser.add_option( "--port",
                       action="store",type=int,
                       dest="port", default=5000,
                       help="Specify port number for SSL service. " )
    parser.add_option( "--host",
                       action="store",
                       dest="host", default=None,
                       help="Specify hosts being served.  " )
    parser.add_option( "--cert",
                       action="store",
                       dest="cert", default="server.crt",
                       help="Specify certificate file for SSL." )
    parser.add_option( "--key",
                       action="store",
                       dest="key", default="server.key",
                       help="Specify key file for SSL." )
    opts,args = parser.parse_args(args)
    app.run(debug=True, port=opts.port,host=opts.host,)
    #        ssl_context=(opts.cert,opts.key))

if __name__ == '__main__':
    main(sys.argv)
