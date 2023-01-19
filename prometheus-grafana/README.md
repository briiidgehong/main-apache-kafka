## 참조 
```
https://github.com/vegasbrianc/prometheus
https://www.confluent.io/blog/monitor-kafka-clusters-with-prometheus-grafana-and-confluent/
https://docs.aws.amazon.com/ko_kr/msk/latest/developerguide/open-monitoring.html

```

## msk - prometheus - grafana
> Prometheus가 Kafka의 다양한 정보를 긁어 내고 Prometheus를 데이터 소스로 사용하여 Grafana에서 표현하자.

### - 프로메테우스란?
Prometheus는 메트릭 수집, 시각화, 알림, 서비스 디스커버리 기능을 모두 제공하는 오픈 소스 모니터링 시스템이다. <br/>
- 매트릭: 일반적으로 그래프등으로 수치화 할수 있는 시계열 데이터를 말한다. <br/>
- CPU사용량/메모리 부하/시간당 데이터 처리량/분당 네트워크 속도 등의 서버 데이터 <br/>
<br/>
- Prometheus는 수백 개의 엔드포인트를 스크랩하면서 여러 플랫폼 메트릭을 집계하는 데 사용되는 도구입니다. <br/>
- 스크랩 및 집계 사용 사례를 위해 특별히 제작되었습니다. <br/>
- 내부적으로 최적화된 방식으로 시분할 데이터를 저장하고 검색할 수 있는 시계열 데이터 저장소를 포함합니다. <br/>
- 또한 OpenMetrics 형식 을 사용합니다 . <br/>
- 최근에 v1.0에 도달한 CNCF 샌드박스 프로젝트로 많은 도구가 이를 지원하거나 지원할 계획이므로 관심을 끌 것으로 예상됩니다. <br/>
- Prometheus 커뮤니티에서 만들고 활용하는 메트릭 내보내기는 이미 이러한 표준을 준수합니다. <br/>
-  Grafana는 Prometheus와 동기화시켜 그래프를 렌더링하는 오픈 소스 차트 및 대시보드 도구입니다. <br/>



### - 로컬 테스트
```
docker run -p 9090:9090 prom/prometheus
http://localhost:9090/
```
<img width="885" alt="스크린샷 2022-12-21 오후 1 35 32" src="https://user-images.githubusercontent.com/73451727/208822211-0eeef3d9-2924-409b-b643-c9ff237ce70a.png">

### - MSK - 프로메테우스(EC2 설치)
<img width="633" alt="스크린샷 2023-01-19 오전 11 57 53" src="https://user-images.githubusercontent.com/73451727/213345454-f74f9597-2552-4f3e-b004-0ea1bccc3cfb.png">

```
# EC2에 프로메테우스 띄우기
sudo apt-get update
wget https://github.com/prometheus/prometheus/releases/download/v2.37.0/prometheus-2.37.0.linux-amd64.tar.gz
tar xf prometheus-2.37.0.linux-amd64.tar.gz 
cd prometheus-2.37.0.linux-amd64/

sudo vi prometheus.yml
  # my global config
  global:
    scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
    evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
    # scrape_timeout is set to the global default (10s).

  # Alertmanager configuration
  alerting:
    alertmanagers:
      - static_configs:
          - targets:
            # - alertmanager:9093

  # Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
  rule_files:
    # - "first_rules.yml"
    # - "second_rules.yml"

  # A scrape configuration containing exactly one endpoint to scrape:
  # Here it's Prometheus itself.
  scrape_configs:
    # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
    - job_name: "prometheus"

      # metrics_path defaults to '/metrics'
      # scheme defaults to 'http'.

      static_configs:
        - targets: ["localhost:9090"]
    - job_name: 'broker'
      file_sd_configs:
        - files:
          - 'targets.json'
   
sudo vi targets.json
  [
    {
      "labels": {
        "job": "jmx"
      },
      "targets": [
        "b-1-#####ap-northeast-2.amazonaws.com:11001",
        "b-2-#####.ap-northeast-2.amazonaws.com:11001"
      ]
    },
    {
      "labels": {
        "job": "node"
      },
      "targets": [
        "b-1-#####.ap-northeast-2.amazonaws.com:11002",
        "b-2-#####.ap-northeast-2.amazonaws.com:11002"
      ]
    }
  ]

# 프로메테우스 서비스 실행
./prometheus
```
<img width="1760" alt="스크린샷 2023-01-19 오전 11 58 42" src="https://user-images.githubusercontent.com/73451727/213345473-8417741d-4069-4db3-9e90-ba051656c0c1.png">


```
# grafana에서 datasource 로 prometheus 연결


```
### - MSK - 프로메테우스(docker-compose)
[add docker-compose](https://github.com/briiidgehong/main-apache-kafka/commit/0e82ccb13c0666af5b445e6062163be87f7e8155)
