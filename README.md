GovPay Gateway Project
Overview
A sandbox government payment gateway built with FastAPI and MongoDB for an 8-week internship training program. It supports invoice registration, payment processing, and notifications with data replication across two instances.
Week 1 Setup Instructions

Install Python 3.10+:

Download from python.org.
Verify: python --version


Set Up Virtual Environment:
python -m venv env


Activate:
Windows: env\Scripts\activate
macOS/Linux: source env/bin/activate




Install Dependencies:
pip install fastapi uvicorn motor
pip freeze > requirements.txt


Run FastAPI App:
uvicorn app.main:app --reload


Access: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs


Set Up CassandraDB:
1.install wsl-2:
wsl --install -d Ubuntu-22.04

2. **Set Up Ubuntu Username**:
- Run: `wsl -d Ubuntu-22.04 -u root`
- Create user: `adduser govpayuser`
sudo apt install openjdk-11-jdk -y

3. **Install Java 11**:


4. **Install Cassandra 4.1.9**:
- Extract `apache-cassandra-4.1.9-bin.tar.gz` to `cassandra-node1` and `cassandra-node2`.
- Configure `cassandra.yaml` and `cassandra-env.sh` for JMX ports (7199, 7200).
- Start: `cassandra-node1/bin/cassandra -f` and `cassandra-node2/bin/cassandra -f`.

5. **Initialize Keyspace**:
cassandra-node1/bin/cqlsh 127.0.0.1 9042 -f docker/cassandra-init.cql

Initialize Git:
git init
git add .
git commit -m "Initial commit: Week 1 setup"


