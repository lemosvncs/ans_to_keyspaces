import os
import pandas as pd

# AWS
import boto3
from botocore.errorfactory import ClientError
ks = boto3.client("keyspaces")

# Cassandra
from cassandra.cluster import Cluster, ConsistencyLevel, ExecutionProfile
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider
from cassandra_sigv4.auth import SigV4AuthProvider

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.load_verify_locations("/home/vini/git/proj_ans/py/sf-class2-root.crt")
ssl_context.verify_mode = CERT_REQUIRED

boto_session = boto3.Session()
auth_provider = SigV4AuthProvider(boto_session)
ep = {"quorum":ExecutionProfile(consistency_level=ConsistencyLevel.LOCAL_QUORUM)}
cluster = Cluster(['cassandra.sa-east-1.amazonaws.com'], ssl_context=ssl_context, auth_provider=auth_provider, port=9142, execution_profiles=ep)
# cluster.add_prepared()j
# ConsistencyLevel.LOCAL_QUORUM
session = cluster.connect()
# session.default_serial_consistency_level(6)

# session.execute("CONSISTENCY LOCAL_QUORUM;")

# r = session.execute("select * from system_schema.keyspaces")
# print(r.current_rows)

files_path = "/home/vini/git/proj_ans/files"
files = os.listdir(path=files_path)

# df = pd.read_csv("../files/PA_202201_AMB_DET.csv", sep = ";", low_memory=False)
# format(f"{*df.columns.values, }".replace("'", ""))
# format(f"{*df.iloc[0].values, }")

# df.columns.to_list()
def up_files(files:list):
    for f in files:
        if f.find(".csv") != -1 and f.find("AMB_DET") != -1:
            df = pd.read_csv(f"{files_path}/{f}", sep=";", low_memory=False)
            # df = df.iloc[0:10]
            colunas = format(f"{*df.columns.values, }".replace("'", ""))
            for i, v in df.iterrows():
                q = f"""INSERT INTO ans.amb_det JSON '{format(v.to_dict()).replace("'", '"').lower()}'"""
                # q = q.replace("'", '"')
                # q = f"""UPDATE ans.amb_det {colunas}
                        #    VALUES {format(f"{*v.values, }")}"""
                try:
                    session.execute(q, execution_profile="quorum")
                except:
                    print(q)
up_files(files)