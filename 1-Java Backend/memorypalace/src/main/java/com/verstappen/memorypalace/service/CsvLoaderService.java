package com.verstappen.memorypalace.service;

import java.io.InputStreamReader;
import java.util.List;

import org.springframework.stereotype.Service;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;
import com.verstappen.memorypalace.model.Concept;
import com.verstappen.memorypalace.repository.ConceptRepository;

@Service
public class CsvLoaderService {

    private final ConceptRepository repo;

    public CsvLoaderService(ConceptRepository repo) {
        this.repo = repo;
    }

    public void loadData(String filePath) {
        try {
            InputStreamReader reader = new InputStreamReader(
                    getClass().getClassLoader().getResourceAsStream(filePath));
            CsvToBean<Concept> csvToBean = new CsvToBeanBuilder<Concept>(reader)
                    .withType(Concept.class)
                    .withIgnoreLeadingWhiteSpace(true)
                    .build();

            List<Concept> concepts = csvToBean.parse();

            repo.deleteAll();
            repo.saveAll(concepts);

            System.out.println("CSV Data Loaded Successfully");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}