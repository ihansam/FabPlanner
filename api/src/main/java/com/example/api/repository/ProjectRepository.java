package com.example.api.repository;

import com.example.api.domain.Project;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ProjectRepository extends CrudRepository<Project, Integer> {
    Optional<Project> findByCodeName(String codeName);
}
