package com.verstappen.memorypalace.dto;

import jakarta.validation.constraints.NotBlank;

public class ConceptDTO {

    @NotBlank
    public String title;

    public String description;

    @NotBlank
    public String mediaUrl;

    public String memoryObject;
    public String location;
    public String visualCue;
}
