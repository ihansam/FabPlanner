package com.example.api.repository;

import com.example.api.domain.Project;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;

@Repository
public class MemoryProjectRepo implements ProjectRepo{

    private List<Project> dummyProjects = new ArrayList<>();

    public MemoryProjectRepo() {
        dummyProjects.add(new Project(0, "M2MacBookAir15"));
        dummyProjects.add(new Project(1, "M3MacBookPro13"));
    }

    public List<Project> readAll() {
        return dummyProjects;
    }
}
