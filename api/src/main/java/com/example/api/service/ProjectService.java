package com.example.api.service;

import com.example.api.domain.Project;
import com.example.api.repository.ProjectRepo;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProjectService {

    private final ProjectRepo projectRepo;

    public ProjectService(ProjectRepo projectRepo) {
        this.projectRepo = projectRepo;
    }

    // 모든 프로젝트 조회
    public List<Project> findAll() {
        return projectRepo.readAll();
    }
}
