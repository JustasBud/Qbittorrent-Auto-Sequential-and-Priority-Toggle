import time
from qbittorrent import Client

# IP/Port of hosted Qbittorrent
qb = Client('http://192.168.1.xxx:xxxx/')


while True:
    qb.login('WebUI_UserID', 'WebUI_UserPW')
    my_list=qb.torrents()
    
    list_to_enable_toggle=[]
    
    
    for i in range(0,len(my_list)):
        if my_list[i].get('seq_dl')==False:
            list_to_enable_toggle.append((my_list[i].get('infohash_v1')))
            
            
           
    qb.toggle_sequential_download(list_to_enable_toggle)
    qb.toggle_first_last_piece_priority(list_to_enable_toggle)
    
    
    qb.logout()
    
    
    time.sleep(60)
    
    
    
    
    





