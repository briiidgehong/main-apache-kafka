# main-apache-kafka
main-apache-kafka <br/>
ref) [고승범님 테크블로그](https://www.popit.kr/author/peter5236) <br/>
ref) [레드햇/아파치 카프카란?](https://www.redhat.com/ko/topics/integration/what-is-apache-kafka) <br/>
ref) [kafka introduce video in 10 min](https://youtu.be/FKgi3n-FyNU) <br/>
     - 단순히 데이터의 상태를 저장하는것이 아닌 시계열 이벤트 자체를 기록한다는 컨셉 <br/>
     - 이벤트 기반 로그/데이터를 관리함으로써 실시간 분석/대응 등의 처리가 가능해짐 <br/>
ref) [confluent learn kafka](https://developer.confluent.io/learn-kafka) ***<br/>
ref) [tutorial video](https://www.youtube.com/watch?v=qu96DFXtbG4&list=PLa7VYi0yPIH0KbnJQcMv5N9iW8HkZHztH&index=2) <br/>
## - what's kafka?
```
아파치 카프카(Apache Kafka)는 아파치 소프트웨어 재단이 <스칼라>로 개발한 오픈 소스 메시지 브로커 프로젝트이다. 
이 프로젝트는 실시간 데이터 피드를 관리하기 위해 통일된, 높은 처리량, 낮은 지연시간을 지닌 플랫폼을 제공하는 것이 목표이다. 
요컨대 분산 트랜잭션 로그로 구성된, 상당히 확장 가능한 pub/sub 메시지 큐로 정의할 수 있으며
스트리밍 데이터를 처리하기 위한 기업 인프라를 위한 고부가 가치 기능이다.

<스칼라>는 자바 바이트코드를 사용하기 때문에 자바 가상 머신(JVM)에서 실행할 수 있고, 
Java 언어와 호환되어 대부분의 자바 API를 그대로 사용할 수 있다.
즉, 카프카는 JVM 위에서 돌아간다.

Apache Kafka는 실시간으로 기록 스트림을 게시, 구독, 저장 및 처리할 수 있는 분산형 데이터 스트리밍 플랫폼입니다. 
여러 소스에서 데이터 스트림을 처리하고 여러 사용자에게 전달하도록 설계되었습니다. 
간단히 말해 A지점에서 B지점까지 이동하는 것뿐만 아니라 A지점에서 Z지점을 비롯해 필요한 모든 곳에서 대규모 데이터를 동시에 이동할 수 있습니다.

Apache Kafka는 전통적인 엔터프라이즈 메시징 시스템의 대안입니다. 
하루에 1조 4천억 건의 메시지를 처리하기 위해 LinkedIn이 개발한 내부 시스템으로 시작했으나, 
현재 이는 다양한 기업의 요구 사항을 지원하는 애플리케이션을 갖춘 오픈소스 데이터 스트리밍 솔루션이 되었습니다.

마이크로서비스는 개발 환경을 바꾸어 놓았습니다. 
공유 데이터베이스 계층과 같은 종속성을 줄여 개발자들이 더욱 민첩하게 작업을 수행하도록 해줍니다. 
그러나 개발자가 구축 중인 분산형 애플리케이션이 데이터를 공유하려면 특정한 유형의 통합이 필요합니다. 
널리 사용되는 통합 옵션으로 동기식 방법이 있는데, 이는 서로 다른 사용자 간 데이터를 공유하는 데 애플리케이션 프로그래밍 인터페이스(API)를 활용합니다.

또 다른 통합 옵션으로는 중간 스토어에서 데이터를 복제하는 비동기식 방법이 있습니다. 
Apache Kafka는 바로 이런 맥락에 등장하는 솔루션으로, 
다른 개발팀의 데이터를 스트리밍하여 데이터 스토어를 채우면 해당 데이터를 여러 팀과 이들의 애플리케이션 간에 공유할 수 있게 됩니다.
```

## - why kafka?
```
- Monolithic -> MSA 로 아키텍쳐가 변환함에 따라 대두됨
- 전통적인 모놀리틱 아키텍쳐에서 당연했던 트렌잭션이나 데이터싱크 처리등이 별도로 필요하게됨
- 데이터 연동의 복잡성 증가 / 확장이 용이하지 못함
```
<img width="639" alt="스크린샷 2022-12-06 오후 4 12 50" src="https://user-images.githubusercontent.com/73451727/205845343-b71e5aed-16e8-4a88-917f-d1adfd747bea.png">
<img width="643" alt="스크린샷 2022-12-06 오후 4 13 00" src="https://user-images.githubusercontent.com/73451727/205845355-b6716947-f1fb-4f8a-8068-e9a6dcab6c2f.png">

## - kafka architecture
- single kafka broker
<img width="762" alt="스크린샷 2022-12-06 오후 4 41 15" src="https://user-images.githubusercontent.com/73451727/205850688-fd0119ca-dfb0-434c-a8eb-f298cb6f0c43.png">
- kafka cluster
<img width="782" alt="스크린샷 2022-12-06 오후 4 41 25" src="https://user-images.githubusercontent.com/73451727/205850695-1a535e93-e927-4003-8c51-4390529beac9.png">

### 각 구성요소
```
rf)
https://zeroco.tistory.com/105
```
#### 프로듀서(Producers)
```
카프카로 메시지를 보내는 역할을 하는 클라이언트를 총칭
```
#### 컨슈머(Consumers)
```
카프카에서 메시지를 꺼내가는 역할을 하는 클라이언트를 총칭
```

#### Zookeeper
```
카프카의 메타데이터(metadata) 관리 및 브로커의 정상상태 점검(health check) 을 담당
```
#### Brokers
```
카프카 애플리케이션이 설치된 서버 또는 노드를 의미
메시지를 저장하고 관리하는 역할
```
#### 카프카 / 카프카 클러스터
```
여러 대의 브로커를 구성한 클러스터를 의미
```

#### 토픽(Topic) / 파티션(Partition) / 세그먼트(Sagment) / 메시지 or 레코드 / 오프셋(Offset) 
```
- 토픽: 카프카는 메시지 피드들을 토픽으로 구분
       각 토픽의 이름은 카프카 내에서 고유

- 파티션: 병렬 처리 및 고성능을 얻기 위해 하나의 토픽을 여러 개로 나눈 것
        이렇게 하나를 여러 개로 나누면 분산 처리가 가능해지며, 파티션 수만큼 컨슈머를 연결할 수 있게 됨

- 세그먼트: 프로듀서에 의해 브로커로 전송된 메시지는 토픽의 파티션에 저장되며, 
          각 메시지들은 세그먼트(segment)라는 로그 파일의 형태로 브로커의 로컬 디스크에 저장되게 됨.

- 메시지 or 레코드: 프로듀서가 브로커로 전송하거나 컨슈머가 읽어가는 데이터 조각

- 리플리케이션: 각 메시지들을 여러 개로 복제해서 카프카 클러스터 내 브로커들에 분산시키는 동작을 의미
             이렇게 카프카 클러스터내 분산시키는 동작으로 브로커가 하나 종료되어도 카프카가 안정성을 유지할 수있다.
         
```
<img width="697" alt="스크린샷 2022-12-08 오후 2 16 58" src="https://user-images.githubusercontent.com/73451727/206362696-524b835e-3a5e-41cd-bfae-9fbd4c7032c0.png">

#### Offset / Commit
```
https://ggop-n.tistory.com/90

카프카의 컨슈머가 poll() 을 호출할 때마다, 컨슈머 그룹은 카프카에 저장되어 있지만 아직 읽지 않은 메시지들을 가져와 처리한다. 
이렇게 할 수 있는 것은 컨슈머 그룹이 카프카의 메시지를 어디까지 읽었는 지를 저장하고 있기 때문인데, 
어디까지 읽었는 지를 Offset 이라는 값으로 저장하게 된다. 

카프카에 저장되는 각 레코드들은 파티션 별로 독립적인 Offset 값을 가지게 되고, 
컨슈머 그룹이 파티션 별로 마지막으로 읽은 레코드의 Offset 을 저장함으로써 읽은 메시지와 읽지 않은 메시지를 구분한다.

그러면 컨슈머에 어떤 문제가 발생해 기존에 관리하던 오프셋 정보가 날아간다면? 
컨슈머들은 파티션 별로 모든 메시지를 다시 읽고 중복 처리해야 할까?
그렇지 않다. 카프카의 컨슈머 그룹은 위와 같은 문제가 발생하는 것을 막기 위해 Offset 을 내부적으로 저장하기도 하지만 
카프카 내에 별도로 내부적으로 사용하는 토픽을 생성하고, 그 토픽에 오프셋 정보를 저장하게 되어있다.

위와 같이 오프셋 정보를 카프카의 내부 토픽에 저장하는 것을 Commit 이라 하는데, 카프카에서는 커밋과 관련된 여러 방법을 제공한다.
```

<img width="500" alt="스크린샷 2022-12-09 오후 7 41 24" src="https://user-images.githubusercontent.com/73451727/206684329-720e6789-c133-4349-96cb-d3b1f8623ff8.png">

#### 카프카 커넥터 = 커넥트 + 커넥터(소스커넥터, 싱크커넥터)
```
rf)
https://yooloo.tistory.com/110 ***
https://minkwon4.tistory.com/319
https://bagbokman.tistory.com/8
https://cjw-awdsd.tistory.com/53

소스변경이나 추가없이 데이터와의 파이프라인을 구축하는것을 목적으로 만들어짐
standalone 모드에서는 cli로, distributed 모드에서는 rest api로 커넥트를 생성한다.

* 커넥트
카프카용 데이터 통합 프레임워크이다. 
커넥터가 동작하도록 실행해주는 프로세스이다.

* 커넥터
커넥트 내부의 실제 메시지 파이프라인이며 데이터를 실질적으로 처리한다.
커넥터에는 소스 커넥터(=프로듀서)/싱크 커넥터(=컨슈머) 가 존재한다.
이러한 커넥터들은 커넥트가 제공하는 REST API로 구성할수있다.

* 커넥트의 실행모드: standalone mode vs distributed mode
rf) https://developer.confluent.io/learn-kafka/kafka-connect/deployment/?_ga=2.106182275.1875207937.1670634794-2030527504.1670634794
커넥트가 standalone mode로 실행되면 커넥터=워커 프로세스는 단일노드에서 실행된다.
커넥트가 distributed mode로 실행되면 커넥터=워커 프로세스는 다중노드에서 실행된다.
스텐트얼론모드와 디스트리뷰트 모드는 커넥트 실행시 주게되는 환경변수를 통해 조정될수 있다.
각각의 환경변수는 connect-distributed.properties / connect-standalone.properties 에 잘 정의되어 있음
confluentinc/cp-kafka-connect 해당 컨테이너 이미지 사용시에도, 위의 프로퍼티를 참조해서 컨테이너 환경변수들을 조정해 모드를 다르게 사용할 수 있다.

- standalone 모드
     bin/connect-standalone.sh 
     config/connect-standalone.properties
     
     커넥터 구성은 CLI를 사용함
     로컬 시스템에서 Kafka Connect를 개발하고 테스트하는 데 유용
     일반적으로 단일 에이전트를 사용하는 환경에 사용
     독립 실행형 worker 상태는 로컬 파일 시스템에 저장
      
- distributed 모드
     bin/connect-distributed.sh 
     config/connect-distributed.properties
     
     커넥터 구성은 REST API를 사용함
     여러 시스템(노드)에서 Connect worker를 실행
     Connect 클러스터를 구성
     클러스터 전체에 커넥터를 배포
     필요에 따라 노드를 추가하거나 제거할 수 있음
     노드가 예기치 않게 클러스터에서 제거되는 경우 
     Kafka Connect는 해당 노드의 작업을 클러스터의 다른 노드에 자동으로 배포
     Kafka Connect는 복제되는 Kafka 클러스터 내부에 
     커넥터 구성, 상태 및 오프셋 정보를 저장
     Connect worker를 실행하는 노드가 손실되더라도 데이터가 손실되지 않음
     분산형 worker 상태는 Kafka에 저장
     
     
- 소스 커넥터 == 프로듀서
data source에 담긴 데이터를 topic에 담는 역할(Producer)을 하는 connector
{
    "name": "my-source-connect",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:mysql://localhost:3306/test",
        "connection.user":"root",
        "connection.password":"비밀번호",
        "mode":"incrementing",
        "incrementing.column.name" : "id",
        "table.whitelist" : "users", # !!데이터 변경을 감지할 table 이름!!
        "topic.prefix" : "example_topic_",
        "tasks.max" : "1",
    }
}

- 싱크 커넥터 == 컨슈머
topic에 담긴 데이터를 특정 data source로 보내는 역할(Consumer 역할)을 하는 connector
{
    "name": "my-pksink-connect",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
        "connection.url": "jdbc:mysql://localhost:3306/test",
        "connection.user":"root",
        "connection.password":"비밀번호",
        "auto.create":"true", # !!데이터를 넣을 테이블이 누락되었을 경우 자동 테이블 생성 여부!!
        "auto.evolve":"true",
        "delete.enabled":"false",
        "tasks.max":"1",
        "topics":"example_topic_users"
    }
}
```
<img width="812" alt="스크린샷 2022-12-08 오후 1 08 46" src="https://user-images.githubusercontent.com/73451727/206354399-29ce192d-d5f6-4dc4-9d3d-579c97ae0cb7.png">

#### 카프카 스트림즈
```
rf) 
https://marrrang.tistory.com/63

컨슈머로 받아와서 처리하는 것보다 더 빠르고 안전하게 실시간으로 처리할 수 있게 
카프카에서 지원해준 것이 Kafka Streams입니다.
어떤 Topic으로 들어오는 데이터를 Consume하여 Kafka Streams에서 제공하는 처리 로직을 통해
처리 후 다른 Topic으로 전송하거나 끝내는 부분을 수행해주는 라이브러리입니다.

- 카프카에 저장된 데이터를 처리하고 분석하기 위해 개발된 자바 라이브러리

- 이렇게 라이브러리로 제공되니까 JVM 기반 언어중 아무 언어를 선택해서 사용해도 무관합니다.

- 데이터 유실과 중복처리 되지 않고 딱 1번만 처리되는 것을 보장한다.

- 스케쥴링 도구가 필요없다.
  Kafka Streams는 다른 것 필요없이 스트림즈 어플리케이션만 가지고 사용할 수 있습니다.
  
- 이벤트 처리 기능 Streams DSL, Processor API 제공
  이벤트 기반 데이터 처리에 필요한 기능들을 제공하기 때문에 스트림즈를 구현하기 편하다.
  
- 자체 로컬 상태 저장소를 사용한다.
  상태 기반 처리를 도와주기 위해 rocksDB를 로컬에서 사용하여 상태를 저장한다.
  로컬 DB에 저장한 상태에 대한 변환 정보는 카프카 변경로그에 저장한다.
  이를 통해 프로세스에 장애가 발생하더라도 상태가 모두 안전하게 저장되기 때문에 
  장애 복구를 할 수 있다.

```
<img width="756" alt="스크린샷 2022-12-09 오후 2 12 52" src="https://user-images.githubusercontent.com/73451727/206628953-79eaa790-9dbe-4940-abb0-42064226fe3b.png">

#### 스키마 레지스트리
```
rf)
https://always-kimkim.tistory.com/entry/kafka101-schema-registry

프로듀서는 직렬화하여 메시지를 발행하고, 컨슈머는 역직렬화하여 메시지를 구독합니다.
따라서 프로듀서와 컨슈머에 각각 스키마(=메시지 구조)에 따라 직렬화/역직렬화 클래스가 구성되고,
이 둘은 강한 의존성(커플링, Coupling)을 갖게 됩니다. 
구조적인 결합도는 낮췄지만 내부적인 결합도는 여전히 가지고 있게 됩니다. 

스키마 레지스트리는 이 스키마(메시지 구조)의 결합도를 낮추기 위해 고안되었습니다. 
스키마 레지스트리는 별도의 웹 어플리케이션 형태로 구성되며, 기능은 다음과 같습니다.
1. 토픽 별 메시지 Key 또는 Value 스키마 버전 관리
2. 스키마 호환성 규칙 강제 *
   운영자는 스키마를 등록하여 사용할 수 있음
   스키마 버전 별 호환성을 강제함으로써 운영 규칙을 설정함
   호환성의 종류에는 Backward / Forward / Full / None 4가지가 존재한다. 
   Backward: 컨슈머는 2번 스키마로 메시지를 처리하지만 1번 스키마도 처리할 수 있습니다
             필드 삭제 혹은 기본 값이 있는 필드 추가인 경우
   Forward: 컨슈머는 1번 스키마로 메시지를 처리하지만 2번 스키마도 처리할 수 있습니다.
            필드 추가 혹은 기본 값이 있는 필드 삭제
   Full: Backward와 Forward를 모두 가집니다.
         기본 값이 있는 필드를 추가 혹은 삭제
   None: 스키마 호환성을 체크하지 않습니다.
   
3. 스키마 버전 조회

```


## - 실습1. QuickStart (confluent 내장 file streams connector 사용)
https://kafka.apache.org/quickstart
```
cd kafka_2.13-3.3.1

# 쥬키퍼 실행
bin/zookeeper-server-start.sh config/zookeeper.properties

# 클러스터 UUID 생성
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

# 로그 디렉토리 포맷
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties

# 카프카 서버 시작
bin/kafka-server-start.sh config/kraft/server.properties

# 토픽 생성 (quickstart-events)
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092

# 생성된 토픽 확인
bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092

# 토픽에 이벤트 입력
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
>first event input!
>second event input!
>third event input!
>stream event input!

# 토픽에서 이벤트 읽기
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
>first event input!
>second event input!
>third event input!
>stream event input!

# 커넥터 연결
     # 소스커넥터에 물릴 test.txt 생성
     echo -e "foo\nbar" > test.txt

     * 커넥트 standalone mode로 실행
          vi config/connect-standalone.properties
               plugin.path=libs/connect-file-3.3.1.jar

          # 커넥트 실행 + 커넥터 생성
          bin/connect-standalone.sh 
          config/connect-standalone.properties # 커넥트 구성
          config/connect-file-source.properties # 소스 커넥터 구성
          config/connect-file-sink.properties # 싱크 커넥터 구성

     * 커넥트 distributed mode로 실행
          vi config/connect-distributed.properties
               plugin.path=libs/connect-file-3.3.1.jar

          # 커넥트 실행
          bin/connect-distributed.sh 
          config/connect-distributed.properties # 커넥트 구성

          # REST API로 소스커넥터/싱크커넥터 생성
          # todo: file stream connector 기반 커넥터 생성 (rest api)

     # 싱크커넥터에서 최종적으로 쌓은 데이터 확인
     cat test.sink.txt 
     
     # 실시간 반영 확인
     echo Another line 345>> test.txt
     cat test.sink.txt
     > foo
     > bar
     > Another line 345
     
     # 토픽 데이터 조회시 커넥터에서 실시간으로 반영해주는 내용 조회 가능
     bin/kafka-console-consumer.sh 
     --bootstrap-server localhost:9092 
     --topic connect-test 
     --from-beginning
     {"schema":{"type":"string","optional":false},"payload":"foo"}
     {"schema":{"type":"string","optional":false},"payload":"bar"}
     {"schema":{"type":"string","optional":false},"payload":"stream !!"}
     {"schema":{"type":"string","optional":false},"payload":"stream2 !!"}
     {"schema":{"type":"string","optional":false},"payload":"Another line 345"}
     
```

## - 실습2. Docker-compose 환경 (dbzium external postgresql jdbc connector 사용)
```
- services
       kafka-ui
       zookeeper0
       kafka0
       schemaregistry0
       zookeeper1
       kafka1
       schemaregistry1
       kafka-connect0 # distribute mode에 해당하는 환경변수로 실행된다.
       kafka-init-topics

zookeeper -> kafka -> schemaregistry -> kafka-connect
                   -> kafka-init-topics
```
## - 실습2-1. 기본 default producer / consumer
```
pip install confluent_kafka
pip install kafka-python

default_producer.py
default_consumer.py
```
## - 실습2-2. postgresql 기반 producer / consumer
### - 커넥터 플러그인 추가
```
rf) https://rmoff.net/2020/06/19/how-to-install-connector-plugins-in-kafka-connect/

방식1. 로컬 경로에 커넥터 jdbc 다운받아서 볼륨으로 컨테이너에 전달
- https://debezium.io/releases/1.9/ 에서 postgresql 용 jdbc 다운로드
- plugin path에 해당 경로 설정해놓음으로써 커넥트 실행시, 커넥터 플러그인 설치
kafka-connect0:
     volumes:
      - ./connector_lib:/usr/share/confluent-hub-components
     environment:
      CONNECT_PLUGIN_PATH: "/usr/share/java,/usr/share/confluent-hub-components/"
 
방식2. 컨테이너 실행시 command로 plugin path에 직접 설치
```

### - 추가된 플러그인 확인
```
# 사용할 수 있는 커넥터 플러그인
curl http://localhost:8083/connector-plugins
[{"class":"io.debezium.connector.postgresql.PostgresConnector","type":"source","version":"1.9.0.Final"}
{"class":"org.apache.kafka.connect.file.FileStreamSinkConnector","type":"sink","version":"6.0.1-ccs"}
{"class":"org.apache.kafka.connect.file.FileStreamSourceConnector","type":"source","version":"6.0.1-ccs"}
{"class":"org.apache.kafka.connect.mirror.MirrorCheckpointConnector","type":"source","version":"1"}
{"class":"org.apache.kafka.connect.mirror.MirrorHeartbeatConnector","type":"source","version":"1"}
{"class":"org.apache.kafka.connect.mirror.MirrorSourceConnector","type":"source","version":"1"}]
```

### - postgresql db setting - wal_level = logical 로 변경
```
rf) https://access.redhat.com/documentation/ko-kr/red_hat_integration/2020.q1/html/debezium_user_guide/debezium-connector-for-postgresql
2.2. Setting up PostgreSQL
This release of Debezium only supports the native pgoutput logical replication stream.

Debezium postgresql connector는 postgresql wal_level=logical에서 동작하도록 되어있다.
다른 레벨로 설정된 경우 logical 레벨로 변경해주도록 하자.

SHOW wal_level;

aws rds의 경우, db parameter group에서 <rds.logical_replication = 1> 로 바꿔주면 된다.

```
<img width="1357" alt="스크린샷 2022-12-12 오전 10 29 41" src="https://user-images.githubusercontent.com/73451727/206942545-529d56c7-96a5-4ff7-94a6-8107b627ef73.png">

### - 소스 커넥터 생성
<img width="856" alt="스크린샷 2023-01-19 오전 11 19 10" src="https://user-images.githubusercontent.com/73451727/213340183-2a230c51-8e72-4411-92a8-5ecb7a341b5d.png">

```
{
  "name": "debezium-connector-test",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "#####.ap-northeast-1.rds.amazonaws.com",
    "database.port": "#####",
    "database.user": "#####",
    "database.password": "#####",
    "database.dbname": "postgres",
    "database.server.name": "test-dbserver",
    "plugin.name": "pgoutput",
    "slot.name" : "testslot"
  }
}
```

### - 생성된 커넥터 리스트 조회
```
curl http://localhost:8083/connectors
["debezium-connector-test"]

```

### - postgresql replication slot 조회
```
{
"select * from pg_replication_slots": [
	{
		"slot_name" : "testslot",
		"plugin" : "pgoutput",
		"slot_type" : "logical",
		"datoid" : 14301,
		"database" : "postgres",
		"temporary" : false,
		"active" : true,
		"active_pid" : 580,
		"xmin" : null,
		"catalog_xmin" : "583",
		"restart_lsn" : "0\/80017F8",
		"confirmed_flush_lsn" : "0\/8001830",
		"wal_status" : "reserved",
		"safe_wal_size" : null
	}
]}
```

## - 실습2-3. kafka streams with faust-streaming
pip install faust-streaming (>python 3.6)



streams_test_producer.py
```
# ==========================================
# PRODUCER
# ==========================================
from confluent_kafka import Producer
from time import sleep
from random import random
import json

conf = {"bootstrap.servers": "localhost:9092"}
producer = Producer(conf)
topic = "faust_stream_data_11"
counter = 1

while True:
    data = {
        "plant_name": "지영발전소",
        "plant_id": 99,
        "type": "per_second",
        "generation": 99 + random(),
    }
    producer.produce(topic, value=json.dumps(data))
    print("Sample #{} produced!".format(counter))
    counter += 1
    producer.flush(1)
    sleep(1)
```


python streams_test_producer.py 로 테스트 데이터 생성
```
Sample #1 produced!
Sample #2 produced!
Sample #3 produced!
Sample #4 produced!
Sample #5 produced!
```


streams_app.py
```
import faust
import logging
from asyncio import sleep

log = logging.getLogger(__name__)


class Plant(faust.Record):
    plant_name: str
    plant_id: int
    type: str
    generation: float


app = faust.App('myapp', broker='kafka://localhost:9092')
source_topic = app.topic('faust_stream_data_11', value_type=Plant)
destination_topic = app.topic('faust_stream_data_12', value_type=Plant)



# specify the source_topic and destination_topic to the agent
@app.agent(source_topic, sink=[destination_topic])
async def hello(messages):
    async for message in messages:
        if message is not None:
            log.info(message.plant_name)
            log.info(message.plant_id)
            log.info(message.type)
            log.info(message.generation)

            message.generation += 1000

            # the yield keyword is used to send the message to the destination_topic
            yield Plant(plant_name=message.plant_name, 
            plant_id=message.plant_id,
            type=message.type,
            generation=message.generation)

            # sleep for 2 seconds
            await sleep(2)
        else:
            log.info('No message received')

if __name__ == '__main__':
    app.main()
```


faust app 실행: faust -A streams_test worker -l info 
```
┌ƒaµS† v0.10.0┬──────────────────────────────────────────────────────────┐
│ id          │ myapp                                                    │
│ transport   │ [URL('kafka://localhost:9092')]                          │
│ store       │ memory:                                                  │
│ web         │ http://jyhong-laptop.local:6066                          │
│ log         │ -stderr- (info)                                          │
│ pid         │ 40086                                                    │
│ hostname    │ jyhong-LAPTOP.local                                      │
│ platform    │ CPython 3.8.15 (Darwin x86_64)                           │
│        +    │ Cython (Clang 14.0.6 )                                   │
│ drivers     │                                                          │
│   transport │ aiokafka=0.8.0                                           │
│   web       │ aiohttp=3.8.3                                            │
│ datadir     │ /Users/jyhong/production/main-apache-kafka/myapp-data    │
│ appdir      │ /Users/jyhong/production/main-apache-kafka/myapp-data/v1 │
└─────────────┴──────────────────────────────────────────────────────────┘
```


streams_app.py 의 source_topic와 destination_topic을 변경해가면서 가공된 데이터를 다시 가공해서 새로운 토픽에 쌓는다. 스트림즈를 이용해 이러한 가공을 몇번이고 반복해서 새로운 토픽에 쌓아둘수 있다.
```
source_topic = app.topic('faust_stream_data_11', value_type=Plant)
destination_topic = app.topic('faust_stream_data_12', value_type=Plant)

[2022-12-12 16:40:01,471] [40086] [INFO] 지영발전소
[2022-12-12 16:40:01,471] [40086] [INFO] 99
[2022-12-12 16:40:01,471] [40086] [INFO] per_second
[2022-12-12 16:40:01,471] [40086] [INFO] 99.02870978165157
[2022-12-12 16:40:01,485] [40086] [WARNING] Topic faust_stream_data_12 is not available during auto-create initialization
[2022-12-12 16:40:03,592] [40086] [INFO] 지영발전소
[2022-12-12 16:40:03,593] [40086] [INFO] 99
[2022-12-12 16:40:03,593] [40086] [INFO] per_second
[2022-12-12 16:40:03,593] [40086] [INFO] 99.04947539974322


source_topic = app.topic('faust_stream_data_12', value_type=Plant)
destination_topic = app.topic('faust_stream_data_13', value_type=Plant)

[2022-12-12 16:40:31,510] [40280] [INFO] 지영발전소
[2022-12-12 16:40:31,510] [40280] [INFO] 99
[2022-12-12 16:40:31,511] [40280] [INFO] per_second
[2022-12-12 16:40:31,511] [40280] [INFO] 1099.0287097816515
[2022-12-12 16:40:31,525] [40280] [WARNING] Topic faust_stream_data_13 is not available during auto-create initialization
[2022-12-12 16:40:33,631] [40280] [INFO] 지영발전소
[2022-12-12 16:40:33,632] [40280] [INFO] 99
[2022-12-12 16:40:33,632] [40280] [INFO] per_second
[2022-12-12 16:40:33,632] [40280] [INFO] 1099.0494753997432
[2022-12-12 16:40:35,634] [40280] [INFO] 지영발전소
[2022-12-12 16:40:35,634] [40280] [INFO] 99
[2022-12-12 16:40:35,634] [40280] [INFO] per_second
[2022-12-12 16:40:35,634] [40280] [INFO] 1099.9242704149892
```


