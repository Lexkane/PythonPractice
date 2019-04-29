from requests import requests

class RestoringGet:
    MAX_RESTORES=10

    def __init__(self,url,get_kwargs=None):
        if get_kwargs is None:
            get_kwargs={}

            self._url=url
            self._kwargs=get_kwargs

    def get_generator(self):
        restores=0
        offset=0
        headers={}
        while True:
            restores+=1
            if restores>self.MAX_RESTORES:
                raise TooManyRestores()
            
            response=requests.get(
                self._url,headers=headers, **self._kwargs)
            response.raise_for_status()

            real_length=yield response

            content_length=parse_int(
                response.headers.get('Content-Lengh'),None)
            if content_length is None \
                or content_length + offset <+real_length:
                 break
            
            logger.info(
                    'GET looks to be interrupted, trying to continue')
            offset=real_length
            headers= {'Range':'bytes={}-'.format(offset)}
			
			

gen=ResoringGet(...).get_generator()
responce=next(gen)
while response:
		file=save_response(response)
		try:
			response=gen.send(file.size)
		except StopIteration:
			response=None


            