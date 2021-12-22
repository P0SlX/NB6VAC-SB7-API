# Florian SAVOURÉ
# 22/12/2021
# Réplique de l'API de la NB6VAC pour faire fonctionner le décodeur SB7 de chez SFR
# Le décodeur fait d'autre GET à l'API cependant il vérifie pas son retour, juste qu'il
# y en a un. Ces routes routes ne sont donc pas implémentés ici. Uniquement celle nécessaires.

from flask import Flask, send_file, request
import pytz
from datetime import datetime
from flask import Response
import requests

app = Flask(__name__)


@app.route('/api/1.0/', methods=['GET'])
def api():
    method = request.args.get('method')
    if method == "system.getInfo":
        return system_get_info()
    elif method == "ftth.getInfo":
        return ftth_get_info()
    elif method == "lan.getHostsList":
        return lan_get_hosts_list()
    elif method == "wan.getInfo":
        return wan_get_info()
    return ""


def wan_get_info():
    with open("/proc/uptime", 'r') as f:
        uptime = f.readline().split('.')[0]

    try:
        ip = requests.get("https://ifconfig.me/ip").text
    except:
        ip = ""
    
    # Changer infra et mode si vous avez autre chose que la fibre
    return Response(f"""<?xml version="1.0" encoding="UTF-8"?>
<rsp stat="ok" version="1.0">
     <wan status="up" uptime="{uptime}" ip_addr="{ip}" infra="ftth" mode="ftth/routed" infra6="" status6="down" uptime6="" ipv6_addr="" />
</rsp>\n""", mimetype='text/xml')


def lan_get_hosts_list():
    # Changer ip et mac avec les valeurs de votre décodeur
    # Attribuez une IP fixe au décodeur pour pas changer l'ip tout le temps
    return Response("""<?xml version="1.0" encoding="UTF-8"?>
<rsp stat="ok" version="1.0">
    <host type="stb" name="STB7" ip="192.168.1.xx" mac="xx:xx:xx:xx:xx:xx" iface="lan3" probe="56" alive="350261" status="online" />
</rsp>\n""", mimetype='text/xml')


def ftth_get_info():
    return Response("""<?xml version="1.0" encoding="UTF-8"?>
<rsp stat="ok" version="1.0">
     <ftth status="up" wanfibre="in"/>
</rsp>\n""", mimetype='text/xml')


def system_get_info():
    with open("/proc/uptime", 'r') as f:
        uptime = f.readline().split('.')[0]

    format_time = lambda d: d.strftime('%Y%m%d%H%M')
    current_datetime = format_time(pytz.timezone("Europe/Paris").localize(datetime.now(), is_dst=None))

    # Changer les infos ci-dessous avec celle de votre box
    return Response(f"""<?xml version="1.0" encoding="UTF-8"?>
<rsp stat="ok" version="1.0">
     <system product_id="NB6VAC-FXC-r0" serial_number="XXXXXXXXXXXXXXXXXX" mac_addr="xx:xx:xx:xx:xx:xx" net_mode="router" net_infra="ftth" uptime="{uptime}" version_mainfirmware="NB6VAC-MAIN-R4.0.44j" version_rescuefirmware="NB6VAC-MAIN-R4.0.44i" version_bootloader="NB6VAC-BOOTLOADER-R4.0.8" version_dsldriver="NB6VAC-XDSL-A2pv6F039p" current_datetime="{current_datetime}" refclient="" idur="XXXXXXX" alimvoltage="12251" temperature="48399"  />
</rsp>\n""", mimetype='text/xml')


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
