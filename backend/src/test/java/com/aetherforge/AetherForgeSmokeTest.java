package com.aetherforge;
import org.junit.jupiter.api.Test;import org.springframework.boot.test.context.SpringBootTest;
@SpringBootTest(properties={"spring.datasource.url=jdbc:h2:mem:testdb;MODE=PostgreSQL","spring.datasource.driver-class-name=org.h2.Driver","spring.datasource.username=sa","spring.datasource.password=","spring.flyway.enabled=false"})
class AetherForgeSmokeTest {@Test void contextLoads() {}}
