import os
from dotenv import load_dotenv
from zeep import Client

load_dotenv()

wsdl = 'http://clswcorrientes.smartmovepro.net/ModuloParadas/SWParadas.asmx?WSDL'
client = Client(wsdl=wsdl)

response = client.service.RecuperarLineaPorLocalidad(
    usuario=os.getenv("USUARIO"),
    clave=os.getenv("CLAVE"),
    localidad="Corrientes",
    provincia="Corrientes",
    pais="Argentina",
    isSublinea=False
)

print(response)
