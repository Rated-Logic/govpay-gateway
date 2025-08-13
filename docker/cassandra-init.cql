CREATE KEYSPACE IF NOT EXISTS govpay WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 2
};