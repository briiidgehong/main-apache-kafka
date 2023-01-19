## ACL
https://docs.confluent.io/4.1.1/kafka/authorization.html

```
- Access Control List
- 일반적으로 네트워크 접근제어를 의미

- Apache Kafka는 모든 ACL을 저장하기 위해 
- Apache ZooKeeper를 사용하는 플러그형 권한 부여자를 함께 제공합니다.(=kafka-acls.sh) 
- ACL을 따로 설정하지 않으면 리소스에 대한 액세스가 슈퍼 사용자로 제한되기 때문에 ACL을 설정하는 것이 중요합니다. 
- (=기본 동작은 리소스에 연결된 ACL이 없는 경우 슈퍼 사용자를 제외한 누구도 리소스에 액세스할 수 없도록 합니다.)
```
