package com.example.api.service;

import com.example.api.domain.Schedule;
import com.example.api.repository.ScheduleRepository;
import org.springframework.stereotype.Service;

import java.util.List;


@Service
public class ScheduleService {
    private final ScheduleRepository scheduleRepo;

    public ScheduleService(ScheduleRepository scheduleRepo) {
        this.scheduleRepo = scheduleRepo;
    }

    // 모든 스케쥴 조회
    public List<Schedule> findAll() {
        return (List<Schedule>) scheduleRepo.findAll();
    }
}
