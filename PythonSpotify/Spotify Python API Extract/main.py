import logging
from config import *
import base64
import requests
from datetime import datetime, timedelta
from urllib.parse import urlencode
import pandas as pd
#import pysftp

now = datetime.now()

logging.basicConfig(
    level=logging.INFO,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename=LogFileName,#'%slog' % __file__[:-2],
    filemode='a'
)

try:
    class SpotifyAPI(object):
        access_token = None
        access_token_expires = now
        access_token_did_expire = True
        client_id = None
        client_secret = None
        token_url = "https://accounts.spotify.com/api/token"

        def __init__(self, client_id, client_secret, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.client_id = client_id
            self.client_secret = client_secret

        def get_client_credentials(self):
            """
            Returns a base64 encoded string
            """
            client_id = self.client_id
            client_secret = self.client_secret
            if client_secret is None or client_id is None:
                raise Exception("You must set client_id and client_secret")
            client_creds = f"{client_id}:{client_secret}"
            client_creds_b64 = base64.b64encode(client_creds.encode())
            return client_creds_b64.decode()

        def get_token_headers(self):
            client_creds_b64 = self.get_client_credentials()
            return {
                "Authorization": f"Basic {client_creds_b64}"
            }

        @staticmethod
        def get_token_data():
            return {
                "grant_type": "client_credentials"
            }

        def perform_auth(self):
            token_url = self.token_url
            token_data = self.get_token_data()
            token_headers = self.get_token_headers()
            r = requests.post(token_url, data=token_data, headers=token_headers)
            if r.status_code not in range(200, 299):
                raise Exception("Could not authenticate client.")
                # return False
            data = r.json()
            access_token = data['access_token']
            expires_in = data['expires_in']  # seconds
            expires = now + timedelta(seconds=expires_in)
            self.access_token = access_token
            self.access_token_expires = expires
            self.access_token_did_expire = expires < now
            return True

        def get_access_token(self):
            token = self.access_token
            expires = self.access_token_expires
            if expires < now:
                self.perform_auth()
                return self.get_access_token()
            elif token is None:
                self.perform_auth()
                return self.get_access_token()
            return token

        def get_resource_header(self):
            access_token = self.get_access_token()
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
            return headers

        def search(self, query, search_type='artist'):  # type
            headers = self.get_resource_header()
            endpoint = "https://api.spotify.com/v1/search"
            data = urlencode({"q": query, "type": search_type.lower()})
            lookup_url = f"{endpoint}?{data}"
            r = requests.get(lookup_url, headers=headers)  # .json()
            if r.status_code not in range(200, 299):
                return {}
            return r.json()

        def get_resource(self, lookup_id, resource_type='artists', version='v1', target='related-artists'):
            endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}/{target}"
            headers = self.get_resource_header()
            r = requests.get(endpoint, headers=headers)
            if r.status_code not in range(200, 299):
                return {}
            return r.json()

        def get_related_artist(self, _id):
            return self.get_resource(_id, resource_type='artists', target='related-artists')

        def get_artist(self, _id):
            return self.get_resource(_id, resource_type='artists', target='albums')



    spotify = SpotifyAPI(client_id, client_secret)


    def getRelatedArtist(artist_name, id):
        # id='4Awgi8rHD631aMJCXLf21D'   ###uncomment for testing
        related_artists = []
        related_artist_cnt = len(spotify.get_related_artist(id)['artists'])
        # print("related_artist_cnt",related_artist_cnt)
        rank = 0
        JSON_Data = spotify.get_related_artist(id)['artists']  # ('4Awgi8rHD631aMJCXLf21D')

        if related_artist_cnt > 0:
            for x in range(0, related_artist_cnt):
                rank = rank + 1
                genres_cnt = 0
                image_cnt = 0
                genres_cnt = len(JSON_Data[x]['genres'])
                image_cnt = len(JSON_Data[x]['images'])

                # derive metadata
                Artist_Name = artist_name
                RelatedArtist_Name = JSON_Data[x]['name']
                External_Urls_Spotify = JSON_Data[x]['external_urls']['spotify']
                Followers_Total = JSON_Data[x]['followers']['total']
                if genres_cnt > 0:
                    Genres_001 = JSON_Data[x]['genres'][0]
                else:
                    Genres_001 = ''

                if genres_cnt > 1:
                    Genres_002 = JSON_Data[x]['genres'][1]
                else:
                    Genres_002 = ''

                if genres_cnt > 2:
                    Genres_003 = JSON_Data[x]['genres'][2]
                else:
                    Genres_003 = ''

                if genres_cnt > 3:
                    Genres_004 = JSON_Data[x]['genres'][3]
                else:
                    Genres_004 = ''

                if genres_cnt > 4:
                    Genres_005 = JSON_Data[x]['genres'][4]
                else:
                    Genres_005 = ''

                ID = JSON_Data[x]['id']

                if image_cnt > 0:
                    Large_image = JSON_Data[x]['images'][0]['url']
                else:
                    Large_image = ''

                if image_cnt > 1:
                    Medium_image = JSON_Data[x]['images'][1]['url']
                else:
                    Medium_image = ''

                if image_cnt > 2:
                    Small_image = JSON_Data[x]['images'][2]['url']
                else:
                    Small_image = ''

                Popularity = JSON_Data[x]['popularity']
                Type = JSON_Data[x]['type']

                artist = [Artist_Name , RelatedArtist_Name, rank, External_Urls_Spotify , Followers_Total
                    , Genres_001, Genres_002, Genres_003, Genres_004, Genres_005
                    , ID
                    , Large_image
                    , Medium_image
                    , Small_image
                    , Popularity, Type]

                related_artists.append(artist)

        return related_artists


    #download Source Artist file
    if 1==1:

        artists = pd.read_csv(SourceFileName, encoding='UTF-16', sep="|", error_bad_lines=False)#   #For testing , nrows=10
        #print(artists.head(10))
        artists_ids_repo = pd.read_csv("artists_ids_repo.csv",  sep=",", error_bad_lines=False)
        #print(artists_ids_repo.head(10))


        df = pd.merge(artists, artists_ids_repo,
                      left_on='Artist_Name',
                      right_on='artist_name',
                      how='left')

        Missing_Artist_ids = df[df['id'].isnull()]
        print("printing artist with missing ids",Missing_Artist_ids)

        Missing_Artist_ids = Missing_Artist_ids[['Artist_Name']].drop_duplicates()
        Missing_Artist_ids['FULL_NAME'] = Missing_Artist_ids['Artist_Name']
        print(len(Missing_Artist_ids))

        print("Starting the process to extract Artists with missing ID's")

        artist_list = []

        for artist in Missing_Artist_ids['FULL_NAME']:
            # print(artist)
            result = spotify.search(artist, search_type='artist')['artists']['items']
            # print(result)
            try:
                if not result:
                    continue
                else:
                    id_val = result[0]['id']
                    artist_name = artist

                    Artist = [artist_name, id_val]
                    print(Artist)
                    artist_list.append(Artist)
            except:
                pass
                print('no data')

        df_artists_missing_ids = pd.DataFrame(artist_list,
                          columns=['artist_name', 'id'])
        LocalFileName = OutputFileName + '.csv'
        FinalOutputFileName = OutputFileName + '_' + now.strftime('%Y-%m-%d') + '.csv'

        #load artists with missing id's to repo csv file.
        df_artists_missing_ids.to_csv('artists_ids_repo.csv', sep=',', index=False, mode='a', header=False)


        artists_ids_repo = pd.read_csv("artists_ids_repo.csv", sep=",", error_bad_lines=False)
        # print(artists_ids_repo.head(10))

        df_artists_ids = pd.merge(artists, artists_ids_repo,
                      left_on='Artist_Name',
                      right_on='artist_name',
                      how='left')


        Full_Related_Artists = []
        print('Starting data load')

        for index, row in df_artists_ids.iterrows():
            # time.sleep(.5)
            try:
                Artists = getRelatedArtist(row["Artist_Name"], row["id"])  # getRelatedArtist(related_artist[i])
                for Artist in Artists:
                    Full_Related_Artists.append(Artist)
            except:
                pass
        # create dataset
        df = pd.DataFrame(Full_Related_Artists,
                          columns=['Artist_Name', 'RelatedArtist_Name', 'Rank', 'External_Urls_Spotify', 'Followers_Total'
                              , 'Genres_001', 'Genres_002', 'Genres_003', 'Genres_004', 'Genres_005'
                              , 'ID', 'Large_image', 'Medium_image', 'Small_image', 'Popularity', 'Type', ])
        LocalFileName = OutputFileName + '.csv'
        FinalOutputFileName = OutputFileName +'_'+ now.strftime('%Y-%m-%d') + '.csv'
        df.to_csv(LocalFileName, sep=',', index = False)

        print('Operation completed')
    # with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp_upload:
    #     print("Upload connection succesfully stablished ... \n")
    if 1==1:
        

        remotepath = r'/Import/Spotify/'+FinalOutputFileName
        localpath = LocalFileName

        # o_var = sftp_upload.put(localpath, remotepath, confirm=False)
        # print('o_var:', o_var)
        # sftp_upload.close()
        print("File uploaded... \n")
    # In[ ]:
    exit(200)

except Exception as e1:
    print('[Error-1]:', e1)
    logging.ERROR("Error Exception Occured: ",exc_info=True)
    logging.critical("Critical Exception Occured Error: ",exc_info=True)
    logging.warning("Warning Exception Occured Error: ",exc_info=True)


