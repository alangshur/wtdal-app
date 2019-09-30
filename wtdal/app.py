import falcon
import time
import wtdal.adapter as adapter

# initialize WSGI app
application = falcon.API()

# build adapter sockets
status, ingestion, match, control = adapter.build_adapter_sockets()
if (status):
    time.sleep(1)
    adapter.MatchSocketFunctions.send_match_packet(match)
    # adapter.ControlSocketFunctions.send_shutdown_packet(control)
    # adapter.ControlSocketFunctions.send_outlier_packet(control)
    # adapter.ControlSocketFunctions.send_alive_packet(control)