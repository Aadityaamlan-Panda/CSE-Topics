package com.verstappen.memorypalace.dto;

import jakarta.validation.constraints.NotBlank;

public class ConceptDTO {

    @NotBlank
    private String title;

    private String description;

    @NotBlank
    private String mediaUrl;

    private String memoryObject;
    private String location;
    private String visualCue;

    // GETTERS
    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public String getMediaUrl() {
        return mediaUrl;
    }

    public String getMemoryObject() {
        return memoryObject;
    }

    public String getLocation() {
        return location;
    }

    public String getVisualCue() {
        return visualCue;
    }

    // SETTERS
    public void setTitle(String title) {
        this.title = title;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setMediaUrl(String mediaUrl) {
        this.mediaUrl = mediaUrl;
    }

    public void setMemoryObject(String memoryObject) {
        this.memoryObject = memoryObject;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public void setVisualCue(String visualCue) {
        this.visualCue = visualCue;
    }
}