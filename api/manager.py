from pydrive2.drive import GoogleDrive

catgry = {"hiphop":"1f7V7JZ3_JJRCerPZ29ympK592A-hltla","hindi":"1aAxMnwdvrPuElQRKKjxg-D13LO_PWVx7","english":"16RHi1_BKPf9Cna-F5P8_ScpeR4xcWOfU"}

def get_file_list(parent,drive=None,gauth=None):
    if gauth :
        drive = GoogleDrive(gauth)
    file_list = drive.ListFile({'q': f"'{parent}' in parents and trashed=false"}).GetList()
    return file_list



# def audio_update(name,id,cat,art):
#     data =  {
#     "name":name,
#     "id":id,
#     "catg":cat,
#     "artist":art,
#     "art":f"/api/album-art?id={id}"
#     }
#     audio.insert(data)


# def SyncDrive(gauth):
    # drive = GoogleDrive(gauth)
    # audio.truncate()
    # folder.truncate()
    # print("syncing drive")
    # for i in catgry.keys():
    #     songs_by_cat = []
    #     files = get_file_list(catgry.get(i),drive)
    #     for k in files:
    #         if k['mimeType'] == "application/vnd.google-apps.folder":
    #             songs_by_art = []
    #             for g in get_file_list(k['id'],drive):# songs with artist
    #                 name,id,cat,artist = g['title'],g['id'],i,k['title']
    #                 songs_by_art.append({"name":name,"id":id})
    #              #   get_album_art(id)
    #                 audio_update(name=name,id=id,cat=cat,art=artist)
    #             folder.insert({artist:songs_by_art,"id":k['id'],"name":artist})
    #         else:#songs without artist
    #             name,id,cat,artist = k['title'],k['id'],i,None
    #             audio_update(name=name,id=id,cat=cat,art=artist)
    #             #get_album_art(id)
    #             songs_by_cat.append({"name":name,"id":id})
    #     folder.insert({i:songs_by_cat,"id":catgry.get(i),"name":i})


    # print("drive is synced ")