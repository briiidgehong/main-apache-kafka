## Burrow - kafka consumer lag monitoring

```
ref.
https://blog.voidmainvoid.net/243
https://blog.voidmainvoid.net/279
https://www.youtube.com/watch?v=b3i6D4eeBGw
```
## - Burrow 란?
- kafka를 개발한 linkedin에서 만든 consumer lag monitoring tool

## - kafka consumer lag 이란?
- 토픽의 가장 최신 오프셋과 컨슈머 오프셋간의 차이
<img width="959" alt="스크린샷 2023-01-16 오후 6 02 10" src="https://user-images.githubusercontent.com/73451727/212638717-4989a198-a55a-4ffd-9fe0-2eb3a724433f.png">
<img width="249" alt="스크린샷 2022-12-29 오후 5 10 34" src="https://user-images.githubusercontent.com/73451727/209922761-98c1bba9-8d2a-448f-92dc-3c1123702715.png">

## - lag 실시간 모니터링
- 데이터를 Elasticsearch나 influxdb와 같은 저장소에 넣은뒤
- grafana와 같은 시각화 대시보드를 사용해 시각화 한다.
<img width="272" alt="스크린샷 2022-12-29 오후 5 17 55" src="https://user-images.githubusercontent.com/73451727/209923548-7ff5ed01-8139-4f2e-ab6b-9669a59f4822.png">

## - Burrow 를 사용해야 하는 이유
- consumer 단위에서 lag을 모니터링하는것은 위험
- 왜? 컨슈머 로직단에서 lag을 수집하는것은 컨슈머에 대한 디펜던시가 걸려있다.
- 즉, 컨슈머가 정상동작하지 않을경우(혹은 비정상종료 될 경우) 컨슈머는 lag 정보를 보낼수 없다.
- 추가적으로 컨슈머가 개발될 때마다 해당 컨슈머에 lag 정보를 특정 저장소에 저장할 수 있도록 로직을 개발해야함
- 그래서 컨슈머와 독립적인 모니터링 애플리케이션인 burrow 를 사용

## - 특징
> 1. 멀티 카프카 클러스터 지원 - 하나의 burrow로 여러개의 클러스터 모니터링 가능
> 2. sliding window를 통한 컨슈머의 status 를 확인해줌 (error/warning/ok)
> - 데이터양이 많아지면서 컨슈머 오프셋이 증가하면 warning
> - 데이터양이 많아지는대 컨슈머가 데이터를 가져가지 않으면 error
> 3. http api 제공
> - api를 호출해서 받은 데이터를 시계열db와 같은곳에 저장하는대 활용한다.

## - burrow - telegraf - elasticsearch - grafana
```
- burrow를 사용하여 lag정보를 Elasticsearch로 수집하는 데이터파이프라인 구현
- Grafana 기반의 consumer단위 lag 모니터링 대시보드 구현
- lag증가에 따른 Slack alert를 받는 기능의 구현
```

## - [HTTP API ENDPOINT](https://github.com/linkedin/Burrow/wiki/HTTP-Endpoint)

### # burrow
```
linkedin에서 공개한 opensource lag monitoring application입니다. rest api를 통해 lag 정보를 전달받을 수 있습니다.
```
### # telegraf
```
데이터의 수집 및 전달에 특화된 agent입니다. configuration설정을 통해 burrow의 데이터를 ES에 넣는 역할을 합니다.
```
### # elasticsearch
```
kafka lag 데이터를 저장하는 역할을 합니다.
```
### # grafana
```
ES의 데이터를 시각화하고 threshold를 설정하여 slack alert를 보낼 수 있는 대시보드 tool입니다.
```
