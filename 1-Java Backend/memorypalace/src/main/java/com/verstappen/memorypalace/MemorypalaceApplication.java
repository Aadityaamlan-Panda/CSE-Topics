package com.verstappen.memorypalace;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.verstappen.memorypalace.service.CsvLoaderService;

@SpringBootApplication
public class MemorypalaceApplication {

	public static void main(String[] args) {
		SpringApplication.run(MemorypalaceApplication.class, args);
	}

	@Bean
	CommandLineRunner loadData(CsvLoaderService loader) {
		return args -> {
			System.out.println("Loading CSV data into database...");

			loader.loadData("data/concepts.csv");

			System.out.println("Data loading complete!");
		};
	}
}