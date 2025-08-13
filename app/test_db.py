import asyncio
from cassandra.cluster import Cluster
from cassandra.io.asyncorereactor import AsyncoreConnection

async def test_connection():
    cluster = Cluster(['127.0.0.1', '127.0.0.2'], port=9042, connection_class=AsyncoreConnection)
    session = cluster.connect('govpay')
    result = session.execute('SELECT cluster_name FROM system.local').one()
    print(result.cluster_name)  # Expect 'govpay_cluster'
    cluster.shutdown()

asyncio.run(test_connection())