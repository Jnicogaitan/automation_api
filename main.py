from datetime import datetime
from automation_api.enums import DevelopmentEnvironments
from automation_api.clients import SupertableClient

client = SupertableClient()
blacklist_collection = client.get_collection(DevelopmentEnvironments.DEV3, 'blacklist')
datacreditexperian_collection = client.get_collection(DevelopmentEnvironments.DEV1, 'datacreditexperian')

try:
     # Cantidad de documentos en la colección
     count = blacklist_collection.count_documents({'identification':1032392583})
     print('Conexión exitosa a la base de datos de GrupoR5')
     print('Cantidad de documentos en blacklist:', count)
except Exception as e:
     print('Error al intentar acceder a la colección:', e)

try:
     count = datacreditexperian_collection.count_documents({'identification':1032392583})
     print('Cantidad de documentos en datacreditexperian:', count)
except Exception as f:
     print('Error al intentar acceder a la colección:', f)

 # Eliminacion de los registros
delete_result1 = blacklist_collection.delete_many({
     'value': {
         '$in': ['1032392583',
                 '3105564840',
                 'nicolas.gaitan+666@grupor5.com',
                 'nicolas.gaitan+233@grupor5.com']
     }
 })

delete_result2 = datacreditexperian_collection.delete_many({
     'identification':  1032392583,
     'created': {
         "$gt": datetime(2023, 2, 12, 15, 24, 15, 724000)
     }
 })
print('Documentos eliminados de blacklist:', delete_result1.deleted_count)
print('Documentos eliminados de datacreditexperian:', delete_result2.deleted_count)

client.close()
print(client.server_info())















