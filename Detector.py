from joblib import load
import pandas as pd

def mapping_fun(data):
    d = ['ftp_data', 'other', 'private', 'http', 'remote_job', 'name',
       'netbios_ns', 'eco_i', 'mtp', 'telnet', 'finger', 'domain_u',
       'supdup', 'uucp_path', 'Z39_50', 'smtp', 'csnet_ns', 'uucp',
       'netbios_dgm', 'urp_i', 'auth', 'domain', 'ftp', 'bgp', 'ldap',
       'ecr_i', 'gopher', 'vmnet', 'systat', 'http_443', 'efs', 'whois',
       'imap4', 'iso_tsap', 'echo', 'klogin', 'link', 'sunrpc', 'login',
       'kshell', 'sql_net', 'time', 'hostnames', 'exec', 'ntp_u',
       'discard', 'nntp', 'courier', 'ctf', 'ssh', 'daytime', 'shell',
       'netstat', 'pop_3', 'nnsp', 'IRC', 'pop_2', 'printer', 'tim_i',
       'pm_dump', 'red_i', 'netbios_ssn', 'rje', 'X11', 'urh_i',
       'http_8001']
    map_data = {}
    flag_data = {}
    index = 0
    f = ['SF', 'S0', 'REJ', 'RSTR', 'SH', 'RSTO', 'S1', 'RSTOS0', 'S3',
       'S2', 'OTH']
    for i in d:
        map_data[i] = index
        index+=1
    index = 0
    for i in f:
        flag_data[i] = index
        index+=1

    return map_data[data['service']] , flag_data[data['flag']]


def detect(data):
    data['service'] , data['flag']= mapping_fun(data)
    model = load('Network_Intrusion_Detection_Model.joblib')
    data = pd.DataFrame([data])
    output = model.predict(data)
    return output