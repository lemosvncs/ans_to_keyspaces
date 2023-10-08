import boto3

from botocore.errorfactory import ClientError

ks = boto3.client("keyspaces")

# Custom
# Definição dos esquemas
from schemas import ambulatorialDet

config = {
    "KsName":"ans",
    "KsTables":["amb_det"]
}

def create_keyspaces_and_tables(config, ks):
    # Confere se os keyspaces e tabelas já existem. Se não existiram, cria-os.
    try:
        response = ks.get_keyspace(keyspaceName=config['KsName'])
    except ks.exceptions.ResourceNotFoundException:
        response = ks.create_keyspace(
            keyspaceName=config["KsName"],
            tags=[
                {
                    "key":"proj",
                    "value":"ans",
                }
            ]
        )
    
    for t in config['KsTables']:
        try:
            response = ks.get_table(keyspaceName=config['KsName'], tableName=t)
        except ks.exceptions.ResourceNotFoundException:
            response = ks.create_table(keyspaceName=config['KsName'],
                                       tableName=t,
                                       schemaDefinition=ambulatorialDet)

        infoTable = dict({
            "allColumns":[
                {
                    "name":"nome_do_arquivo",
                    "type":"text"
                },
                {
                    "name":"caminho",
                    "type":"text"
                },
                {
                    "name":"enviado",
                    "type":"boolean",
                }
            ],
            "partitionKeys":[{
                
                "name":"nome_do_arquivo",
            }],
        })

        try:
            response = ks.get_table(keyspaceName=config['KsName'], tableName="infoTable")
        except ks.exceptions.ResourceNotFoundException:
            response = ks.create_table(keyspaceName=config['KsName'],
                                       tableName="infoTable",
                                       schemaDefinition=infoTable)
                
create_keyspaces_and_tables(config, ks)