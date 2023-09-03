package com.example.api.controller;

import com.example.api.domain.Schedule;
import com.example.api.service.ScheduleService;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/schedules")
public class ScheduleController {
    private final ScheduleService scheduleService;

    @Autowired
    public ScheduleController(ScheduleService scheduleService) {
        this.scheduleService = scheduleService;
    }

    @GetMapping
    public List<Schedule> findAllSchedules() {
        return scheduleService.findAll();
    }

    @GetMapping("/project")
    public List<Schedule> findProjectSchedules(@RequestParam("id") int projectId) {
        return scheduleService.findByProject(projectId);
    }

    @PostMapping("/project")
    public ResponseEntity<?> addScheduleToProject(@RequestParam("id") int projectId,
                                                  @RequestBody Schedule schedule) {
        try {
            Schedule added = scheduleService.add(projectId, schedule);
            return ResponseEntity.status(HttpStatus.CREATED).body(added);
        } catch (DataIntegrityViolationException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("Cannot add schedule that already exists type in project");
        } catch (IllegalArgumentException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("Schedule dates should be ascending");
        }
    }

    @PatchMapping("/{sjId}")
    public ResponseEntity<String> modifySchedule(@PathVariable("sjId") int scheduleId,
                                                 @RequestBody Schedule schedule) {
        try {
            scheduleService.modify(scheduleId, schedule);
            return ResponseEntity.ok("Schedule modified successfully.");
        } catch (EntityNotFoundException e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body("Schedule not found");
        } catch (DataIntegrityViolationException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("Cannot add schedule that already exist type in project");
        } catch (IllegalArgumentException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                    .body("Schedule dates should be ascending");
        }
    }

    @DeleteMapping("/{sjId}")
    public ResponseEntity<String> cancelSchedule(@PathVariable("sjId") int scheduleId) {
        try {
            scheduleService.cancel(scheduleId);
            return ResponseEntity.ok("Schedule canceled successfully.");
        } catch (EntityNotFoundException e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Schedule not found.");
        }
    }
}
