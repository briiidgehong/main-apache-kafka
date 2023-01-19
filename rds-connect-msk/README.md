[confluent connector docs](https://docs.confluent.io/cloud/current/connectors/index.html#supported-connectors)

1. msk 클러스터 구성 설정

```
# 테스트용 임시 처리 (원래는 네이밍규칙에 맞게 사전에 topic 생성해서 사용)
auto.create.topics.enable=true

# broker 갯수와 동일하게
default.replication.factor=2

min.insync.replicas=2
num.io.threads=8
num.network.threads=5
num.partitions=1
num.replica.fetchers=2
replica.lag.time.max.ms=30000
socket.receive.buffer.bytes=102400
socket.request.max.bytes=104857600
socket.send.buffer.bytes=102400
unclean.leader.election.enable=true
zookeeper.session.timeout.ms=18000
allow.everyone.if.no.acl.found=false
 ```

2. 커넥터 소스 디비 설정 (RDS 기준)

```
# DB RDS 옵션그룹 설정
rds.logical_replication = 1
max_replication_slots = 30
max_wal_senders	20
max_wal_size 2048

# wal_level 확인
show wal_level 
logical

# 사용자 구성
# 기본 사용자 postgres 를 사용해도 무방하나 새로운 사용자를 생성하고 싶다면 
# 아래와 같은 권한을 부여한다.
CREATE role debezium2 WITH PASSWORD '#####' login;
GRANT rds_superuser TO debezium2;
GRANT SELECT ON ALL TABLES IN SCHEMA public to debezium2;
GRANT CREATE ON DATABASE postgres TO debezium2;
 ```

3. docker-compose-postgresql-connect.yml

```
version: '2'
services:
  kafka-connect0:
    image: confluentinc/cp-kafka-connect:6.0.1
    ports:
      - 8083:8083
    volumes:
      - ./connector_lib:/usr/share/confluent-hub-components
    environment:
      CONNECT_PLUGIN_PATH: "/usr/share/java,/usr/share/confluent-hub-components"
      CONNECT_BOOTSTRAP_SERVERS: b-1-#####.ap-northeast-2.amazonaws.com:9196,b-2-#####.ap-northeast-2.amazonaws.com:9196

      CONNECT_SECURITY_PROTOCOL: SASL_SSL
      CONNECT_SASL_MECHANISM: SCRAM-SHA-512
      CONNECT_SASL_JAAS_CONFIG: org.apache.kafka.common.security.scram.ScramLoginModule required username="#####" password="#####";

      CONNECT_PRODUCER_SECURITY_PROTOCOL: SASL_SSL
      CONNECT_PRODUCER_SASL_MECHANISM: SCRAM-SHA-512
      CONNECT_PRODUCER_SASL_JAAS_CONFIG: org.apache.kafka.common.security.scram.ScramLoginModule required username="#####" password="#####";

      CONNECT_CONSUMER_SECURITY_PROTOCOL: SASL_SSL
      CONNECT_CONSUMER_SASL_MECHANISM: SCRAM-SHA-512
      CONNECT_CONSUMER_SASL_JAAS_CONFIG: org.apache.kafka.common.security.scram.ScramLoginModule required username="#####" password="#####";

      CONNECT_GROUP_ID: compose-connect-group
      CONNECT_CONFIG_STORAGE_TOPIC: _connect_configs_6
      CONNECT_CONFIG_STORAGE_REPLICATION_FACTOR: 2
      CONNECT_OFFSET_STORAGE_TOPIC: _connect_offset_6
      CONNECT_OFFSET_STORAGE_REPLICATION_FACTOR: 2
      CONNECT_STATUS_STORAGE_TOPIC: _connect_status_6
      CONNECT_STATUS_STORAGE_REPLICATION_FACTOR: 2

      CONNECT_KEY_CONVERTER: org.apache.kafka.connect.storage.StringConverter
      CONNECT_VALUE_CONVERTER: org.apache.kafka.connect.storage.StringConverter
      CONNECT_INTERNAL_KEY_CONVERTER: org.apache.kafka.connect.json.JsonConverter
      CONNECT_INTERNAL_VALUE_CONVERTER: org.apache.kafka.connect.json.JsonConverter

      CONNECT_REST_ADVERTISED_HOST_NAME: kafka-connect0
```
 

4. 볼륨 경로(=./connector_lib)에 postgresql debezium file download
```
https://debezium.io/releases/1.9/
./connector_lib
└── debezium-connector-postgres\ 3
    ├── CHANGELOG.md
    ├── CONTRIBUTE.md
    ├── COPYRIGHT.txt
    ├── LICENSE-3rd-PARTIES.txt
    ├── LICENSE.txt
    ├── README.md
    ├── README_JA.md
    ├── README_ZH.md
    ├── debezium-api-1.9.0.Final.jar
    ├── debezium-connector-postgres-1.9.0.Final.jar
    ├── debezium-core-1.9.0.Final.jar
    ├── failureaccess-1.0.1.jar
    ├── guava-30.1.1-jre.jar
    ├── postgres.json
    ├── postgresql-42.3.3.jar
    └── protobuf-java-3.19.2.jar
```
5. docker-compose -f docker-compose-postgresql-connect.yml up

6. 플러그인 조회
```
GET) http://0.0.0.0:8083/connector-plugins
{
  "class": "io.debezium.connector.postgresql.PostgresConnector",
  "type": "source",
  "version": "1.9.0.Final"
}
```

7. 커넥터 등록
```
POST) http://localhost:8083/connectors
BODY)
{
  "name": "postgresql-debezium-connector-test",
  "config": {
      "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
      "tasks.max": "1",
      "database.hostname": "#####.ap-northeast-1.rds.amazonaws.com",
      "database.port": "5432",
      "database.user": "#####",
      "database.password": "#####",
      "database.dbname" : "postgres",
      "database.server.name": "debezium-connector-test",
      "schema.whitelist": "public",
      "table.whitelist": "public.users3",
      "slot.name": "debeziumconnectortestslot",
      "plugin.name": "pgoutput"
      }
 }
```

8. 커넥터 조회
```
# 리스트 조회
GET) http://localhost:8083/connectors
[
  "postgresql-debezium-connector-test"
]

# 상세조회
GET) http://localhost:8083/connectors/postgresql-debezium-connector-test

# status 조회
GET) http://localhost:8083/connectors/postgresql-debezium-connector-test/status

# 커넥터 삭제
DELETE) http://localhost:8083/connectors/postgresql-debezium-connector-test
```

9. users3 테이블에 데이터 추가하고, 토픽에 잘 들어가는지 확인
```
http://watcher.haezoom.io:4000/topics/
```
<img width="1445" alt="스크린샷 2022-12-20 오전 11 08 42" src="https://user-images.githubusercontent.com/73451727/208594401-a82ae504-6779-4652-8cf2-7e463393f189.png">

 

참조) 

[Debezium connector for PostgreSQL :: Debezium Documentation](https://debezium.io/documentation/reference/stable/connectors/postgresql.html)

[Debezium PostgreSQL Source Connector for Confluent Platform | Confluent Documentation](https://docs.confluent.io/kafka-connectors/debezium-postgres-source/current/overview.html#clean-up-resources)

[debezium/user](https://gitter.im/debezium/user?at=5c894390ac408e1192541111)

