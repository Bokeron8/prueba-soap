import os
from dotenv import load_dotenv
from zeep import Client
from zeep.plugins import HistoryPlugin
from lxml import etree # type: ignore
load_dotenv()


wsdl = 'http://clswcorrientes.smartmovepro.net/ModuloParadas/SWParadas.asmx?WSDL'
history = HistoryPlugin()
client = Client(wsdl=wsdl,
                plugins=[history])

response = client.service.RecuperarLineaPorLocalidad(
    usuario=os.getenv("USUARIO"),
    clave=os.getenv("CLAVE"),
    localidad="Corrientes",
    provincia="Corrientes",
    pais="Argentina",
    isSublinea=False
)

print(response)
if(history.last_sent != None):
    print("\n Solicitud (XML enviado):")
    print(etree.tostring(history.last_sent["envelope"], pretty_print=True).decode())