package com.example.api.domain;

import jakarta.persistence.*;

import java.util.ArrayList;
import java.util.List;

@Entity
public class Project {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "pjId")
    private int pjId;
    private String codeName;

    @OneToMany(mappedBy = "project")
    private List<Schedule> schedules = new ArrayList<>();

    // Getter & Setter
    public int getPjId() {
        return pjId;
    }

    public void setPjId(int pjId) {
        this.pjId = pjId;
    }

    public String getCodeName() {
        return codeName;
    }

    public void setCodeName(String codeName) {
        this.codeName = codeName;
    }
}
