package com.example.api.repository;

import com.example.api.domain.Schedule;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ScheduleRepository extends CrudRepository<Schedule, Integer> {

    List<Schedule> findByProject_PjId(int projectId);

    List<Schedule> findByTypeAndProject_PjId(String type, int projectId);
}
