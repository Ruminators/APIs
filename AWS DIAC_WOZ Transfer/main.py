

import os 
import tempfile as tmp
rootpath=os.getcwd()
print("ping ",rootpath)

import json
import requests
import os 
import boto3

BUCKET_NAME='daic-woz-data'



def cache_generate(session, download, file):
    


    print("-----------------------------------------------------------------------")
    print("file dumped into local cloud function storage from web.")
    print("now started uploading it into cloud stoage bucket's blob: ",download[1]) 
    r = session.get(download[0], stream = True)

    # -------------------------------------------------------

    with open(file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    # -------------------------------------------------------
    
    print("uploaded into bucket: ",file)    
    





def daic_downloader(tm,client):


    # ===================================================
    hostname='dcapswoz.ict.usc.edu'
    session = requests.Session()
    session.auth = ('daicwozuser','dA1c_U$3rW0zz')
    
    auth = session.post('http://' + hostname)
    hostname += '/wwwdaicwoz'
    response = session.get('http://' + hostname)
    htmlsrc = response.content
    # print(htmlsrc)
    # ===================================================
    


    # ==============================================================================
    from bs4 import BeautifulSoup as bs
    s=bs(htmlsrc,"html.parser")
    l=[]
    for link in s.find_all('a'):
        l.append(link.get('href'))

    links = [ [ 'http://' + hostname + '/' + x ,x] for x in l[5:]]
    for i in links:
        print(i);
    print("here, got all links in hand after scraping: apache_server indexof/")
    # ==============================================================================
    



    # ---------------------------------------------------------------
    if not os.path.exists(os.path.join(rootpath,'cache')):
        os.makedirs(os.path.join(rootpath,'cache'))
    # ---------------------------------------------------------------



    # ==============================================================================
    for download in links:
        
        
        b_data=client.list_objects(Bucket=BUCKET_NAME)
        if "Contents" in b_data.keys():
            b_items=b_data["Contents"]
        else:
            b_items=[]



        hello = [ x['Key'] for x in b_items]
        print(hello)
        f_name=download[1]
        file = os.path.join(rootpath,'cache',f_name)


        if not f_name in hello:
           

            if os.path.exists(file):
                tm.upload_file(file, BUCKET_NAME,f_name)
            else:
                cache_generate(session,download,file)
        else:
            print("ignored it")


        if os.path.exists(file):
            os.remove(file)
        print("removed file from /tmp/cache local storage")
        print("-----------------------------------------------------------------------")

    # ==============================================================================










def load(init):

    # bucket init
    # ------------------------------------------------------------------


    print("initiating bucket: ",BUCKET_NAME)
    client= boto3.client('s3')




    # ****************************************************** 
    conf = boto3.s3.transfer.S3TransferConfig()
    MB=boto3.s3.transfer.MB
    conf.use_threads=False
    conf.multipart_threshold=100*MB
    conf.multipart_chunksize=30*MB
    # ******************************************************   
    
    
    tm = boto3.s3.transfer.S3Transfer(client,conf)
    daic_downloader(tm,client)
    boto3.set_stream_logger()
    # ------------------------------------------------------------------


#   shell build commands
#   gcloud compute --project "daic-220306" ssh --zone "us-central1-a" "diac"
#   python /daic/main.py 


load("start")
print("process finished :)")

exit()