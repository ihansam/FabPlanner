package com.example.api.service;

import com.example.api.domain.Project;
import com.example.api.domain.Schedule;
import com.example.api.repository.ScheduleRepository;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;


@Service
public class ScheduleService {
    private final ScheduleRepository scheduleRepo;
    private final ProjectService projectService;

    public ScheduleService(ScheduleRepository scheduleRepo,
                           ProjectService projectService) {
        this.scheduleRepo = scheduleRepo;
        this.projectService = projectService;
    }

    // 모든 스케쥴 조회
    public List<Schedule> findAll() {
        return (List<Schedule>) scheduleRepo.findAll();
    }

    // 프로젝트에 대한 스케줄 조회
    public List<Schedule> findByProject(int projectId){
        return scheduleRepo.findByProject_PjId(projectId);
    }

    // 프로젝트에 대한 새 스케쥴 생성
    public Schedule add(int projectId, Schedule schedule) {
        validateSchedule(projectId, schedule);
        Project project = projectService.findById(projectId);
        schedule.setProject(project);
        return scheduleRepo.save(schedule);
    }

    // 스케쥴 갱신
    public Schedule modify(int scheduleId, Schedule schedule){
        Schedule scheduleToUpdate = scheduleRepo.findById(scheduleId)
                .orElseThrow(() -> new EntityNotFoundException("Schedule not found"));

        validateSchedule(scheduleToUpdate.getProject().getPjId(), schedule);

        if (schedule.getType() != null) {
            scheduleToUpdate.setType(schedule.getType());
        }
        if (schedule.getKickOff() != null){
            scheduleToUpdate.setKickOff(schedule.getKickOff());
        }
        if (schedule.getFabIn() != null){
            scheduleToUpdate.setFabIn(schedule.getFabIn());
        }
        if (schedule.getFabOut() != null) {
            scheduleToUpdate.setFabOut(schedule.getFabOut());
        }
        if (schedule.getApproved() != null) {
            scheduleToUpdate.setApproved(schedule.getApproved());
        }

        return scheduleRepo.save(scheduleToUpdate);
    }

    // 스케쥴 삭제
    public void cancel(int scheduleId){
        Schedule scheduleToDelete = scheduleRepo.findById(scheduleId)
                .orElseThrow(() -> new EntityNotFoundException("Schedule not found"));
        scheduleRepo.delete(scheduleToDelete);
    }

    // 유효성 검사
    private boolean hasDuplicateScheduleType(int pjId, Schedule schedule) {
        return !scheduleRepo.findByTypeAndProject_PjId(schedule.getType(), pjId).isEmpty();
    }

    private boolean isAscendingDates(Schedule schedule) {
        List<LocalDate> dateList = new ArrayList<>();

        if (schedule.getKickOff() != null)
            dateList.add(schedule.getKickOff());
        if (schedule.getFabIn() != null)
            dateList.add(schedule.getFabIn());
        if (schedule.getFabOut() != null)
            dateList.add(schedule.getFabOut());
        if (schedule.getApproved() != null)
            dateList.add(schedule.getApproved());

        for (int i = 0; i < dateList.size() - 1; ++i) {
            if (dateList.get(i).isAfter(dateList.get(i + 1)))
                return false;
        }
        return true;
    }

    public void validateSchedule(int pjId, Schedule schedule) {
        if (hasDuplicateScheduleType(pjId, schedule))
            throw new DataIntegrityViolationException("Duplicate type found");

        if (!isAscendingDates(schedule))
            throw new IllegalArgumentException("Not ascending dates");
    }
}
