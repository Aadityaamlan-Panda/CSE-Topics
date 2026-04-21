package com.verstappen.memorypalace.service;

import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import com.verstappen.memorypalace.dto.ConceptDTO;
import com.verstappen.memorypalace.model.Concept;
import com.verstappen.memorypalace.repository.ConceptRepository;

@Service
public class ConceptService {

    private final ConceptRepository repo;

    public ConceptService(ConceptRepository repo) {
        this.repo = repo;
    }

    public Concept save(ConceptDTO dto) {
        Concept c = new Concept();

        c.setTitle(dto.getTitle());
        c.setDescription(dto.getDescription());
        c.setMediaUrl(dto.getMediaUrl());
        c.setMemoryObject(dto.getMemoryObject());
        c.setLocation(dto.getLocation());
        c.setVisualCue(dto.getVisualCue());

        return repo.save(c);
    }

    public List<Concept> getAll() {
        return repo.findAllByOrderByIdAsc();
    }

    public Concept getById(Long id) {
        return repo.findById(id)
                .orElseThrow(() -> new RuntimeException("Concept not found"));
    }

    public void delete(Long id) {
        repo.deleteById(id);
    }

    public Concept update(Long id, ConceptDTO dto) {
        Concept c = getById(id);

        c.setTitle(dto.getTitle());
        c.setDescription(dto.getDescription());
        c.setMediaUrl(dto.getMediaUrl());
        c.setMemoryObject(dto.getMemoryObject());
        c.setLocation(dto.getLocation());
        c.setVisualCue(dto.getVisualCue());

        return repo.save(c);
    }

    public List<Concept> search(String keyword) {
        return repo.findByTitleContainingIgnoreCase(keyword);
    }

    public Page<Concept> getPaginated(Pageable pageable) {
        return repo.findAll(pageable);
    }
}