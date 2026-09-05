package com.aetherforge.repo;
import org.springframework.jdbc.core.JdbcTemplate;import org.springframework.stereotype.Repository;import java.util.*;
@Repository public class UserRepository {private final JdbcTemplate db;public UserRepository(JdbcTemplate db){this.db=db;}public Map<String,Object> byEmail(String e){return db.queryForMap("select id,email,full_name,password_hash,role from app_user where lower(email)=lower(?)",e);}public List<Map<String,Object>> users(){return db.queryForList("select id,email,full_name,role,created_at from app_user order by full_name");}}
