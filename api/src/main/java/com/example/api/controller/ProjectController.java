package com.example.api.controller;

import com.example.api.domain.Project;
import com.example.api.service.ProjectService;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/projects")
public class ProjectController {

    private final ProjectService projectService;

    @Autowired
    public ProjectController(ProjectService projectService) {
        this.projectService = projectService;
    }

    @GetMapping
    public List<Project> findAllProjects() {
        return projectService.findAll();
    }

    @PostMapping
    public ResponseEntity<?> launchProject(@RequestBody Project project) {
        try {
            Project launched = projectService.launch(project);
            return ResponseEntity.status(HttpStatus.CREATED).body(launched);
        } catch (DataIntegrityViolationException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("Cannot add project that already exists codename");
        }
    }

    @PutMapping("/{pj_id}")
    public ResponseEntity<String> modifyProject(@PathVariable("pj_id") int projectId,
                                                @RequestBody Project project) {
        try {
            projectService.modify(projectId, project.getCodeName());
            return ResponseEntity.ok("Project modified successfully.");
        } catch (EntityNotFoundException e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body("Project not found.");
        } catch (DataIntegrityViolationException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("Cannot update to the codename that already exists.");
        }
    }

    @DeleteMapping("/{pj_id}")
    public ResponseEntity<String> dropProject(@PathVariable("pj_id") int projectId) {
        try {
            projectService.drop(projectId);
            return ResponseEntity.ok("Project dropped successfully.");
        } catch (EntityNotFoundException e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Project not found.");
        }
    }
}
