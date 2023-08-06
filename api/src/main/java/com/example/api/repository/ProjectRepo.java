package com.example.api.repository;

import com.example.api.domain.Project;

import java.util.List;

public interface ProjectRepo {
    List<Project> readAll();
}
