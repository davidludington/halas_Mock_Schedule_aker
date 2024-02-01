import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.io.*;


public class ScheduleBuilder {

    public static List<Map<String, String>> readSchedulePreferences(String filePath) throws IOException {
        List<Map<String, String>> schedules = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String[] headers = reader.readLine().split(","); // Assuming the first row contains headers

            String line;
            while ((line = reader.readLine()) != null) {
                String[] values = line.split(",");
                Map<String, String> schedule = new HashMap<>();
                for (int i = 0; i < headers.length; i++) {
                    schedule.put(headers[i], values[i]);
                }
                schedules.add(schedule);
            }
        }

        return schedules;
    }

    public static List<Map<String, String>> buildMockSchedule(List<Map<String, String>> schedulePreferences) {
        List<Map<String, String>> mockSchedule = new ArrayList<>();

        // Define the hours open and usual shift times
        String[] hoursOpen = {"6:30-10", "10-1", "1-5", "5-8", "8-11:30"};

        for (Map<String, String> schedule : schedulePreferences) {
            Map<String, String> employeeSchedule = new HashMap<>();
            String employeeName = schedule.get("Employee");

            for (String day : List.of("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")) {
                int availability = Integer.parseInt(schedule.get(day + " availability"));
                if (availability > 0) {
                    String shift = hoursOpen[availability - 1];
                    employeeSchedule.put(day, employeeName + " is scheduled for the shift " + shift);
                }
            }

            mockSchedule.add(employeeSchedule);
        }

        return mockSchedule;
    }

    public static void printMockSchedule(List<Map<String, String>> mockSchedule) {
        for (Map<String, String> employeeSchedule : mockSchedule) {
            for (Map.Entry<String, String> entry : employeeSchedule.entrySet()) {
                System.out.println(entry.getValue() + " on " + entry.getKey());
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // Specify the path to your CSV file
        String filePath = "SampleScheduleInput.csv";

        try {
            // Read employee schedule preferences from the CSV file
            List<Map<String, String>> schedulePreferences = readSchedulePreferences(filePath);

            // Build the mock schedule based on the preferences
            List<Map<String, String>> mockSchedule = buildMockSchedule(schedulePreferences);

            // Print the mock schedule
            printMockSchedule(mockSchedule);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

