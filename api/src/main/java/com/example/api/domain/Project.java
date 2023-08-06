package com.example.api.domain;

public class Project {
    private int pjId;
    private String codeName;

    public Project(int pjId, String codeName) {
        this.pjId = pjId;
        this.codeName = codeName;
    }

    public int getPjId() {
        return pjId;
    }

    public String getCodeName() {
        return codeName;
    }

    public void setPjId(int pjId) {
        this.pjId = pjId;
    }

    public void setCodeName(String codeName) {
        this.codeName = codeName;
    }
}
