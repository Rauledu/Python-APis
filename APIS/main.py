import requests

if __name__=='__main__':
    url = 'https://i.imgur.com/Ab0BWOU.jpeg'

    response = requests.get(url, stream=True)#realiza la peticion sin descargar contenido
    with open('image.jpeg', 'wb') as file:

        for Chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(Chunk)
    response.close()


    #https://www.youtube.com/watch?v=oExagoikAZ8&list=PLpOqH6AE0tNguX5SG8HpcD3lfmzWrIn9n&index=9&ab_channel=codigofacilito




    # url = 'http://httpbin.org/delete'
    # # args= {'nombre': 'Raul', 'curso': 'python'}
    # payload= {'nombre': 'Raul', 'curso': 'python'}
    # headers={'Content-Type': 'aplication/json'}

    # response=requests.delete(url, data=json.dumps(payload), headers=headers)
    """
    GET
    POST
    PUT
    DELETE
    """
    #json post se encarga de serializarlos
    #data entonces nos debemos de encargar de serializarlos
    # print(response.url)

    # if response.status_code==200:
    #     headers_response = response.headers
    #     server = headers_response['Server']
    #     print(server)
        #print(response.content)


        # response_json = json.loads(response.text)
        # origin = response_json['origin']
        # print(origin)


        #Metodo GET
        # response_json= response.json()
        # origin = response_json['origin']
        # print(origin)

        # content= response.content
        # print(content)
        # file= open('youtube.html', 'wb')
        # file.write(content)
        # file.close()