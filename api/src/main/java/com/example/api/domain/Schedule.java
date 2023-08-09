package com.example.api.domain;

import jakarta.persistence.*;

import java.time.LocalDate;

@Entity
public class Schedule {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int sdId;

    private String type;
    private LocalDate kickOff;
    private LocalDate fabIn;
    private LocalDate fabOut;
    private LocalDate approved;

    @ManyToOne
    @JoinColumn(name = "pjId", nullable = false)
    private Project project;

    // Getter & Setter
    public int getSdId() {
        return sdId;
    }

    public void setSdId(int sdId) {
        this.sdId = sdId;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public LocalDate getKickOff() {
        return kickOff;
    }

    public void setKickOff(LocalDate kickOff) {
        this.kickOff = kickOff;
    }

    public LocalDate getFabIn() {
        return fabIn;
    }

    public void setFabIn(LocalDate fabIn) {
        this.fabIn = fabIn;
    }

    public LocalDate getFabOut() {
        return fabOut;
    }

    public void setFabOut(LocalDate fabOut) {
        this.fabOut = fabOut;
    }

    public LocalDate getApproved() {
        return approved;
    }

    public void setApproved(LocalDate approved) {
        this.approved = approved;
    }

    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }
}
