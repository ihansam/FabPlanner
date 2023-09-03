package com.example.api.service;

import com.example.api.domain.Project;
import com.example.api.repository.ProjectRepository;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.dao.DataIntegrityViolationException;
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

    // 한 프로젝트 조회
    public Project findById(int projectId){
        return projectRepo.findById(projectId)
                .orElseThrow(EntityNotFoundException::new);
    }

    // 중복 점검
    public void validateProjectNameExist(Project project) {
        projectRepo.findByCodeName(project.getCodeName())
                .ifPresent(m->{
                    throw new DataIntegrityViolationException("Cannot add codename that already exists");
                });
    }

    // 프로젝트 개시
    public Project launch(Project project) {
        validateProjectNameExist(project);
        return projectRepo.save(project);
    }

    // 프로젝트 갱신
    public Project modify(int projectId, String codeName) {
        Project projectToUpdate = projectRepo.findById(projectId)
                .orElseThrow(() -> new EntityNotFoundException("Project not found"));

        projectToUpdate.setCodeName(codeName);
        validateProjectNameExist(projectToUpdate);

        return projectRepo.save(projectToUpdate);
    }

    // 프로젝트 삭제
    public void drop(int projectId) {
        Project projectToDelete = projectRepo.findById(projectId)
                .orElseThrow(() -> new EntityNotFoundException("Project not found"));

        projectRepo.delete(projectToDelete);
    }
}
