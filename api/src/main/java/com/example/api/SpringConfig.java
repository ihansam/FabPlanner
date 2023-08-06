package com.example.api;

import com.example.api.repository.MemoryProjectRepo;
import com.example.api.repository.ProjectRepo;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringConfig {
    @Bean
    public ProjectRepo projectRepo(){
        return new MemoryProjectRepo();
    }
}
