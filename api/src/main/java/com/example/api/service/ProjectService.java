package com.example.api.service;

import com.example.api.domain.Project;
import com.example.api.repository.ProjectRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProjectService {

    private final ProjectRepository projectRepo;

    public ProjectService(ProjectRepository projectRepo) {
        this.projectRepo = projectRepo;
    }

    // 모든 프로젝트 조회
    public List<Project> findAll() {
        return (List<Project>) projectRepo.findAll();
    }
}
