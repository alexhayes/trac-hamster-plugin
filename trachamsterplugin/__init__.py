from trac.core import *
from trac.util.html import html
from trac.web import IRequestHandler
from trac.ticket import Ticket
from trac.util.datefmt import utc
from datetime import datetime

class TracHamsterPlugin(Component):
    implements(IRequestHandler)

    # IRequestHandler methods
    def match_request(self, req):
        return req.path_info == '/trac-hamster-plugin'
    
    def process_request(self, req):
        
        if not req.args.has_key('ticket_id') or not req.args.has_key('author') or not req.args.has_key('spent') or not req.args.has_key('message'):
            raise Exception("Request variables 'ticket_id', 'author', 'spent' and 'message' must be set.")

        ticket = Ticket(self.env, int(req.args.get('ticket_id')))
        
        # Check that timingandestimation plugin is installed...
        if not ticket.values.has_key('hours'):
            raise Exception("Ticket doesn't have 'hours' - check timingandestimation plugin is installed.", 500)
    
        ticket['hours'] = str(req.args.get('spent'))
        ticket.save_changes(req.args.get('author'), req.args.get('message'), datetime.now(utc))

        content = 'OK'
        req.send_response(200)
        req.send_header('Content-Type', 'text/plain')
        req.send_header('Content-Length', len(content))
        req.end_headers()
        req.write(content)
            